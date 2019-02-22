#!/usr/bin/env python3

from bottle import *
import sqlite3
import json
import random
import html2text
import re
from datetime import date

tableTra = ['Car', 'Walking', 'Bus']

@route('/')
def home():
	trip = getData()
	
	if trip[4]:
		addr = "Obiščite nas: " + trip[4]
	else:
		addr = "V bazi ni naslova na katerem se nahaja znamenitost"
	
	sl = {
	
	'header': trip[2], 'description': addr, 
	'place': trip[14], 'stars': random.randrange(4)+1 , 
	'start': [getRandomDate() for i in range(1,10)], 
	'duration': [str(i)+ ' days' for i in range(2,8)], 
	'numPeople': [str(i) + ' people' for i in range(2,6)],
	'transportTable': tableTra,
	'priceFrom': [str(i*100) for i in range(1,5)],
	'priceTo': [str(i*100) for i in range(5,10)],
	'transport': tableTra[random.randint(0,2)]
	}
	
	return template('card.html', sl)


def getRandomDate():
	start_dt = date.today().replace(day=1, month=1).toordinal()
	end_dt = date.today().toordinal()
	random_day = date.fromordinal(random.randint(start_dt, end_dt))
	return random_day
	
def getRandomDuration():
	var = random.randrange(6)+1
	


def getData():
	conn = sqlite3.connect('slovenia_db')
	c = conn.cursor()
	c.execute("SELECT * FROM attraction")
	result = c.fetchall()
	return result[random.randrange(len(result))]

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='/')

@route('/to')
def todo_list():
	return str(html2text.html2text(getData()[9]))
    
run(host='localhost', port=8080, debug=True)
