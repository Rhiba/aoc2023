
import sys

def main(in_string):
    grid = in_string.splitlines()
    part_numbers = []
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
                        is_part = check_surrounds(loc[0],loc[1],grid)
                        if is_part:
                            part_numbers.append(int(number))
                            break
                    number = ''
                    locations = []

    print(sum(part_numbers))

def check_surrounds(x,y,grid):
    for i in range(-1,2):
        for j in range(-1,2):
            if x+i >= 0 and x+i < len(grid[0]) and y+j >= 0 and y+j < len(grid) and not (i == 0 and j == 0):
                if not grid[y+j][x+i].isdigit() and not grid[y+j][x+i] == '.':
                    return True

    return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
