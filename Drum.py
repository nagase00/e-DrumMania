# -*- cpding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import RPi.GPIO as GPIO
import spidev

class Drum(metaclass = ABCMeta):
	@abstractmethod
	def __init__(self, sound):
		self.sound = sound
		self.flg = False
		self.division_cnt = 0

	@abstractmethod
	def play(self):
		pass

class Pedal(Drum):
	def __init__(self, sound, pin):
		super().__init__(sound = sound)
		self.pin = pin

	def play(self):
		if self.division_cnt < 200:
			self.division_cnt = 0
			if GPIO.input(self.pin) == 1:
				if self.flg == False:
					self.sound.stop()
					self.sound.play()
				self.flg = True
			else:
				self.flg = False
		else:
			self.division_cnt += 1

class Pad(Drum):
	def __init__(self, sound, channel):
		super().__init__(sound = sound)
		self.channel = channel
		#spi
		self.spi = spidev.SpiDev()
		self.spi.open(0, 0)  # bus0,cs0
		self.spi.max_speed_hz = 100000  # 100kHz 必ず指定する

	def __del__(self):
		self.spi.close()

	def read_adc(self):
		adc = self.spi.xfer2([1, (8 + self.channel) << 4, 200])
		data = ((adc[1] & 3) << 8) + adc[2]
		return data
	
	def convert_volts(self, data):
		vref = 3.334  # 電圧をテスターで実測する
		volts = (data * vref) / float(1023)
		return volts

	def get_velocity(self, volts):
		vel = 0
		if volts > 1:
			vel = 1
		#elif volts < :
		#	vel = 0.2
		#elif volts < :
		#	vel = 0.4
		#elif volts < :
		#	vel = 0.6
		#elif volts < :
		#	vel = 0.8
		#else
		#	vel = 1.0
		return vel

	def play(self):
		if self.flg == True:
			if self.division_cnt < 100:
				self.division_cnt += 1
			else:
				self.flg = False
				self.division_cnt = 0
		else:
			data = self.read_adc()
			volts = self.convert_volts(data)
			velocity = self.get_velocity(volts)
			if velocity > 0:
				self.sound.stop()
				self.sound.set_volume(velocity)
				self.sound.play()
				self.flg = True
				print(self.channel)
	
