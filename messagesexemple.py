"""
	Class to store data for the message class
	copy this file to messagescustom.py to make your own
	cp messagesexemple.py messagescustom.py
"""

from messages import Messages

class MyMessages(Messages):
	title = "Is it noon ?"
	
	messages = {
		'04:00' : "No wait !",
		'12:00' : "Yes it is !",
		'13:00' : "Wait until tomorrow !",
	}
