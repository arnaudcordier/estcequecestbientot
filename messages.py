"""
	A class to handle messages
"""

from datetime import datetime
from collections import OrderedDict
import yaml

class Messages():
	title = "Configure your own title please !"
	messages = {'00:00' : "Configure your own messages please !"}

	def __init__(self, messagesFile):
		self.messagesFile = messagesFile
		self.load()

	# initialise from a file and create messages dict from it
	def load(self):
		self.loadVariables(self.messagesFile)
		self.sortedMessages = self.createMessagesDict(self.messages)

	# load conf file and instanciate title and messages
	def loadVariables(self, messagesFile):
		f = open(messagesFile, 'r')
		variables = yaml.load(f)
		self.title = variables['title']
		self.messages = variables['messages']

	# Create a ordered dict from dict of messages 
	def createMessagesDict(self, messages):
		# Convert keys to secondes
		withSecondes = [ (self.timeToSecondes(k),v) for k,v in messages.items() ]

		# Order the keys
		ordered = sorted(withSecondes, key=lambda k: k[0])

		# If there is no 0 key create it, copied from the last message
		if ordered[0][0] != 0:
			ordered.insert(0, (0, ordered[-1][1]))

		# Shift each key to the right
		# the new key will be the time the message should stop appearing
		# make the last key to be midnight (3600*24)
		returnNextItem = lambda index, items: 3600*24 if index == len(items)-1 else items[index+1][0]
		shifted = [ 
			(returnNextItem(index, ordered), ordered[index][1])
			for index in range(0, len(ordered))
		]

		# Return an ordered dict
		return OrderedDict(shifted)

	# Get the title of the messages
	def getTitle(self):
		return self.title

	# Get hours, minutes, and the message of current time
	def getDateAndMessage(self):
		currentTime = datetime.now()
		return (
			currentTime.strftime("%H"),
			currentTime.strftime("%M"),
			self.getMessage(
				self.timeToSecondes(
					currentTime.strftime("%H:%M")
				)
			)
		)

	# Get the message for specific time (in secondes)
	def getMessage(self, forTime):
		if forTime >= 3600*24:
			forTime = 3600*24 - 1
		for t, m in self.sortedMessages.items():
			if forTime < t:
				return m

	# convert a time string to corresponding secondes
	def timeToSecondes(self, timeStr):
		hours = int(timeStr[0:2])
		minutes = int(timeStr[3:5])
		secondes = (hours * 3600) + (minutes * 60)
		return secondes
