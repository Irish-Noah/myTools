import os
import re
from pathlib import Path

DIR_PATH = './'

def create_json(file):
    fp = open(file, 'r')
    content = fp.read()

    if not len(content):
        return ['Not much is known about this box']

    content = content.strip().replace('\\n','').replace('<>', '')
    devices = content.split('DEVICE')
    devices = devices[1:]

    filtered_devices = []
    for device in devices: 
        # Device ID is always first, grab first non-space sequence
        device_match = re.search(r':\s*(\S+)', device)
        device_id = device_match.group(1) if device_match else 'n/a'

        # Search for VIN and FIRMWARE anywhere (case-insensitive)
        vin_match = re.search(r'VIN:\s*(\S+)', device, re.IGNORECASE)
        firmware_match = re.search(r'FIRMWARE:\s*(\S+)', device, re.IGNORECASE)

        data = {
            "device_id": device_id,
            "vin": vin_match.group(1) if vin_match else 'n/a',
            "firmware": firmware_match.group(1) if firmware_match else 'n/a'
        }

        filtered_devices.append(data)
    
    #print(devices[1:])
    fp.close()
    return filtered_devices


def main(): 
    boxes = {}

    for subdir, dirs, files in os.walk(DIR_PATH):
        box = str(subdir).replace('./','')

        # if there are no devices reported on the box
        if not files:
            boxes[box] = {'Error': ['No devices found --> Possible that box offline']}

        for filename in files: 
            # files on server don't have extensions, filter out files that have them
            if '.' in filename: 
                continue

            filepath = os.path.join(subdir, filename)
            if box in boxes.keys():
                boxes[box][filename] = create_json(filepath)
            else: 
                boxes[box] = {filename : create_json(filepath)}
            

    for box in boxes.items():
        print(box)
        print()


if __name__ == "__main__":
    main()