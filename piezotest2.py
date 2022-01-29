# -*- coding:utf-8 -*-
import time
import spidev

Vref = 3.334  # 電圧をテスターで実測する

spi = spidev.SpiDev()

spi.open(0, 0)  # bus0,cs0
spi.max_speed_hz = 100000  # 100kHz 必ず指定する


def readAdc(channel):
	adc = spi.xfer2([1, (8 + channel) << 4, 200])
	data = ((adc[1] & 3) << 8) + adc[2]
	return data


def convertVolts(data, vref):
	volts = (data * vref) / float(1023)
	return volts

if __name__ == '__main__':
	try:
		while True:
			data = readAdc(channel=0)
			volts = convertVolts(data, Vref)
			if volts > 0.01:
				print("CH0 volts: {:.2f}".format(volts))
			time.sleep(0.01)
	except KeyboardInterrupt:
		spi.close()
