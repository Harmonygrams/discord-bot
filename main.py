import pyautogui as pt 
from time import sleep 
import pyperclip 
import random 
import words

#time will take for the robot to chat in seconds
min_time = 20
max_time = 70

#Sleeping for 3 seconds before going to whatsapp 
sleep(3) 
position1 = pt.locateOnScreen("smiley_paperclip.png", confidence = .6)
x = position1[0] 
y = position1[1] 

#Here is the word to paste 

#Get message 
def get_message(num): 
	global x, y
	text = words.words_spiller()
	text = text[num]
	position1 = pt.locateOnScreen("smiley_paperclip.png", confidence = .6)
	x = position1[0]
	y = position1[1] 
	pt.moveTo(x,y, duration=.05)
	pt.moveTo(x - 200, y + 20, duration= .05)
	pt.click()
	pyperclip.copy(text)
	pt.typewrite(text, interval=.02)
	pt.typewrite("\n", interval=.01)

num = 10

while True: 
	get_message(num)
	number = random.randint(min_time, max_time)
	print("I'm  going to wait for {} seconds and the index is {}".format(int(number), num))
	sleep(number)
	num += 1

