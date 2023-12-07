
import sys

def main(in_string):
    tmp = in_string.splitlines()
    time = int(tmp[0].split(':')[1].strip().replace(" ",""))
    distance = int(tmp[1].split(':')[1].strip().replace(" ",""))

    beats = 0
    for i in range(time):
        if (time-i)*i > distance:
            beats += 1

    print(beats)





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
