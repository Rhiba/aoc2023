
import sys

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

def main(in_string):
    grid = in_string.splitlines()
    grid = [list(x) for x in grid]
    #find S
    current = None
    for y, row in enumerate(grid):
        for x, entry in enumerate(row):
            if entry == 'S':
                current = (x,y)

    loop = [current]
    while len(loop) <= 1 or not loop[0] == loop[-1]: 
        # north
        current_x = loop[-1][0]
        current_y = loop[-1][1]
        current_symbol = grid[current_y][current_x]
        dirs = []
        if current_symbol == 'S':
            # north, east, south, west
            dirs = [1,2,3,4]
        elif current_symbol == '|':
            dirs = [1,3]
        elif current_symbol == '-':
            dirs = [2,4]
        elif current_symbol == 'L':
            dirs = [1,2]
        elif current_symbol == 'J':
            dirs = [1,4]
        elif current_symbol == '7':
            dirs = [3,4]
        elif current_symbol == 'F':
            dirs = [2,3]
        else:
            print("UH OH")
            sys.exit(0)

        if 1 in dirs:
            #north
            if (len(loop) > 1 and not (current_x,current_y-1) == loop[-2]) or (len(loop)==1 and current_y-1 >= 0 and (grid[current_y-1][current_x] == '|' or grid[current_y-1][current_x] == '7'or grid[current_y-1][current_x] == 'F' )):
                loop.append((current_x,current_y-1))
                continue
            
        if 2 in dirs:
            #east
            if (len(loop) > 1 and not (current_x+1,current_y) == loop[-2]) or (len(loop)==1 and current_x+1 < len(grid[0]) and (grid[current_y][current_x+1] == '-' or grid[current_y][current_x+1] == 'J'or grid[current_y][current_x+1] == '7' )):
                loop.append((current_x+1,current_y))
                continue

        if 3 in dirs:
            #south
            if (len(loop) > 1 and not (current_x,current_y+1) == loop[-2]) or (len(loop)==1 and current_y+1 < len(grid) and (grid[current_y+1][current_x] == '|' or grid[current_y+1][current_x] == 'L'or grid[current_y+1][current_x] == 'J' )):
                loop.append((current_x,current_y+1))
                continue

        if 4 in dirs:
            #west
            if (len(loop) > 1 and not (current_x-1,current_y) == loop[-2]) or (len(loop)==1 and current_x-1 >= 0 and (grid[current_y][current_x-1] == '-' or grid[current_y][current_x-1] == 'L'or grid[current_y][current_x-1] == 'F' )):
                loop.append((current_x-1,current_y))
                continue

    loop = loop[:-1]
    s_eq = None
    sx = loop[0][0]
    sy = loop[0][1]
    if loop[-1] == (sx-1,sy) and loop[1] == (sx+1,sy):
        s_eq = '-'
    elif loop[-1] == (sx-1,sy) and loop[1] == (sx,sy+1):
        s_eq = '7'
    elif loop[-1] == (sx-1,sy) and loop[1] == (sx,sy-1):
        s_eq = 'J'
    elif loop[-1] == (sx,sy-1) and loop[1] == (sx,sy+1):
        s_eq = '|'
    elif loop[-1] == (sx,sy-1) and loop[1] == (sx+1,sy):
        s_eq = 'L'
    elif loop[-1] == (sx,sy-1) and loop[1] == (sx-1,sy):
        s_eq = 'J'
    elif loop[-1] == (sx+1,sy) and loop[1] == (sx-1,sy):
        s_eq = '-'
    elif loop[-1] == (sx+1,sy) and loop[1] == (sx,sy+1):
        s_eq = 'F'
    elif loop[-1] == (sx+1,sy) and loop[1] == (sx,sy-1):
        s_eq = 'L'
    elif loop[-1] == (sx,sy+1) and loop[1] == (sx,sy-1):
        s_eq = '|'
    elif loop[-1] == (sx,sy+1) and loop[1] == (sx+1,sy):
        s_eq = 'F'
    elif loop[-1] == (sx,sy+1) and loop[1] == (sx-1,sy):
        s_eq = '7'

    grid[sy][sx] = s_eq

    inside = []
    for idy, row in enumerate(grid):
        in_row = False
        for idx, entry in enumerate(row):
            if (idx,idy) in loop:
                if entry == '|' or entry == 'F' or entry == '7':
                    in_row = not in_row
            else:
                if in_row:
                    inside.append((idx,idy))

    print(inside)
    print(len(inside))



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
