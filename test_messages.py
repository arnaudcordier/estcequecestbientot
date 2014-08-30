from messagesexemple import MyMessages
m = MyMessages()

midnight = 3600*24

def test_hasMidnight():
	assert m.sortedMessages[midnight]

def test_messageOfMidnight():
	message = m.getMessage(midnight)
	assert message == "Wait until tomorrow !"

def test_messageOfStart():
	message = m.getMessage(0)
	assert message == "Wait until tomorrow !"

def test_messageOnTime():
	noon = m.timeToSecondes('12:00')
	message = m.getMessage(noon)
	message_before = m.getMessage(noon-1)
	assert message == "Yes it is !"

def test_messageBeforeTime():
	noon = m.timeToSecondes('12:00')
	message = m.getMessage(noon-1)
	assert message == "No wait !"

