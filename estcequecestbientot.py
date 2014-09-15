"""
	Web app to display messages depending of the time of the day
	Using the flask framework
"""
from flask import Flask
from flask import render_template, redirect, url_for
from messageApp.messageApp import MessageApp

app = Flask(__name__)

ma = MessageApp();

# show current messages
@app.route('/')
def estcequecestbientot():
	messages = ma.getMessages()
	return render_template('estcequecestbientot.html', messages=messages)

# load a message
@app.route('/load/<name>')
def load(name):
	names = name.split(',')
	ma.loadMessage(names)
	return redirect('/')

# unload
@app.route('/unload/<name>')
def unload(name):
	names = name.split(',')
	ma.unloadMessage(names)
	return redirect('/')

# reload current messages from file
@app.route('/reload')
def reload():
	ma.reload()
	return redirect('/')

# list available messages
@app.route('/list')
def list():
	notloadedList, loadedList = ma.listMessages()
	loadedList    = [(url_for('unload', name=name), name) for name in loadedList]
	notloadedList = [(url_for('load',   name=name), name) for name in notloadedList]
	return render_template('list.html', loaded=loadedList, notloaded=notloadedList)

# run !
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9000, debug=True)

'''
Purpose:
display a message depending of the time of the day
could display a message depending of the day, date, day of week, year…

Similar projects:
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

TODO:
 - reverse message intervals, in order to write exceptional intervals at the bottom of the file (maybe not a good idea)
 - file system handling should only be in messageApp class
 - find a way to configure app at loading time

Similar web sites:
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
