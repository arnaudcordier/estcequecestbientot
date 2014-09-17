# Test IntervalBit
from messageApp.intervalBit import IntervalBit

ib = IntervalBit('5-45,52-56,57', 6)

def test_IntervalBit_doesItFit_1():
	assert ib.doesItFit(6) == [5, 45]

def test_IntervalBit_doesItFit_2():
	assert ib.doesItFit(55) == [52,56]

def test_IntervalBit_doesItFit_3():
	assert ib.doesItFit(52) == [52,56]

def test_IntervalBit_doesItFit_4():
	assert ib.doesItFit(56) == [52,56]

def test_IntervalBit_doesItFit_exact():
	assert ib.doesItFit(57) == [57,57]

def test_IntervalBit_doesItFit_none():
	assert ib.doesItFit(4) == None

def test_IntervalBit_doesItFit_all():
	a = IntervalBit('5-45,52-56,57,*', 6)
	assert a.doesItFit(46) == ['*','*']

def test_IntervalBit_doesItFit_no_out_of_boundary():
	a = IntervalBit('52-56,57,89-95', 6)
	assert a._intervals == [[52,56], [57,57]]


# Test Interval
from messageApp.intervals import Interval
from datetime import datetime

interval= '* * 13-22 5-7 09-20,23 *'
messages = [('10:30', 'message1'), ('11:45', 'message2'), ('13:12', 'message3'), ('09:12', 'message4')]
i = Interval(interval, messages)

def test_Interval_doesItFit_1():
	assert i._doesItFit([2013, 12, 13, 5, 15, 12]) == [['*', '*'], ['*', '*'], [13, 22], [5, 7], [9, 20], ['*', '*']]

def test_Interval_doesItFit_2():
	assert i._doesItFit([2013, 12, 13, 5, 23, 53]) == [['*', '*'], ['*', '*'], [13, 22], [5, 7], [23, 23], ['*', '*']]

def test_Interval_doesItFit_not():
	assert i._doesItFit([2013, 12, 13, 5,  2, 18]) == None

def test_Interval_getMessage_1():
	assert i.getMessage(datetime(2013, 12, 13, 23, 53)) == 'message3'

def test_Interval_getMessage_2():
	assert i.getMessage(datetime(2013, 12, 13, 9, 12)) == 'message4'

def test_Interval_getMessage_not():
	assert i.getMessage(datetime(2013, 12, 13, 9, 11)) == None


# Test Messages
#TODO test empty if no default message
from messageApp.messages import Messages
from datetime import datetime
import yaml

def test_Messages_getMessage():
	f = open('messages/messages_object.yaml', 'r')
	y = yaml.load(f)
	m = Messages(y)
	estcequecestbientot = m.getMessage( datetime(2013, 12, 13, 23, 53) )
	print(estcequecestbientot)
	assert estcequecestbientot == ('montitre', 'message3')

# test MessageApp
#TODO test no loose of the order of the messages
#TODO test load / unload of unknown named Messages
from messageApp.messageApp import MessageApp
from datetime import datetime

m = MessageApp('messages', "messages_")

def test_MessageApp_loadMessages():
	m.loadMessage('object')
	_, l = m.listMessages()
	print(l)
	assert l == ['object']

def test_MessageApp_unloadMessage():
	m.unloadMessage('object')
	_, l = m.listMessages()
	print(l)
	assert l == []

# def test_listMessages() # allready done

def test_MessageApp_reload(): #TODO realy test reload of file !
	m.loadMessage('object')
	_, l1 = m.listMessages()
	m.reload()
	_, l2 = m.listMessages()
	assert l1 == l2

#def test_getMessages(): # too tricky

def test_MessageApp_getMessagesAtTime():
	m.loadMessage('object')
	estcequecestbientot = m.getMessagesAtTime(datetime(2013, 12, 13, 23, 53))
	print(estcequecestbientot)
	assert estcequecestbientot == [('montitre', 'message3')]

