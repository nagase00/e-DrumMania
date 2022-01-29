# -*- cpding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
import pygame
from pygame.locals import*

# local modules
import maintenance
import Drum

SELECT_PIN = 21
KICK_PIN = 5


def setup():
	drums = []

	kick=pygame.mixer.Sound("/home/pi/e-DrumMania/drum_sample/Drum_kick.wav")
	drums.append(Drum.Pedal(kick, KICK_PIN))


	return drums

def main_loop():
	drums = setup()
	while True:
		for d in drums
			d.play()
		time.sleep(0.02)

if __name__ == "__main__":
	#set up gpio
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SELECT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #select(reset or entering maintenance mode)
	GPIO.setup(KICK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #kick
	
	#set up pygame.mixer
	pygame.mixer.init(44100, -16, 1, 512)
	pygame.mixer.set_num_channels(16)

	try:
		if GPIO.input(SELECT_PIN):
			maintenance.ip_addr_loop()
		else:
			main_loop()
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit()

