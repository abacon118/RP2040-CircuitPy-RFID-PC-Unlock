import time
import board
import digitalio
import simpleio
import busio
import mfrc522
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import array as arr

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

sck = board.GP6
mosi = board.GP7
miso = board.GP4
spi = busio.SPI(sck, MOSI=mosi, MISO=miso)

cs = digitalio.DigitalInOut(board.GP5) #SDA
rst = digitalio.DigitalInOut(board.GP8)
rfid = mfrc522.MFRC522(spi, cs, rst)
rfid.set_antenna_gain(0x07 << 4)

keys = [ 'aaaaaaaa', 'bbbbbbb' ] #add your card(s) here.

print("\n***** Scan your RFid tag/card *****\n")

prev_data = ""
prev_time = 0
timeout = 1

buzzer = digitalio.DigitalInOut(board.GP14)
buzzer.direction = digitalio.Direction.OUTPUT

red = digitalio.DigitalInOut(board.GP29)
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP28)
green.direction = digitalio.Direction.OUTPUT
blue = digitalio.DigitalInOut(board.GP27)
blue.direction = digitalio.Direction.OUTPUT
red.value = True
green.value = True
blue.value = True



while True:
    (status, tag_type) = rfid.request(rfid.REQALL)

    if status == rfid.OK:
        (status, raw_uid) = rfid.anticoll()
        blue.value = False
        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("Card detected! UID: {}".format(rfid_data))
            blue.value = True
            for x in keys:
                if x == "{}".format(rfid_data):
                    print("correct card")
                    green.value = False
                    buzzer.value = True
                    keyboard.send(Keycode.ENTER)
                    time.sleep(0.2)
                    buzzer.value = False
                    layout.write('Your Password')  #Insert your password here
                    keyboard.release_all()
                    green.value = True
                    time.sleep(2)
                else:
                    red.value = False
                    print("incorrect card")
                    time.sleep(0.2)
                    red.value = True
                prev_time = time.monotonic()
                
        

    else:
        if time.monotonic() - prev_time > timeout:
            prev_data = ""
