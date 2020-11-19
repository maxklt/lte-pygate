import settings
from network import LTE
import time
import machine
from machine import RTC
import pycom


# define colors
off = 0x000000
white = 0xffffff
red = 0x8a0000
green = 0x007f00
orange = 0xff7300
blue = 0x035afc
yellow = 0xffff00
purple = 0xf700ff


print('\nStarting LoRaWAN concentrator')


# stop heartbeat
pycom.heartbeat(False)


# pygate callback handler
def machine_cb(arg):
    evt = machine.events()
    print("-------------------------")
    print("MACHINE EVENT: {}".format(evt))
    print("-------------------------")
    if (evt & machine.PYGATE_START_EVT):
        pycom.rgbled(green)
    elif (evt & machine.PYGATE_ERROR_EVT):
        pycom.rgbled(red)
    elif (evt & machine.PYGATE_STOP_EVT):
        pycom.rgbled(off)


# lte callback handler
def lte_connection_lost_handler(arg):
    print("!!! CONNECTION LOST !!!")
    led_control(red, 5)
    machine.pygate_deinit()
    # machine.pygate_reset()
    machine.reset()


# function to light the Led
def led_control(color, duration):
    pycom.rgbled(color)
    time.sleep(duration)
    pycom.rgbled(off)


# set pygate event callback
machine.callback(trigger=(machine.PYGATE_START_EVT |
                          machine.PYGATE_STOP_EVT | machine.PYGATE_ERROR_EVT), handler=machine_cb)


# setup LTE
lte = LTE()


# set lte callback
lte.lte_callback(LTE.EVENT_COVERAGE_LOSS, lte_connection_lost_handler)


# check lte connection or establish lte connection
if not lte.isconnected():
    print("Resetting LTE modem ... ", end='')
    lte.send_at_cmd('AT^RESET')
    print("OK")
    time.sleep(1)

    if not lte.isattached():
        print("Attaching to LTE network ", end='')
        lte.attach(band=settings.LTE_BAND, apn=settings.LTE_APN)
        arc = 0
        while(True):
            if arc >= 120:
                machine.reset()
            if lte.isattached():
                print("OK", end="\n\n")
                print("----------------------------")
                signal_strenght = lte.send_at_cmd("AT+CSQ")
                signal_strenght = float(
                    ''.join([n for n in signal_strenght if n.isdigit()])) / 100
                if 0 <= signal_strenght <= 9:
                    led_control(red, 1)
                if 10 <= signal_strenght <= 14:
                    led_control(orange, 1)
                if 15 <= signal_strenght <= 19:
                    led_control(yellow, 1)
                if 20 <= signal_strenght <= 30:
                    led_control(green, 1)
                print("Signal strenght: {}".format(signal_strenght))
                print("- - - - - - - - - - - - - -")
                print("IMEI: {}".format(lte.imei()))
                print("ICCID: {}".format(lte.iccid()))
                print("----------------------------", end="\n\n")
                break
            print('.', end='')
            arc += 1
            time.sleep(.5)

    if not lte.isconnected():
        print("Connecting on LTE network ", end='')
        lte.connect()
        crc = 0
        while(True):
            if crc >= 60:
                machine.reset()
            if lte.isconnected():
                led_control(green, .5)
                print(" OK")
                break
            print('.', end='')
            crc += 1
            time.sleep(.5)


# sync RTC
print('Syncing RTC via ntp...', end='')
rtc = RTC()
rtc.ntp_sync(server=settings.TIME_SERVER)
while not rtc.synced():
    print('.', end='')
    time.sleep(.5)
print(" OK\n")


# open config
fp = open('/flash/config.json', 'r')
buf = fp.read()


print("------ start paygate ------", end="\n\n")


machine.pygate_init(buf)


# disable degub messages
# machine.pygate_debug_level(1)
