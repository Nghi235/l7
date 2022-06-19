#!/usr/bin/python3



from sys import argv

from framework import console, module  


def run():
	main_console = console()
	main_console.rsversion = "4.1 (Pre)"
	main_console.user_argv = argv

	module("setup", main_console)

	main_console.run()


if __name__ == "__main__":
	run()
