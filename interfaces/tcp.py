import logging

import meshtastic.tcp_interface

logger = logging.getLogger(__name__)

class TCPInterface(meshtastic.tcp_interface.TCPInterface):
	def __init__(
		self,
		config : dict,
		**kwargs
	):
		host = config.get("hostname", "127.0.0.1")
		port = config.get("port", meshtastic.tcp_interface.DEFAULT_TCP_PORT)

		try:
			super().__init__(
				host,
				portNumber = config.get("port", meshtastic.tcp_interface.DEFAULT_TCP_PORT),
				connectNow = True,
				#debugOut = debugOut,
				#noProto=args.noproto,
				#noNodes=args.no_nodes,
				#timeout = args.timeout,
			)
		except (TimeoutError, ConnectionAbortedError) as e:
			raise RuntimeError(f"Unable to connect to {host} on port {port}. {e}")

def get_driver():
	return TCPInterface