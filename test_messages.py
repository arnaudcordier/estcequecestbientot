# Test IntervalBit
from messageApp.intervalBit import IntervalBit

ib = IntervalBit('5-45,52-56,57', 6)

def test_bitFit_interval1():
	assert ib.doesItFit(6) == [5, 45]

def test_bitFit_interval2():
	assert ib.doesItFit(55) == [52,56]

def test_bitFit_interval3():
	assert ib.doesItFit(52) == [52,56]

def test_bitFit_interval4():
	assert ib.doesItFit(56) == [52,56]

def test_bitFit_exact():
	assert ib.doesItFit(57) == [57,57]

def test_bitFit_none():
	assert ib.doesItFit(4) == None

def test_bitFit_all():
	a = IntervalBit('5-45,52-56,57,*', 6)
	assert a.doesItFit(46) == ['*','*']

def test_bitFit_eliminate_out_of_boundary():
	a = IntervalBit('52-56,57,89-95', 6)
	assert a._intervals == [[52,56], [57,57]]


# Test Interval
from messageApp.intervals import Interval
from datetime import datetime

interval= '* * 13-22 5-7 09-20,23 *'
messages = [('10:30', 'message1'), ('11:45', 'message2'), ('13:12', 'message3'), ('09:12', 'message4')]
i = Interval(interval, messages)

def test_interval_fit_1():
	assert i._doesItFit([2013, 12, 13, 5, 15, 12]) == [['*', '*'], ['*', '*'], [13, 22], [5, 7], [9, 20], ['*', '*']]

def test_interval_nofit():
	assert i._doesItFit([2013, 12, 13, 5,  2, 18]) == None

def test_interval_fit_2():
	assert i._doesItFit([2013, 12, 13, 5, 23, 53]) == [['*', '*'], ['*', '*'], [13, 22], [5, 7], [23, 23], ['*', '*']]

def test_interval_message_1():
	assert i.getMessage(datetime(2013, 12, 13, 23, 53)) == 'message3'

def test_interval_message_2():
	assert i.getMessage(datetime(2013, 12, 13, 9, 11)) == None

def test_interval_message_3():
	assert i.getMessage(datetime(2013, 12, 13, 9, 12)) == 'message4'


# Test Messages
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
from messageApp.messageApp import MessageApp
from datetime import datetime

m = MessageApp('messages', "messages_")

def test_loadMessages():
	m.loadMessage('object')
	_, l = m.listMessages()
	print(l)
	assert l == ['object']

def test_unloadMessage():
	m.unloadMessage('object')
	_, l = m.listMessages()
	print(l)
	assert l == []
	
# def test_listMessages() # allready done

def test_reload(): # does not realy test reload of file
	m.loadMessage('object')
	_, l1 = m.listMessages()
	m.reload()
	_, l2 = m.listMessages()
	assert l1 == l2

#def test_getMessages(): # too tricky

def test_getMessagesAtTime():
	m.loadMessage('object')
	estcequecestbientot = m.getMessagesAtTime(datetime(2013, 12, 13, 23, 53))
	print(estcequecestbientot)
	assert estcequecestbientot == [('montitre', 'message3')]


