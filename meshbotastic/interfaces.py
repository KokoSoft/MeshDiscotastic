import logging
import importlib
from typing import *
from abc import ABC, abstractmethod

from meshbotastic.utils import *

from meshtastic.mesh_interface import MeshInterface

logger = logging.getLogger(__name__)

class InterfaceFactory:
	counter = 0

	@staticmethod
	def load_driver(name: str):
		module_name = f"interfaces.{name}"
		module = importlib.import_module(module_name)

		if hasattr(module, "get_driver"):
			return module.get_driver()
		else:
			raise RuntimeError(f"Interface driver '{name}' does not define a 'get_driver' method!")

	@staticmethod
	def create(config : dict):
		try:
			name = config.get("name", f"if{InterfaceFactory.counter}")
			driver_name = config["driver"]

			driver = InterfaceFactory.load_driver(driver_name)

			params = {
				"config": config,
				"interface_name": name
			}

			interface = driver(**params)

			#debug = config.get("debug", False)
			#if debug:
			#	debugOut = logging.getLogger(f"interface[{name}]")
			#else:
			#	debugOut = None

			InterfaceFactory.counter += 1
			return interface
		except KeyError as e:
			error_exit(f"The required field {e} is missing in the interface '{name}' configuration.", logger)
		except RuntimeError as e:
			error_exit(f"Unable to create '{name}' interface. {e}", logger)
		except ModuleNotFoundError as e:
			error_exit(f"Unknown interface driver {driver_name} for interface {name}. {e}", logger)
