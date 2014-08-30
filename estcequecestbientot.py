"""
	Web app to display messages depending of the time of the day
	Using the flask framework
"""
from flask import Flask
from flask import render_template, redirect, url_for
from messages import Messages
import os.path

app = Flask(__name__)

# import the messages
messageFile = 'messages_custom.yaml' if os.path.isfile('messages_custom.yaml') else 'messages.yaml'

m = Messages(messageFile)

# We only respond to /
@app.route('/')
def estcequecestbientot():
	title = m.getTitle()
	(hours, minutes, message) = m.getDateAndMessage()
	return render_template('estcequecestbientot.html', title=title, message=message, hours=hours, minutes=minutes)

@app.route('/reload')
def reload():
	m.load()
	return redirect('/')

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