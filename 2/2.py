
import sys

def main(in_string):

    ids_power = []

    for game in in_string.splitlines():
        maxs = {'red':0,'green':0,'blue':0}
        splits = game.split(':')
        game_id = int(splits[0].split(" ")[1])
        draws = splits[1].split(';')
        for draw in draws:
            draw = draw.strip()
            colours = draw.split(',')
            for colour in colours:
                colour = colour.strip()
                num = int(colour.split(' ')[0])
                c = colour.split(' ')[1]
                if num > maxs[c]:
                    maxs[c] = num

        power = maxs['red']*maxs['green']*maxs['blue']
        ids_power.append(power)

    print(sum(ids_power))

        


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
