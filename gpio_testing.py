

import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
print "BCM"
print "this a test running, make sure to GPIO.cleanup() afterwards"

def config_out(x):
	GPIO.setup(x, GPIO.OUT)


def output_high(x):
	GPIO.output(x, GPIO.HIGH)
	print"HIgh output on selected BCM pin"

def output_low(x):
	GPIO.output(x, GPIO.LOW)
	print"HIgh output on selected BCM pin"


def clean():
	GPIO.cleanup()
	print"Floor is clean"
