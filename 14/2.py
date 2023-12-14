
import sys

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def rotated(array):
    list_of_tuples = zip(*array[::-1])
    return [list(elem) for elem in list_of_tuples]

def spin_cycle(grid):
    new_grid = grid.copy()
    for compass in range(4):
        for idy, row in enumerate(new_grid):
            for idx, entry in enumerate(row):
                if entry == 'O':
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
                        new_grid[idy][idx] = 'O'
                    else:
                        new_grid[new_y][idx] = 'O'
                        new_grid[idy][idx] = '.'
        new_grid = list(rotated(new_grid))

    return new_grid

def calc_load(grid):
    load = 0
    for idx, row in enumerate(grid):
        score = len(grid)-idx
        count = row.count('O')
        load += (score * count)
    return load


def main(in_string):
    grid = [list(x) for x in in_string.splitlines()]

    loads = []
    for i in range(1000):
        grid = spin_cycle(grid)
        load = calc_load(grid)
        loads.append(load)

    substr_len = 2
    found = None
    substr = None
    cycle_start = None
    cycle_end = None
    while substr_len <= len(loads)/2:
        for start_idx in range(len(loads)):
            if start_idx + substr_len + substr_len >= len(loads):
                break
            if loads[start_idx:start_idx+substr_len] == loads[start_idx+substr_len:start_idx+substr_len+substr_len]:
                found = True
                substr = loads[start_idx:start_idx+substr_len]
                cycle_start = start_idx
                cycle_end = start_idx+substr_len
                break
        if found:
            break
        substr_len += 1

    idx = (1000000000-(cycle_start+1))%len(substr)
    res = substr[idx]
    print(res)

    



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
