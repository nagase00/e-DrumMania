# -*- cpding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
import pygame
from pygame.locals import*

# local modules
import maintenance
import Drum

# PIN
#SELECT_PIN = 21
KICK_PIN = 5

def setup():
	drums = []

	kick=pygame.mixer.Sound("/home/pi/e-DrumMania/drum_sample/Drum_kick.wav")
	drums.append(Drum.Pedal(kick, KICK_PIN))

	hat=pygame.mixer.Sound("/home/pi/e-DrumMania/drum_sample/Drum_HatClose.wav")
	drums.append(Drum.Pad(hat, 0))

	snare=pygame.mixer.Sound("/home/pi/e-DrumMania/drum_sample/Drum_Snare.wav")
	drums.append(Drum.Pad(snare, 1))

	tom1=pygame.mixer.Sound("/home/pi/e-DrumMania/drum_sample/Drum_HighTom.wav")
	drums.append(Drum.Pad(tom1, 2))

	tom2=pygame.mixer.Sound("/home/pi/e-DrumMania/drum_sample/Drum_Floor.wav")
	drums.append(Drum.Pad(tom2, 3))

	clash=pygame.mixer.Sound("/home/pi/e-DrumMania/drum_sample/Drum_Clash.wav")
	drums.append(Drum.Pad(clash, 4))
	return drums

def main_loop():
	drums = setup()
	while True:
		for d in drums:
			d.play()
		time.sleep(0.001)

if __name__ == "__main__":
	#set up gpio
	GPIO.setmode(GPIO.BCM)
	#GPIO.setup(SELECT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #select(reset or entering maintenance mode)
	GPIO.setup(KICK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #kick
	
	#set up pygame.mixer
	pygame.mixer.init(44100, -16, 1, 512)
	pygame.mixer.set_num_channels(16)

	try:
		#if GPIO.input(SELECT_PIN):
		#	maintenance.ip_addr_loop()
		#else:
		main_loop()
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit()

