# RP2040 CircuitPy RFID PC Unlock

This allows you to unlock your computer with an NFC or RFID tag.  Programmed using Circuit Python on a RP2040 Zero board from AliExpress, it conencts to a RC522 RFID Reader.  This uses the Adafruit_hid.keyboard Circuit Python library to input the password as text to the computer.

Parts:
*RP2040 Zero
	https://www.aliexpress.us/item/3256805271899344.html?spm=a2g0o.order_list.order_list_main.39.6fe01802m0HRTG&gatewayAdapt=glo2usa
*RC522 RFID Reader
	https://www.aliexpress.us/item/3256805162087677.html?spm=a2g0o.order_list.order_list_main.67.6fe01802m0HRTG&gatewayAdapt=glo2usa
*Computer with Thonny
*Piezo Buzzer
*10k Ohm Resistor (optional to limit volume of buzzer)
*Common Cathode RGB LED (definently can be switches to Common Anthode LED) - Optional, not pictured
*3x 200 Ohm Resistors for RGB LED


<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Schematic/RFID_PC_RP2040Zero.jpg">
 <source media="(prefers-color-scheme: light)" srcset="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Schematic/RFID_PC_RP2040Zero.jpg">
 <img alt="Schematic" src="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Schematic/RFID_PC_RP2040Zero.jpg">
</picture>

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Photos/PXL_20230624_032824612.jpg">
 <source media="(prefers-color-scheme: light)" srcset="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Photos/PXL_20230624_032824612.jpg">
 <img alt="Completed Board" src="https://github.com/abacon118/RP2040-CircuitPy-RFID-PC-Unlock/blob/main/Photos/PXL_20230624_032824612.jpg">
</picture>
