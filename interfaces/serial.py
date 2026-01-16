import logging

import meshtastic.serial_interface

logger = logging.getLogger(__name__)

class SerialInterface(meshtastic.tcp_interface.SerialInterface):
	def __init__(
		self,
		config : dict,
		**kwargs
	):
		try:
			dev_path = config.get("device_path")

			super().__init__(dev_path)
			#	def __init__(
			#        self,
			#        devPath: Optional[str] = None,
			#        debugOut=None,
			#        noProto: bool = False,
			#        connectNow: bool = True,
			#        noNodes: bool = False,
			#        timeout: int = 300

			# There is no other way to determine whether opening the interface succeeded.
			# We can only check whether the constructor created the stream.
			if not hasattr(self, "stream"):
				raise RuntimeError()

		except FileNotFoundError:
			# Handle the case where the serial device is not found
			raise RuntimeError(f"The serial device at '{dev_path}' was not found!")
		except PermissionError as e:
			# Handle the case where the serial device is not found
			raise RuntimeError(f"A permission error occurred while opening the serial device '{dev_path}'. {e}")
		except OSError as e:
			raise RuntimeError(f"The serial device '{dev_path}' couldn't be opened, it might be in use by another process. {e}")

def get_driver():
	return SerialInterface
