"""
 There should be a insightful documentation here
"""
import glob
import os.path
from datetime import datetime
from collections import OrderedDict
from messageApp.messages import Messages

class MessageApp():
	def __init__(self, messagesDir='messages', filePattern="messages_"):
		self.filePattern = os.path.join(messagesDir, filePattern)
		self.messages = OrderedDict()
		
	def loadMessage(self, names):
		if type(names) is str:
			names = (names, )
		
		fileList = self._getFileList()
		for name in names:
			if (name not in self.messages) and (name in fileList):
				filename = self.filePattern + name + '.yaml'
				self.messages[name] = Messages(filename)
			else:
				self.messages[name].reload()

	def unloadMessage(self, names):
		if type(names) is str:
			names = (names, )
		
		for name in names:
			if (name in self.messages):
				self.messages.pop(name)

	def listMessages(self):
		loadedList = [ name for name, _ in self.messages.items() ]
		notloadedList = list(set(self._getFileList()) - set(loadedList))
		return notloadedList, loadedList

	def reload(self):
		for _, messages in self.messages.items():
			messages.reload()

	def getMessages(self):
		time = datetime.now()
		return self.getMessagesAtTime(time)

	def getMessagesAtTime(self, time):
		messageList = []
		for _, messages in self.messages.items():
			message = messages.getMessage(time)
			if message:
				messageList.append(message)
		return messageList

	def _getFileList(self):
		fileList = glob.glob(self.filePattern + "*.yaml")
		nameStartAt = len(self.filePattern)
		fileList = [ name[nameStartAt:-5] for name in fileList ]
		return fileList
