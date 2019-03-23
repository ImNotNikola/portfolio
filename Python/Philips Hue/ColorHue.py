#!/usr/bin/python

from phue import Bridge

import random
import time
import logging

logging.basicConfig()

ip = '10.0.0.6'

b = Bridge(ip)

#b.connect()

#b.get_api()

lights = b.get_light_objects('name')

left = lights["colorOutside 1"]
center = lights["colorOutside 2"]
right = lights["colorOutside 3"]
outsideLights = ['left', 'center', 'right']

#b.set_lights(['left' 'center', 'right'], 'on', True)

while True:
	left.xy = [random.random(), random.random()]
	time.sleep(.20)
	center.xy = [random.random(), random.random()]
	time.sleep(.20)
	right.xy = [random.random(), random.random()]
	time.sleep(.20)