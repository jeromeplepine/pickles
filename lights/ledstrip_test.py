

from raspledstrip.ledstrip import *
from datetime import datetime
from pytz import timezone
import time


##CONSTANTS DECLARATION
time_open = 15		#Lower time limit to lightup the strip

max_brightness = 255
min_brightness = 25
brightness = 0

R_max = 255		#From massroots.com leds color guide,
G_max = 255		#Blueish lights helps plants grow short
B_max = 218		#with robust leaves
R_increment = (float(R_max) / max_brightness)
G_increment = (float(G_max) / max_brightness)
B_increment = (float(B_max) / max_brightness)

direction = 1		#1 means light increasing in intensity. not currently implemented

##INIT - place after constant decl
led = LEDStrip(32)	#LEDstrip control handle
R = G = B = 0


led.fillRGB(R, G, B)
led.update()

# This loop will increase or decrease the light to a desired level

while direction == 1 :
   # time = datetime.now(timezone('US/Eastern'))
   # if time.second > time_open
    if brightness < max_brightness :
        brightness += 1
	R = round(brightness * R_increment)
        G = round(brightness * G_increment)
        B = round(brightness * B_increment)
        led.fillRGB(R, G, B)
    else :
	# brightness -= 1		#allows light intensity to decrease
	#direction = 0
	brightness = 0
	R = G = B = 0
	led.fillRGB(R, G, B)
    
    led.update()
    print R
    time.sleep(0.1)
    
