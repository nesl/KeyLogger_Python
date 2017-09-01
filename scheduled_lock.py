'''
Python Schedued Windows LockScreen
====================================
Coded By: Vikranth

'''
import schedule
import time
import ctypes

def job():
    ctypes.windll.user32.LockWorkStation()
    return schedule.CancelJob

'''    
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
'''


def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True


var = raw_input("Enter the time in the 24 hr format hh:mm ")
schedule.every().day.at(var).do(job)
hide()

while True:
    schedule.run_pending()
    time.sleep(1)