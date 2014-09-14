from messages import Messages
m = Messages('messages.yaml')

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
	assert a.intervals == [[52,56], [57,57]]

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
