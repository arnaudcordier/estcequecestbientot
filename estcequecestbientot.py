"""
	Web app to display messages depending of the time of the day
	Using the flask framework
"""
from flask import Flask
from flask import render_template
import os.path

app = Flask(__name__)

# import the messages
customMessageFile = 'messagescustom.py'
if os.path.isfile(customMessageFile):
	from messagescustom import MyMessages
else:
	from messagesexemple import MyMessages

m = MyMessages()

# We only respond to /
@app.route('/')
def estcequecestbientot():
	title = m.getTitle()
	(hours, minutes, message) = m.getDateAndMessage()
	return render_template('estcequecestbientot.html', title=title, message=message, hours=hours, minutes=minutes)

# run !
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9000, debug=True)


'''
Similar project (PHP)
https://github.com/tontonDuPirox/estcequecestbientot

purpose
 display a message depending of the time of the day
 could display a message depending of the day, date, day of week, year…
 
synopsis
 load array of messages and date
 get the current date/time
 find the message corresponding to the current time
 display the message
'''