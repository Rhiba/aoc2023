
import sys

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def main(in_string):
    grid = [list(x) for x in in_string.splitlines()]

    new_grid = []
    for idy, row in enumerate(grid):
        new_row = []
        for idx, entry in enumerate(row):
            if entry == '.' or entry == '#':
                new_row.append(entry)
            else:
                # can we move it up?
                new_y = idy
                for y in range(idy-1,-1,-1):
                    if not new_grid[y][idx] == '.':
                        new_y = y+1
                        break
                    elif new_grid[y][idx] == '.' and y == 0:
                        new_y = 0
                        break
                if new_y == idy:
                    new_row.append('O')
                else:
                    new_grid[new_y][idx] = 'O'
                    new_row.append('.')
        new_grid.append(new_row)

    load = 0
    for idx, row in enumerate(new_grid):
        score = len(new_grid)-idx
        count = row.count('O')
        load += (score * count)

    print(load)





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
