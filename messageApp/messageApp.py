"""
 There should be a insightful documentation here
"""
import os.path

from datetime import datetime
from collections import OrderedDict
from messageApp.messages import Messages

class MessageApp():
	def __init__(self):
		self.messages = OrderedDict()
		
	def loadMessage(self, names):
		if type(names) is str:
			names = names,
		
		for name in names:
			if (not name in self.messages):
				filename = 'messages/messages_' + name + '.yaml'
				if os.path.isfile(filename):
					self.messages[name] = Messages(filename)
			else:
				self.messages[name].reload()

	def unloadMessage(self, names):
		if type(names) is str:
			names = names,
		
		for name in names:
			if (name in self.messages):
				self.messages.pop(name)

	def reload(self):
		for name, messages in self.messages.items():
			messages.reload()

	def getMessages(self):
		time = datetime.now()
		return self.getMessagesAtTime(time)

	def getMessagesAtTime(self, time):
		messageList = []
		for name, messages in self.messages.items():
			message = messages.getMessage(time)
			if message:
				messageList.append(message)
		return messageList
