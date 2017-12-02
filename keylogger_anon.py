from AppKit import NSWorkspace
from pynput import keyboard
import logging
import os

cwd = os.getcwd()
log_directory = os.path.join(cwd,"Key_logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

os.chdir(log_directory)

i = 0
while os.path.exists("key_log%s.txt" %i):
    i += 1

#log_dir = ""
#logging.basicConfig(filename = (log_dir + "key_log%s.txt" % i), level=logging.INFO, format='%(asctime)s.%(msecs)03d,%(message)s', datefmt='%s')

formatter = logging.Formatter('%(asctime)s.%(msecs)03d,%(message)s', datefmt='%s')
def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

key_logger = setup_logger('key_logger', 'key_log%s.txt' %i)

left = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b','Q','W','E','R','T','A','S','D','F','G','Z','X','C','V','B']
right = ['y','u','i','o','p','h','j','k','l',';','n','m',',','.','/','Y','U','I','O','P','H','J','K','L',':','N','M','<','>','?']

def on_press(key):
    try:
    	active_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    	if key.char in left:
    		key = 'left'
    	elif key.char in right:
    		key = 'right'
    	else:
    		key = key

    	key_logger.info('{0}, pressed, {1}'.format(key, active_app_name))

    except AttributeError:
    	active_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    	key_logger.info('{0}, pressed, {1}'.format(key, active_app_name))

def on_release(key):
	try:
		active_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
		if key.char in left:
			key = 'left'
		elif key.char in right:
			key = 'right'
		else:
			key = key

		key_logger.info('{0}, released, {1}'.format(key, active_app_name))

	except AttributeError:
		active_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
		key_logger.info('{0}, released, {1}'.format(key, active_app_name))

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()