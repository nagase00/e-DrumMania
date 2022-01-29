# -*- cpding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import RPi.GPIO as GPIO

class Drum(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self, sound):
		self.sound = sound

	@abstractmethod
	def play(self):
		pass

class Pedal(Drum):
	def __init__(self, sound, pin):
		super().__init__(sound=sound)
		self.pin = pin
		self.kick_flg = False

	def play(self):
		if GPIO.input(self.pin) == 1:
			if self.kick_flg == False:
				self.sound.stop()
				self.sound.play()
			self.kick_flg=True
		else:
			self.kick_flg=False

#class Pad(Drum)
#	def __init__(self, sound, channel):
