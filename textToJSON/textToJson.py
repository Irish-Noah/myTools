import os
from pathlib import Path

DIR_PATH = './'

def create_json(file):
    fp = open(file, 'r')
    content = fp.read()
    content = content.strip().replace('\\n','').replace('<>', '')
    devices = content.split('DEVICE')
    #print(devices[1:])
    fp.close()
    return devices


def main(): 
    boxes = {}

    for subdir, dirs, files in os.walk(DIR_PATH):
        for filename in files: 
            if '.' in filename: 
                continue

            filepath = os.path.join(subdir, filename)
            box = str(subdir).replace('./','')
            if box in boxes.keys():
                boxes[box][filename] = create_json(filepath)
            else: 
                boxes[box] = {filename : create_json(filepath)}
            
    print(boxes)


if __name__ == "__main__":
    main()