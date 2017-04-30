print "this a test running, make sure to GPIO.cleanup() afterwards"

sudo python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
pwm = GPIO.PWM(18, 1000)
pwm.start(50)