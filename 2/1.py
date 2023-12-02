
import sys

def main(in_string):

    max_map = {"red":12,"green":13,"blue":14}
    ids_poss = []
    ids_imposs = []
    for game in in_string.splitlines():
        splits = game.split(':')
        game_id = int(splits[0].split(" ")[1])
        draws = splits[1].split(';')
        impossible = False
        for draw in draws:
            draw = draw.strip()
            colours = draw.split(',')
            for colour in colours:
                colour = colour.strip()
                num = int(colour.split(' ')[0])
                c = colour.split(' ')[1]
                if num > max_map[c]:
                    impossible = True

        if impossible:
            ids_imposs.append(game_id)
        else:
            ids_poss.append(game_id)

    print(sum(ids_poss))





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
