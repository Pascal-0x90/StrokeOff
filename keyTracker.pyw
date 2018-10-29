#################################
#           StrokeOff           #
#          Nathan Smith         #
#  Software protection against  #
#       HID Attacks via USB     #
#################################

# This project is based off of an idea inspired by duckHunt, a project by Pedro M. Sosa
# His/her github is: https://github.com/pmsosa/duckhunt
def main():
	# Import packages
	import pyHook
	import pygame
	import yaml
	import datetime
	import ctypes
	import win32ui
	from StrokeOff import yamlWriter

	lastTime = 0
	avg = 0
	config = yaml.safe_load(open("config.yml"))
	# Load some settings from the config file
	#################################################
	threshold = config["threshold"]
	password = config["password"]
	filename = config["filename"]
	blacklist = config["blacklist"]
	policy = config["policy"]
	lastkey = ""
	windowExist = False
	#################################################

	def log(event):
		global prevWindow

		x = open(filename, "a+")
		y = open(filename + "_notime.txt", "a+")
		if 32 < event.Ascii < 127:
			x.write(str(datetime.datetime.now()) + "\n" + chr(event.Ascii) + " \n")
			y.write(chr(event.Ascii))
		else:
			x.write("[%s]" % event.Key)
			y.write("[%s]" % event.Key)
			x.close()
			y.close()
		return

	def OnKeyboardEvent(event):
		global lastTime, avg, lastkey, windowExist
		windowExist = False
		print(event.Time)
		avg = (event.Time - lastTime) / 2
		lastTime = event.Time
		print(avg)
		print(event.WindowName)
		# Blacklisting
		for window in blacklist.split(","):
			if window in event.WindowName:
				windowExist = True
		print(windowExist)
		if avg < threshold and lastkey != str(event.Key) or windowExist:
			log(event)
			lastkey = str(event.Key)
			if policy == "paranoid":
				print(True)
				ctypes.windll.user32.LockWorkStation()
			return False
		else:
			lastkey = str(event.Key)

			return True

	# create a hook manager
	hm = pyHook.HookManager()
	# watch for all keyboard events
	hm.KeyDown = OnKeyboardEvent
	# set the hook
	hm.HookKeyboard()

	pygame.init()

	while 1:
		pygame.event.pump()


if __name__ == '__main__':
	main()