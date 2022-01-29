# -*- cpding: utf-8 -*-
import time
import sys
import os
import netifaces

def ip_addr_loop():
	for _ in range(10):	
		time.sleep(1)
		interface_data = netifaces.ifaddresses('eth0')
		try:
			ip_v4 = interface_data[netifaces.AF_INET][0]['addr']
		except Exception as e:
			os.system('/home/pi/e-DrumMania/aquestalkpi/AquesTalkPi -s 100 ' + '"メンテナンスモードで起動中。ランケーブルを接続してください。"' + '| aplay')
		else:
			os.system('/home/pi/e-DrumMania/aquestalkpi/AquesTalkPi -s 100 ' + '"IPアドレスは"' + '| aplay')
			os.system('/home/pi/e-DrumMania/aquestalkpi/AquesTalkPi -s 50 ' + '"'+ ip_v4 + '"' + '| aplay')
