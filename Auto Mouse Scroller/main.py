import pyautogui
import time
import keyboard
import os
# Safety first
pyautogui.FAILSAFE = True
# greet
user_notify = 'This is only a concept DEMO\nAt want speed you want to read?\n1. Fast\n2. Normal\n3. Slow\n4. Very Slow'
# alert
alert_text = "The program is about to start. Relocate your mouse on the position for the scrolling to work. This program will be excueted in 3 seconds after the [OK] is pressed.\nTo stop this program, click shift on your keyboard. You can also use the Crtl+C on terminal to manually stop the scrolling."
# abort
abort_text = "The program was aborted. Thanks for testing."

# notify that the program's about to start
def start_notify(): 
	pyautogui.alert(text=alert_text, title="Program Alert")

# notify that the program ended 
def aborted():
	pyautogui.alert(text=abort_text, title="Program Alert")

# notify that the program ended with false respond
def type_invalid():
	pyautogui.alert(text='Invalid Input', title="Program Warning")


# Ask user the speed of the program
# check if it is string
try:
	user_input = int(pyautogui.prompt(text=user_notify, title='Program Setup' , default='Choose Index'))
except ValueError:
	type_invalid()


try:
	if user_input:
		start_notify()
		time.sleep(3)

		while True:
			if keyboard.is_pressed('shift'):
				aborted()
				break
			elif user_input == 4:
				pyautogui.scroll(-5)
			elif user_input == 3:
				pyautogui.scroll(-10)
			elif user_input == 2:
				pyautogui.scroll(-15)
			elif user_input == 1:
				pyautogui.scroll(-20)
			else:
				type_invalid()
				break	
	else:
		type_invalid()	



except (KeyboardInterrupt, NameError): # Exception handling
	aborted()

