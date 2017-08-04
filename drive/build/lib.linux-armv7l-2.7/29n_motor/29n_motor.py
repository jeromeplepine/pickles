#!/usr/bin/python

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepPinForward=23 #GPIO 23
StepPinBackward=24 #GPIO 24
PwmPin=18
sleeptime=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(PwmPin, GPIO.OUT)
pwm = GPIO.PWM(PwmPin, 500)
pwm.start(0)

def forward(x):
	pwm.start(0)
	time.sleep(2)
	GPIO.output(StepPinForward, GPIO.HIGH)
	print "forwarding running  motor "
	GPIO.output(StepPinBackward, GPIO.LOW)
	pwm.ChangeDutyCycle(x)

def reverse(x):
	pwm.start(0)
	time.sleep(2)
	GPIO.output(StepPinBackward, GPIO.HIGH)
	print "backwarding running motor"
	GPIO.output(StepPinForward, GPIO.LOW)
	pwm.ChangeDutyCycle(x)

def stop():
	pwm.stop
	print "pwm stopped"

print "pwm zero, waiting command: forward(%), reverse(%), stop()"
