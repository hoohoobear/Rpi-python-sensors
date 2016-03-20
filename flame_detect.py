
# flame_detect.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_FIR=17
GPIO_BEEP=9

GPIO.setup(GPIO_FIR,GPIO.IN)
GPIO.setup(GPIO_BEEP,GPIO.OUT)

print("ctrl+c to exit")

def beep(seconds):
	GPIO.output(GPIO_BEEP,GPIO.LOW)
	time.sleep(seconds)
	GPIO.output(GPIO_BEEP,GPIO.HIGH)
	time.sleep(seconds)

GPIO.output(GPIO_BEEP,GPIO.HIGH)

try:
	print("waiting for Fir to settle...")
	for i in range(1,101):
		if GPIO.input(GPIO_FIR)==0:
			print("flame detected")
			beep(0.6)
		else:
			print("ready!")
			GPIO.output(GPIO_BEEP,GPIO.HIGH)
		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
GPIO.cleanup()
