
import sys

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

    end = False
    counter = 0
    current = 'AAA'
    while not end:
        idx = counter % len(instructions)
        ins = instructions[idx]
        if ins == 'L':
            current = maps[current][0]
        elif ins == 'R':
            current = maps[current][1]

        if current == 'ZZZ':
            end = True

        counter += 1

    print(counter)





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
