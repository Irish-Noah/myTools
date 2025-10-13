from pathlib import Path

DIR_PATH = './'

def create_json(file, report):
    fp = open(file, 'r')
    for line in fp:
        print(line)
        line = line.strip().replace('\\n','').replace('<>', '').replace(':', '')
        devices = line.split("DEVICE")
        print(devices)
    fp.close()


def main(): 
    report = []
    for file in Path(DIR_PATH).rglob('*.txt'):
        create_json(file, report)
        break


if __name__ == "__main__":
    main()