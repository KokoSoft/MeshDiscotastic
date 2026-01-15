import json5
import logging
from typing import *
import sys
import logging

logger = logging.getLogger(__name__)

def load_config(name : str | None = None) -> dict[str, Any]:
	try:
		with open("config.json", "r", encoding="utf-8") as config_file:
			config = json5.load(config_file)
			return config[name] if name else config
	except FileNotFoundError:
		logger.critical("The config.json file was not found.")
		sys.exit(1)
	except ValueError as e:
		logger.critical(f"An error ocurred while parsing config.json: {e}")
		sys.exit(1)
	except KeyError as e:
		logger.critical(f"The required section {e} is missing in the config.json file.")
		sys.exit(1)
	except Exception as e:
		logger.critical(f"An unexpected error occurred while loading config.json: {e}")
		raise

class Config:
	def __init__(self):
		self.config = load_config()
	
	def get_section(self, name : str):
		try:
			return self.config[name]
		except KeyError as e:
			logger.critical(f"The required section {e} is missing in the config.json file.")
			sys.exit(1)

	def get_port(self):
		return self.data.get("port")

	def __getitem__(self, key):
		return self.data[key]
