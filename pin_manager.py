#RFID PC Unlock V2 - Pin Number Manager
#Andrew Bowman 2026
#Assistance from Microsoft Copilot was used
import os
import adafruit_hashlib as hashlib

# Replace this with your real hardware ID getter
HW_ID = b"\x01\x23\x45\x67\x89\xAB\xCD\xEF"

PIN_FILE = "/pin.bin"

def derive_key(hw_id):
    return hashlib.sha256(hw_id).digest()

def xor_bytes(data, key):
    return bytes([d ^ key[i % len(key)] for i, d in enumerate(data)])

def store_pin(pin):
    key = derive_key(HW_ID)
    wrapped = xor_bytes(pin.encode(), key)
    with open(PIN_FILE, "wb") as f:
        f.write(wrapped)

def load_pin():
    key = derive_key(HW_ID)
    with open(PIN_FILE, "rb") as f:
        wrapped = f.read()
    return xor_bytes(wrapped, key).decode()

def pin_exists():
    try:
        os.stat(PIN_FILE)
        return True
    except OSError:
        return False
    
def ask_for_pin():
    while True:
        pin = input("Enter a 4–8 digit PIN: ").strip()
        if pin.isdigit() and 4 <= len(pin) <= 8:
            return pin
        print("Invalid PIN. Must be 4–8 digits.")
        
def load_keys():
    keys = []
    key_file = "keys.txt"
    with open(key_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                keys.append(line)
    return keys