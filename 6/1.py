
import sys
import numpy as np

def main(in_string):
    tmp = in_string.splitlines()
    times = [int(x) for x in tmp[0].split(':')[1].strip().split(' ') if x]
    distances = [int(x) for x in tmp[1].split(':')[1].strip().split(' ') if x]

    ways_of_beating = []
    for race in range(len(times)):
        beats = 0
        for i in range(times[race]):
            if (times[race]-i)*i > distances[race]:
                beats += 1
        ways_of_beating.append(beats)

    print(np.prod(ways_of_beating))





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
