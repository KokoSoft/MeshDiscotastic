import logging

import meshtastic.ble_interface

logger = logging.getLogger(__name__)

class BLEInterface(meshtastic.ble_interface.BLEInterface):
	def __init__(
		self,
		config : dict,
		**kwargs
	):
		try:
			address = config.get("address")
			super().__init__(address)
			#def __init__( # pylint: disable=R0917
			#	self,
			#	address: Optional[str],
			#	noProto: bool = False,
			#	debugOut: Optional[io.TextIOWrapper]=None,
			#	noNodes: bool = False,
			#	timeout: int = 300,

		except meshtastic.ble_interface.BLEInterface.BLEError as e:
			raise RuntimeError(e)

def get_driver():
	return BLEInterface
