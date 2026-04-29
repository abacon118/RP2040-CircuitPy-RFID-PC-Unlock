# RP2040 CircuitPy RFID/NFC PC Unlock

This allows you to unlock your computer with an NFC or RFID tag.  Programmed using Circuit Python on a RP2040 Zero board from AliExpress, it conencts to a RC522 RFID Reader.  This uses the Adafruit_hid.keyboard Circuit Python library to input the password as text to the computer.

Copy the CircuitPython_Device folder to your RP2040 Zero.  All needed libaries are included there.  Boot.Py prevents your RP2040 Zero from showing up as a USB Flash Drive in File Explorer.

V2 changes the pin number to be semi-encrypted.  The pin number is stored on the RP2040 in a file that is encrypted with the Adafruit Hashlib library.  The hardware ID is the encryption key.

Parts:
* RP2040 Zero
	* https://www.aliexpress.us/item/3256805271899344.html?spm=a2g0o.order_list.order_list_main.39.6fe01802m0HRTG&gatewayAdapt=glo2usa
* RC522 RFID Reader
	* https://www.aliexpress.us/item/3256805162087677.html?spm=a2g0o.order_list.order_list_main.67.6fe01802m0HRTG&gatewayAdapt=glo2usa
* Computer with Thonny
	* Get Started with MicroPython on Raspberry Pi Pico is a good guide to start with
		* https://magpi.raspberrypi.com/books/micropython-pico
* Piezo Buzzer
* 10k Ohm Resistor (optional to limit volume of buzzer)
* Common Cathode RGB LED (definently can be switches to Common Anthode LED) - Optional, not pictured
* 3x 200 Ohm Resistors for RGB LED

Steps to set up:
1. Connect RC522 RFID Reader to your RP2040 Zero.
2. Install Circuit Python on your device.  This was tested with Circuit Python 8.1.0 on a Waveshare RP2040 Zero.
3. Copy the following to your Circuit Python device.
    boot.py
    code.py
    mrfc522.py
    pin_manager.py
    lib
5. Run the Code
6. During the first run you will be asked to enter your computer pin number.  This can be reset by deleting pin.bin.
7. Scan your NFC Cards
8. Put the UUID for each card on one line and save in keys.txt.
9. Close Thonny and restart your Circuit Python device. Your card should now unlock your computer.

# Schematic
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Schematic/RFID_PC_RP2040Zero.jpg">
 <source media="(prefers-color-scheme: light)" srcset="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Schematic/RFID_PC_RP2040Zero.jpg">
 <img alt="Schematic" src="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Schematic/RFID_PC_RP2040Zero.jpg">
</picture>

# Finished Project
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Photos/PXL_20230624_032824612.jpg">
 <source media="(prefers-color-scheme: light)" srcset="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Photos/PXL_20230624_032824612.jpg">
 <img alt="Completed Board" src="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Photos/PXL_20230624_032824612.jpg">
</picture>
