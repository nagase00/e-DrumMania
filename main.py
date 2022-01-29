# -*- cpding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
import pygame
from pygame.locals import*

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pygame.mixer.init(44100, -16, 1, 512)
pygame.mixer.set_num_channels(16)
kick=pygame.mixer.Sound("drum_sample/Drum_kick.wav")
kick_flg=0

while True:
    try:
        if GPIO.input(5) == 1:
            if kick_flg == 0:
                kick.stop()
                kick.play()
            kick_flg=1
        else:
            kick_flg=0
        time.sleep(0.02)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
