# -*- cpding: utf-8 -*-
from gpiozero import MCP3008
import time
import csv

def analog_read(channel):
	pot = MCP3008(channel)
	volt = pot.value * Vref
	return volt

Vref = 3.33
NCHANEL = 1

if __name__== "__main__":
	try:
		while True:
			#for i in range(NCHANEL):
			#	print(analog_read(i))
			print(analog_read(0))
			time.sleep(1)
	except KeyboardInterrupt:
		pass
