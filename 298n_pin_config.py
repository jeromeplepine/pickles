<p>import RPi.GPIO as GPIO
 
# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)
 
# set up the GPIO channels - one input and one output
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.OUT)
 
# input from GPIO7
input_value = GPIO.input(7)
 
# output to GPIO8
GPIO.output(8, True)</p>