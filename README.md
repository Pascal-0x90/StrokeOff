# StrokeOff
Block input from HID attacks (Rubberducky blocker)
------------------------------------------------------
Main GUI is strokeOff.py. This will open a GUI which can have values entered into it:
Policy: Normal or Paranoid
Password: <Anything you want> - Doesnt do anything currently
Blacklist: Blacklist programs you don't use so they get blocked input instantly
Size: just enter the number 1 here. It doesnt do anything currently
Randdrop: Same with this one
Filename: put something fancy like log.txt

Example: 
  Policy: Paranoid
  Password: quack
  BlackList:  Command Prompt
  Size: 1
  Randdrop: 1
  Filename: log.txt
  
Tick the manual thresh radio button to enable threshold:
  Comfortable threshold is around 30. Agressive is 50 and lax would be around 15-20. This is the main hitter of the program since it bases the concept that humans cant type as fast as USB Rubberduckies or other HID attack platforms. 
  
 Hit save settings to save to a yaml file.
 
 Then hit start and it should run the keyTracker.pyw (rename to .py probably otherwise you'll need to kill the process manually in TskMgr.)
 
 *** DIFFERENCE BETWEEN NORMAL AND PARANOID ******
 Mainly just paranoid locks the users screen therefore mitigating the "oh shit i left my computer unlocked" problem and someone tries a HID attack

Packages:
You will need:
  - tkinter
  - os
  - subprocess
  - yaml

Main files:
  - yamlWriter
  - keyTracker
  - stroekGUI
  
StrokeOff.py is an alpha of strokeOff.

ISSUES: 
  - I cannot properly compile both into one exe properly
  - Usually when I do one or the other will work coherently
  - I can however get things to work when theres atleast one .py file hanging outside the exe
  
I used pyInstaller so if anyone wants to fandangle with that or something else and tell me how they did it that'd be pretty neato. I'll probably try to finish it sometime towards the end of December when I amd not slammed with other commitments.
