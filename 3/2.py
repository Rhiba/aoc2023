
import sys

def main(in_string):
    grid = in_string.splitlines()
    loc_to_number = dict()
    for y,line in enumerate(grid):
        number = ''
        locations = []
        for x,symbol in enumerate(line):
            if symbol.isdigit():
                number += symbol
                locations.append((x,y))
            if not symbol.isdigit() or x == len(line)-1:
                if number:
                    for loc in locations:
                        loc_to_number[str(loc)] = int(number)
                    number = ''
                    locations = []


    gear_ratios = []
    for y,line in enumerate(grid):
        for x, symbol in enumerate(line):
            if symbol == '*':
                adjacent_parts = set()
                for i in range(-1,2):
                    for j in range(-1,2):
                        if x+i >= 0 and x+i < len(grid[0]) and y+j >= 0 and y+j < len(grid) and not (i == 0 and j == 0):
                            loc = (x+i,y+j)
                            if str(loc) in loc_to_number:
                                adjacent_parts.add(loc_to_number[str(loc)])

                if len(adjacent_parts) == 2: 
                    adjacent_parts = list(adjacent_parts)
                    gear_ratio = adjacent_parts[0]*adjacent_parts[1]
                    gear_ratios.append(gear_ratio)

    print(sum(gear_ratios))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
