#!/usr/bin/python

from phue import Bridge

import random
import time
import logging
import itertools

logging.basicConfig()

green = [0.409, 0.518]
red = [0.675, 0.322]
christmas = [green, red]

toggle = itertools.cycle(christmas).next

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
	for light in outsideLights
		light.xy = toggle()
		time.sleep(.20)

#while True:
#	left.xy = random.choice(christmas)
#	time.sleep(.20)
#	center.xy = random.choice(christmas)
#	time.sleep(.20)
#	right.xy = random.choice(christmas)
#	time.sleep(.20)