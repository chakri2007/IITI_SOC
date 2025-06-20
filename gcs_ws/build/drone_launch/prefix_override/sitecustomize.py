import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/chakrapani/drone_files/IITI_SOC/gcs_ws/install/drone_launch'
