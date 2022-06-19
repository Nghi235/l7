

from os import chdir, path, system
from random import choice
from time import sleep

import requests
from framework import console  
from framework import event  
from framework import module  
from framework import tools  

try:
	import readline 
except Exception:  
	pass


event = event()
tools = tools()


class Main:
	def __init__(selfie, console):  
		global var
		global self
		self = selfie
		var = console  

		var.modules = {}
		self._add_commands()

		

		var.session = [[False, ""], [False, []]]  
		var.server = [False, True, "ip", "pass", 1]  
		if len(var.user_argv) != 1:
			if var.user_argv[1] == "--connect":
				var.server = [True, False, var.user_argv[2], var.user_argv[3], 1]
				status = requests.post((var.server[2] + "reset"), data={"password": var.server[3]}).text

	

	def banner(self):  
		banner_logo = ("Nguyễn Nghị Attack Layer7")
		banner_logo = ("")
		banner_logo = ("Hãy Nhập l7 Để Tấn Công")
		
		print(banner_logo)
        
	@event.event
	def on_ready():
		system("clear || cls")
		self.banner()
		

	@event.event
	def on_command_not_found(command):
		quit()
		

	

	

	def _add_commands(self):
		
		
		

		
		var.modules["Layer7"] = console()
		

	

	def check_session(self):
		if var.session[1][0] and len(var.session[1][1]) >= 1:
			if len(var.session[1][1][0]) >= 1:
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			else:
				var.session[1][1] = var.session[1][1][1:]
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			var.run_command = run_following

	

	

	

	@event.command
	def l7():
		module("attack", var.modules["Layer7"])
		var.modules["Layer7"].session = var.session
		var.modules["Layer7"].server = var.server
		var.modules["Layer7"].run()

	

	
	

	

	

	

	@event.command
	def clear():
		system("clear || cls")

	@event.event
	def on_command():
		print("", end="")

	@event.event
	def on_interrupt():
		self.exit_console()


def setup(console):
	console.ps1 = ">> "
	console.add(Main(console), event)
