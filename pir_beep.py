
# pir_beep.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_PIR=17
GPIO_BEEP=9

GPIO.setup(GPIO_PIR,GPIO.IN)
GPIO.setup(GPIO_BEEP,GPIO.OUT)

print("ctrl+c to exit")

def beep(seconds):
	while GPIO.input(GPIO_PIR):
		GPIO.output(GPIO_BEEP,GPIO.LOW)
		time.sleep(seconds)
		GPIO.output(GPIO_BEEP,GPIO.HIGH)
		time.sleep(seconds)

print("write high")
GPIO.output(GPIO_BEEP,GPIO.HIGH)
time.sleep(3)
print("write low")
beep(0.8)
GPIO.output(GPIO_BEEP,GPIO.LOW)
time.sleep(1)
GPIO.output(GPIO_BEEP,GPIO.HIGH)
time.sleep(5)

try:
	print("waiting for pir to settle...")
	for i in range(1,1001):
		if GPIO.input(GPIO_PIR)==1:
			print("Motion detected")
			beep(0.6)
		else:
			print("ready!")
			GPIO.output(GPIO_BEEP,GPIO.HIGH)
		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
GPIO.cleanup()
