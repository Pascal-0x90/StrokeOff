#################################
#           StrokeOff           #
#          Nathan Smith         #
#  Software protection against  #
#       HID Attacks via USB     #
#################################

from tkinter import *
from StrokeOff import yamlWriter
import os
import subprocess
from subprocess import Popen, PIPE

def main():
	window = Tk()
	window.title("StrokeOff")
	window.geometry('450x350')
	# Labels
	lbl = Label(window, text="Stroke Off Setup", font=("Arial Bold", 16))
	lbl0 = Label(window, text="Policy: ", font=("Arial", 14))
	lbl1 = Label(window, text="Password: ", font=("Arial", 14))
	lbl2 = Label(window, text="BlackList: ", font=("Arial", 14))
	lbl3 = Label(window, text="Threshold: ", font=("Arial", 14))
	lbl4 = Label(window, text="Size: ", font=("Arial", 14))
	lbl5 = Label(window, text="Randdrop: ", font=("Arial", 14))
	lbl6 = Label(window, text="Filename: ", font=("Arial", 14))
	lbl7 = Label(window, text="Average ", font=("Arial", 14))
	# Label Place
	lbl.grid(column=0, row=0)
	lbl0.grid(column=0, row=1)
	lbl1.grid(column=0, row=2)
	lbl2.grid(column=0, row=3)
	# lbl3.grid(column=0, row=4)
	lbl4.grid(column=0, row=5)
	lbl5.grid(column=0, row=6)
	lbl6.grid(column=0, row=7)
	# Text fields
	txt = Entry(window, width=15)
	txt1 = Entry(window, width=15)
	txt2 = Entry(window, width=15)
	txt3 = Entry(window, width=15)
	txt4 = Entry(window, width=15)
	txt5 = Entry(window, width=15)
	txt6 = Entry(window, width=15)
	txt7 = Entry(window, width=15)
	# Place TextFields
	txt.grid(column=1, row=1)  # Policy
	txt1.grid(column=1, row=2)  # Password
	txt2.grid(column=1, row=3)  # BlackList
	# txt3.grid(column=1, row=4)  # Threshold
	txt4.grid(column=1, row=5)  # Size
	txt5.grid(column=1, row=6)  # Randdrop
	txt6.grid(column=1, row=7)  # Filename

	# txt7.grid(column=1, row=8)  # Filename
	def display():
		if v.get() is 1:
			lbl3.grid(column=0, row=4)
			txt3.grid(column=1, row=4)  # Filename
		elif v.get() is 2:
			lbl3.grid_remove()
			txt3.grid_remove()
		elif v.get() is 3:
			lbl3.grid_remove()
			txt3.grid_remove()

	def clicked():
		if v.get() is 2:
			yamlWriter.trainer(txt.get().lower(), txt1.get().lower(), txt2.get(), txt4.get().lower(),
							   txt6.get().lower())
		elif v.get() is 1:
			yamlWriter.trainer_avg(txt.get().lower(), txt1.get().lower(), txt2.get(), int(txt3.get().lower()),
								   int(txt4.get().lower()), txt6.get().lower())
		elif v.get() is 3:
			yamlWriter.trainer_avg(txt.get().lower(), txt1.get().lower(), txt2.get().lower(), 30,
								   int(txt4.get().lower()), txt6.get().lower())

	def execute():
		window.destroy()
		subprocess.call("KeyTracker.exe", shell=True, stderr=subprocess.STDOUT)



	# Buttons
	btn = Button(window, text="Save Settings", command=clicked, font=("Arial", 14))
	btn.grid(column=1, row=9)
	btn1 = Button(window, text="Start", command=execute, font=("Arial", 14))
	btn1.grid(column=1, row=10)
	# Radio Buttons
	v = IntVar()
	v.set(2)  # initializing the choice, i.e. Python
	rad1 = Radiobutton(window, text='Manual Thresh', value=1, variable=v, command=display)
	rad2 = Radiobutton(window, text='Auto Thresh', value=2, variable=v, command=display)
	rad3 = Radiobutton(window, text='Default Thresh', value=3, variable=v, command=display)
	# Place RadioButtons
	rad2.grid(column=2, row=4)
	rad1.grid(column=2, row=5)
	rad3.grid(column=2, row=6)
	window.mainloop()


main()
