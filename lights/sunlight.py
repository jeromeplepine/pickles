# This is the module containing the grow light constants, functions, etc.

def sunlight_init():
    from raspledstrip.ledstrip import *
    from datetime import datetime
    from pytz import timezone
    import time


    ##CONSTANTS DECLARATION
     ## Timing related
    time_open = 15		#Lower time limit to lightup the strip
    minute = 60			# 60 seconds in a minute
    dusk_period = 25		# Assumption, in minutes
    dawn_period = 25		# According to some website, 25min til its black in FL
    dusk_progress = 0
    dawn_progress = 0
    

     ## Brightness settings - not used
    # max_brightness = 255
   # min_brightness = 25
    # brightness = 0

     ## RGB mix parameters - to scale with plant needs
    R_max = 255		# From massroots.com leds color guide,
    G_max = 255		# Blueish lights helps plants grow short
    B_max = 218		# with robust leaves. These set the maximum
			# brightness for each colors
    R_increment = (float(R_max) / dusk_period)
    G_increment = (float(G_max) / dusk_period)
    B_increment = (float(B_max) / dusk_period)

    ##INIT
    led = LEDStrip(32)	#LEDstrip control handle
    R = G = B = 0
    ## Make sure the strip is completely closed
    led.fillRGB(R, G, B)
    led.update()


def dusk():      ############ figure how ill actualise lighting increments  
	time = datetime.now(timezone('US/Eastern'))

	dusk_start = time = next_increment
        dusk_ends = time + dusk_period	# Add wrap around 60 minutes
        dusk_progress += 1

   if next_increment == time.minute:
	dusk_progress += 1
        R = round(dusk_progress * R_increment)
        G = round(dusk_progress * G_increment)
        B = round(dusk_progress * B_increment)
        led.fillRGB(R, G, B)
	next_increment = dusk_start + dusk_progress
        else :
    	    # brightness -= 1		#allows light intensity to decrease
	    #direction = 0
	    brightness = 0
	    R = G = B = 0
	    led.fillRGB(R, G, B)
    
        led.update()
        print R
        time.sleep()
    
