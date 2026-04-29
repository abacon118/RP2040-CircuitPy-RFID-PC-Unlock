#RFID PC Unlock V2
#Andrew Bowman 2026
#Assistance from Microsoft Copilot was used
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
from pin_manager import pin_exists, store_pin, load_pin, ask_for_pin, load_keys

keys = load_keys()

if not pin_exists():
    print("No PIN found. Setting up a new PIN.")
    new_pin = ask_for_pin()
    store_pin(new_pin)
    print("PIN stored.")

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


#1 = Key card on chair, 2 = HRL fob, 3 = SmarTrip

print("\n***** Scan your RFid tag/card *****\n")

prev_data = ""
prev_time = 0
timeout = 0.5


buzzer = digitalio.DigitalInOut(board.GP14)
buzzer.direction = digitalio.Direction.OUTPUT

red = digitalio.DigitalInOut(board.GP3)
red.direction = digitalio.Direction.OUTPUT

green = digitalio.DigitalInOut(board.GP1)
green.direction = digitalio.Direction.OUTPUT

blue = digitalio.DigitalInOut(board.GP2)
blue.direction = digitalio.Direction.OUTPUT
red.value = False
green.value = False
blue.value = False



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
                    #keyboard.send(Keycode.ENTER)
                   # time.sleep(0.2)
                    print("correct card")
                    green.value = True
                    buzzer.value = True
                    keyboard.send(Keycode.ENTER)
                    time.sleep(0.2)
                    buzzer.value = False
                    layout.write(load_pin())
                    keyboard.release_all()
                    green.value = False
                    
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


