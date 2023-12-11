import itertools
import sys

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def main(in_string):
    grid = [list(x) for x in in_string.splitlines()]
    empty_cols = []
    x = 0
    while x < len(grid[0]):
        col = [grid[y][x]=='.' for y in range(len(grid))]
        if all(col):
            empty_cols.append(x)
        x += 1

    empty_rows = []
    y = 0
    while y < len(grid):
        row = [grid[y][x]=='.' for x in range(len(grid[0]))]
        if all(row):
            empty_rows.append(y)
        y += 1

    galaxies = []
    for y, row in enumerate(grid):
        for x, entry in enumerate(row):
            if entry == '#':
                galaxies.append((x,y))

    path_lens = []
    additional = 999999
    for comb in itertools.combinations(list(range(len(galaxies))),2):
        g1 = galaxies[comb[0]]
        g2 = galaxies[comb[1]]
        manhat = abs(g1[0]-g2[0])+abs(g1[1]-g2[1])
        for ec in empty_cols:
            if (g1[0] < ec and g2[0] > ec) or (g2[0] < ec and g1[0] > ec): 
                manhat += additional
        for er in empty_rows:
            if (g1[1] < er and g2[1] > er) or (g2[1] < er and g1[1] > er): 
                manhat += additional
        path_lens.append(manhat)

    print(sum(path_lens))
        

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
