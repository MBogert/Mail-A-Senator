# command_enum.py
from enum import Enum

class command(Enum):
	HELP = 'help'
	LIST = 'list'
	FIND = 'find'
	MAKE = 'make'
	EXIT = 'exit'