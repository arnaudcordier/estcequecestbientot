"""
Return list of messages given a datetime (empty is now) : [ (title, message), ]
Load, unload and reload messages give their name
"""
import yaml
import glob
import os.path
from datetime import datetime
from collections import OrderedDict
from messageApp.messages import Messages

class MessageApp():
	def __init__(self, messagesDir='messages', filePattern="messages_"):
		self._filePattern = os.path.join(messagesDir, filePattern)
		self._loadedMessages = OrderedDict()

	# return list of estcequecestbientot [ (title, message), ] at now
	def getMessages(self):
		time = datetime.now()
		return self.getMessagesAtTime(time)

	# given a datetime
	# return list of estcequecestbientot [ (title, message), ]
	def getMessagesAtTime(self, time):
		estcequecestbientot = []
		for _, messages in self._loadedMessages.items():
			message = messages.getMessage(time)
			if message:
				estcequecestbientot.append(message)
		return estcequecestbientot

	# given a (string) messageNames (a , separate list)
	# [re]-instanciate some Messages in _loadedMessages[] with it
	def loadMessage(self, messageNames):
		#TODO: do not loose the order of the messages and write a TEST for it !
		if type(messageNames) is str:
			messageNames = (messageNames, )
		for name in messageNames:
			messageObject = self._getMessageObject(name)
			if messageObject:
				self._loadedMessages[name] = Messages(messageObject)

	# given a (string) messageNames (a , separate list)
	# unload some Messages in _loadedMessages[]
	def unloadMessage(self, messageNames):
		if type(messageNames) is str:
			messageNames = (messageNames, )
		for name in messageNames:
			if (name in self._loadedMessages):
				self._loadedMessages.pop(name)

	# reload all _loadedMessages[]
	def reload(self):
		for name, _ in self._loadedMessages.items():
			self.loadMessage(name)

	# return (notloadedList, loadedList)
	def listMessages(self):
		loadedList = [ name for name, _ in self._loadedMessages.items() ]
		notloadedList = list(set(self._getNameList()) - set(loadedList))
		return notloadedList, loadedList

	# given a name
	# return a messageObject
	# using _filePattern and the file system
	def _getMessageObject(self, name):
		nameList = self._getNameList()
		if name in nameList:
			filename = self._filePattern + name + '.yaml'
			f = open(filename, 'r')
			messageObject = yaml.load(f)
			return messageObject
		return None

	# return an updated list of name of existing [messageObject]
	# using _filePattern and the file system
	def _getNameList(self):
		fileList = glob.glob(self._filePattern + "*.yaml")
		nameStartAt = len(self._filePattern)
		nameList = [ name[nameStartAt:-5] for name in fileList ]
		return nameList
