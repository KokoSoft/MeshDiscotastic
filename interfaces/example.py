import logging

from modules.interfaces import InterfaceBase

logger = logging.getLogger(__name__)

class ExampleInterface(InterfaceBase):
	def __init__(
		self, 
		config : dict,
		**kwargs
	):
		pass

def get_driver():
	return ExampleInterface