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
Similar projects
 https://github.com/tontonDuPirox/estcequecestbientot (php)
 https://github.com/hughevans/isitcoffeetime.com (ruby)
 https://github.com/isitchristmas (js)
 https://github.com/ravinggenius/weekend (js)
 https://github.com/attaboy/isitteatimeyet (php)
 https://github.com/antoinefriteau/estcequecestlheureducafe (js)
 https://github.com/chregu/isitfullmoon (php)
 https://github.com/antoinefriteau/estcequecestlheuredalleraucinema.fr (php)
 https://github.com/noahd1/isitburgerwednesday.com (js)
 https://github.com/kd35a/isitthefuture (php)
 https://github.com/jingweno/isittheday.com (ruby)
 https://github.com/stilldavid/isittimetogohome.com (php)

purpose
 display a message depending of the time of the day
 could display a message depending of the day, date, day of week, year…
 
synopsis
 load array of messages and date
 get the current date/time
 find the message corresponding to the current time
 display the message
 
sites
 http://estcequecestbientot.fr/
  http://estcequecestbientotlheuredemanger.fr/
  http://estcequecestbientotlapero.fr/
  http://estcequecestbientotlhappyhours.fr/
  http://cestquandlessoldes.com/
  http://estcequecestbientotlesvacances.fr/
  http://estcequecestbientotleweekend.fr/
  http://estcequecestbientotlematch.fr/
  http://estcequecestbientotnoel.fr/
  http://estcequecestbientotlete.fr/
  http://estcequecestbientotlafriteduvendredi.fr/
 http://www.estcequonmetenprodaujourdhui.info/
 http://www.isittheweekendyet.com/
 http://isittheweekendyet.co.uk/
 http://isittimeforabeer.com/
 http://isittimeforbed.com/
 https://isitchristmas.com/
 http://isitteatimeyet.com/
 http://isitcoffeetime.com/
 http://isitfullmoon.com
'''