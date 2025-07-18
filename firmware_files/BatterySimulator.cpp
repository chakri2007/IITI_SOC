/****************************************************************************
 *
 *   Copyright (c) 2020 PX4 Development Team. All rights reserved.
 *   (unchanged license header)
 ****************************************************************************/

#include "BatterySimulator.hpp"

BatterySimulator::BatterySimulator() :
	ModuleParams(nullptr),
	ScheduledWorkItem(MODULE_NAME, px4::wq_configurations::hp_default),
	_battery(1, this, BATTERY_SIMLATOR_SAMPLE_INTERVAL_US, battery_status_s::BATTERY_SOURCE_POWER_MODULE)
{
}

BatterySimulator::~BatterySimulator()
{
	perf_free(_loop_perf);
}

bool BatterySimulator::init()
{
	ScheduleOnInterval(BATTERY_SIMLATOR_SAMPLE_INTERVAL_US);
	return true;
}

void BatterySimulator::Run()
{
	if (should_exit()) {
		ScheduleClear();
		exit_and_cleanup();
		return;
	}

	perf_begin(_loop_perf);

	if (_parameter_update_sub.updated()) {
		parameter_update_s param_update;
		_parameter_update_sub.copy(&param_update);
		updateParams();
	}

	updateCommands();

	if (_vehicle_status_sub.updated()) {
		vehicle_status_s vehicle_status;
		if (_vehicle_status_sub.copy(&vehicle_status)) {
			_armed = (vehicle_status.arming_state == vehicle_status_s::ARMING_STATE_ARMED);
		}
	}

	const hrt_abstime now_us = hrt_absolute_time();
	const float discharge_interval_us = _param_sim_bat_drain.get() * 1000 * 1000;

	// 🟡 Modified section: read battery percentage from /tmp/sim_voltage.txt
	bool overridden_by_ros = false;

	// Construct file path based on PX4 instance number
	char path[64] = {};
	snprintf(path, sizeof(path), "/tmp/sim_voltage_drone%d.txt", px4::instance());

	// Check if file exists before opening
	if (access(path, F_OK) == 0) {
		FILE *fp = fopen(path, "r");
		if (fp != nullptr) {
			float new_pct = NAN;
			if (fscanf(fp, "%f", &new_pct) == 1 && new_pct >= 0.0f && new_pct <= 1.0f) {
				_battery_percentage = new_pct;
				overridden_by_ros = true;
			}
			fclose(fp);
		}
	}

	// fallback to internal drain logic
	if (!overridden_by_ros) {
		if (_armed) {
			if (_last_integration_us != 0) {
				_battery_percentage -= (now_us - _last_integration_us) / discharge_interval_us;
			}
			_last_integration_us = now_us;
		} else {
			_battery_percentage = 1.f;
			_last_integration_us = 0;
		}
	}


	float ibatt = -1.0f;
	_battery_percentage = math::max(_battery_percentage, _param_bat_min_pct.get() / 100.f);

	float vbatt = math::interpolate(_battery_percentage, 0.f, 1.f,
					_battery.empty_cell_voltage(),
					_battery.full_cell_voltage());

	if (_force_empty_battery) {
		vbatt = _battery.empty_cell_voltage();
	}

	vbatt *= _battery.cell_count();

	_battery.setConnected(true);
	_battery.updateVoltage(vbatt);
	_battery.updateCurrent(ibatt);
	_battery.updateAndPublishBatteryStatus(now_us);

	perf_end(_loop_perf);
}

void BatterySimulator::updateCommands()
{
	vehicle_command_s vehicle_command;

	while (_vehicle_command_sub.update(&vehicle_command)) {
		if (vehicle_command.command != vehicle_command_s::VEHICLE_CMD_INJECT_FAILURE) {
			continue;
		}

		bool handled = false;
		bool supported = false;

		const int failure_unit = static_cast<int>(vehicle_command.param1 + 0.5f);
		const int failure_type = static_cast<int>(vehicle_command.param2 + 0.5f);
		const int instance = static_cast<int>(vehicle_command.param3 + 0.5f);

		if (failure_unit == vehicle_command_s::FAILURE_UNIT_SYSTEM_BATTERY) {
			if (failure_type == vehicle_command_s::FAILURE_TYPE_OK) {
				handled = true;
				PX4_INFO("CMD_INJECT_FAILURE, battery ok");
				supported = false;

				if (instance == 0) {
					supported = true;
					_force_empty_battery = false;
				}
			} else if (failure_type == vehicle_command_s::FAILURE_TYPE_OFF) {
				handled = true;
				PX4_WARN("CMD_INJECT_FAILURE, battery empty");
				supported = false;

				if (instance == 0) {
					supported = true;
					_force_empty_battery = true;
				}
			}
		}

		if (handled) {
			vehicle_command_ack_s ack{};
			ack.command = vehicle_command.command;
			ack.from_external = false;
			ack.result = supported ?
				     vehicle_command_ack_s::VEHICLE_CMD_RESULT_ACCEPTED :
				     vehicle_command_ack_s::VEHICLE_CMD_RESULT_UNSUPPORTED;
			ack.timestamp = hrt_absolute_time();
			_command_ack_pub.publish(ack);
		}
	}
}

int BatterySimulator::task_spawn(int argc, char *argv[])
{
	BatterySimulator *instance = new BatterySimulator();

	if (instance) {
		_object.store(instance);
		_task_id = task_id_is_work_queue;

		if (instance->init()) {
			return PX4_OK;
		}
	} else {
		PX4_ERR("alloc failed");
	}

	delete instance;
	_object.store(nullptr);
	_task_id = -1;
	return PX4_ERROR;
}

int BatterySimulator::custom_command(int argc, char *argv[])
{
	return print_usage("unknown command");
}

int BatterySimulator::print_usage(const char *reason)
{
	if (reason) {
		PX4_WARN("%s\n", reason);
	}

	PRINT_MODULE_DESCRIPTION(R"DESCR_STR(
### Description
Simulates battery behavior in PX4 SITL. Modified to support external recharge control via file.

)DESCR_STR");

	PRINT_MODULE_USAGE_NAME("battery_simulator", "system");
	PRINT_MODULE_USAGE_COMMAND("start");
	PRINT_MODULE_USAGE_DEFAULT_COMMANDS();
	return 0;
}

extern "C" __EXPORT int battery_simulator_main(int argc, char *argv[])
{
	return BatterySimulator::main(argc, argv);
}

