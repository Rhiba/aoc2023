import numpy as np
import sys
from math import gcd

def main(in_string):
    tmp = in_string.split("\n\n")
    instructions = tmp[0].strip()
    map_strings = tmp[1].strip().splitlines()
    maps = dict()
    for map_str in map_strings:
        key = map_str.split(' ')[0]
        val_l = map_str.split(' ')[2][1:-1]
        val_r = map_str.split(' ')[3][:-1]
        maps[key] = (val_l, val_r)

    starts = [x for x in maps.keys() if x.endswith('A')]
    loop_lens = []
    for start in starts:
        current = start
        end = False
        counter = 0
        while not end:
            idx = counter % len(instructions)
            ins = instructions[idx]
            if ins == 'L':
                current = maps[current][0]
            elif ins == 'R':
                current = maps[current][1]

            # making assumptions about the loop here but its AoC
            # so its probably correct
            if current.endswith('Z'):
                end = True

            counter += 1

        loop_lens.append(counter)

    lcm = 1
    for i in loop_lens:
        lcm = lcm*i//gcd(lcm,i)

    print(lcm)





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
