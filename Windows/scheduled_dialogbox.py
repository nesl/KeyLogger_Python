'''
Python Schedued Login Box
====================================
Coded By: Vikranth

'''
import schedule
import time
import ctypes
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry

schedule.clear()
passwords = ["Hello", "How", "Are", "You"]
i=0
password = passwords[i]

def try_login():
	global window, password_guess, password
	print("Trying to login...")
	if password_guess.get() == password:
		messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
		window.destroy()
		global i
		i = (i + 1) % 4
		password = passwords[i]
		
	else:
		messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")


def on_closing():
	pass

def job():
	global window, password_guess

	window, password_guess = create_window()

	#Main Starter
	window.lift()
	window.attributes('-topmost',True)
	window.mainloop()
	
	#return schedule.CancelJob

def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True


var = raw_input("Enter the time in the 24 hr format hh:mm ")
#schedule.every().day.at(var).do(job)
schedule.every(10).seconds.do(job)
#hide()

def create_window():
#Gui Things
	window = Tk()
	window.resizable(width=FALSE, height=FALSE)
	window.title("Log-In")
	window.geometry("1500x2000")
	window.protocol("WM_DELETE_WINDOW", on_closing)
	window.overrideredirect(True)

	##Creating the username & password entry boxes
	password_text = Label(window, text="Password:")
	password_guess = Entry(window, show="*")

	#attempt to login button
	attempt_login = Button(text="Login", command=try_login)

	password_text.pack()
	password_guess.pack()
	attempt_login.pack()
	return window, password_guess

#window, password_guess = create_window()


while True:
    schedule.run_pending()
    time.sleep(1)


