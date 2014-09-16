"""
Return list of messages given a datetime (empty is now) : [ (title, message), ]
Load, unload and reload messages give their name
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
# TODO _nameList[], _loadedMessages[], _filePattern, 
	
	# given a (string) messageName (, separate list)
	# get all named messageObject
	# and [re]-instanciate a Messages in _loadedMessages[] with it
	def loadMessage(self, names):
		if type(names) is str:
			names = (names, )
		
		fileList = self._getFileList()
		for name in names:
#TODO only check for names
			if (name not in self.messages) and (name in fileList):
				filename = self.filePattern + name + '.yaml'
# TODO _getMessageObject(name):
				self.messages[name] = Messages(filename)
# no need
			else:
				self.messages[name].reload()

	# given a (string) messageName (, separate list)
	# unload a Messages in _loadedMessages[]
	def unloadMessage(self, names):
		if type(names) is str:
			names = (names, )
		
		for name in names:
			if (name in self.messages):
				self.messages.pop(name)

	# return (_loadedMessages[])
	def listMessages(self):
		loadedList = [ name for name, _ in self.messages.items() ]
		notloadedList = list(set(self._getFileList()) - set(loadedList))
		return notloadedList, loadedList

#TODO reload all _loadedMessages[]
	def reload(self):
		for _, messages in self.messages.items():
			messages.reload()

	# return list of estcequecestbientot [ (title, message), ] at now
	def getMessages(self):
		time = datetime.now()
		return self.getMessagesAtTime(time)

	# return list of estcequecestbientot [ (title, message), ] given a datetime
	def getMessagesAtTime(self, time):
		messageList = []
		for _, messages in self.messages.items():
			message = messages.getMessage(time)
			if message:
				messageList.append(message)
		return messageList

#TODO
# def getMessageObject(self, name):
# return a messageObject given a name
# using _filePattern and the file system

	# def _gatNameList(self):
	# return an updated list of name of existing [messageObject]
	# using _filePattern and the file system
	def _getFileList(self):
		fileList = glob.glob(self.filePattern + "*.yaml")
		nameStartAt = len(self.filePattern)
		fileList = [ name[nameStartAt:-5] for name in fileList ]
		return fileList
