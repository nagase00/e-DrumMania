# e-DrumMania

## raspi setting

### bootconfig

sudo vim /boot/config.txt
- GPIO03 power on / off switch
```
dtoverlay=gpio-shutdown,debounce=1000
```
- SPI
```
dtparam=spi=on
```
and reboot.

### include main.py in rc.local

sudo vim /etc/rc.local
```
/usr/bin/python3 /home/pi/e-DrumMania/main.py

exit 0
```
