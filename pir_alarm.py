# pir_alarm.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_PIR=17
GPIO_BEEP=9

GPIO.setup(GPIO_PIR,GPIO.IN)
GPIO.setup(GPIO_BEEP,GPIO.OUT)

print("ctrl+c to exit")

def beep(seconds):
	GPIO.output(GPIO_BEEP,GPIO.LOW)
	time.sleep(seconds)
	GPIO.output(GPIO_BEEP,GPIO.HIGH)

def beepAction(secs,sleepsecs,times):
	for t in range(times):
		time.sleep(sleepsecs)
		beep(secs)

Current_State=0
Previous_State=0
GPIO.output(GPIO_BEEP,GPIO.HIGH)

try:
	print("waiting for pir to settle...")
	while GPIO.input(GPIO_PIR)==1:
		current_State=0
	print("ready!")
	beepAction(0.2,0.4,3)

	while True:
		Current_State=GPIO.input(GPIO_PIR)

		if Current_State==1 and Previous_State==0:
			print("Motion detected")
			Previous_State=1
			beep(0.8)
		elif Current_State==0 and Previous_State==1:
			print("ready!")
			Previous_State=0
		time.sleep(0.01)
except KeyboardInterrupt:
	print("Quit")
GPIO.cleanup()
