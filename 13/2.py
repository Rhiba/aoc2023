
import sys

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def edit_dist(row1, row2):
    changes = 0
    for i in range(len(row1)):
        if not row1[i] == row2[i]:
            changes += 1
    return changes

def main(in_string):
    grids = in_string.split("\n\n")

    total = 0
    for g in grids:
        grid = g.split('\n')
        grid_t = [''.join(x) for x in zip(*grid)]

        score = None
        for split in range(1,len(grid_t)):
            before = grid_t[:split]
            after = grid_t[split:]
            mirrored = True
            delta = 0
            for i in range(min(len(before),len(after))):
                delta += edit_dist(before[len(before)-1-i],after[i])
            if delta == 1:
                score = split
                break

        if not score:
            for split in range(1,len(grid)):
                before = grid[:split]
                after = grid[split:]
                delta = 0
                for i in range(min(len(before),len(after))):
                    delta += edit_dist(before[len(before)-1-i],after[i])
                if delta == 1:
                    score = split*100
                    break

        print_grid(grid)
        print("score:",score)
        print()
        total += score
    print(total)





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
