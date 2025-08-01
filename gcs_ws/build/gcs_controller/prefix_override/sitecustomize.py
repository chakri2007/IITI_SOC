import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bhav/IITISoC-25-IVR09/gcs_ws/install/gcs_controller'
