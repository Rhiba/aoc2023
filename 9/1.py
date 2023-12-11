
import sys

def main(in_string):
    next_values = []
    for sequence in in_string.splitlines():
        sequence = [int(x) for x in sequence.split(' ')]
        all_zero = False
        layers = [sequence]
        while not all_zero:
            last_layer = layers[-1]
            if all(v == 0 for v in last_layer):
                all_zero = True
            else:
                diffs = []
                for i in range(len(last_layer)-1):
                    diffs.append(last_layer[i+1]-last_layer[i])
                layers.append(diffs)

        next_values.append(sum([x[-1] for x in layers]))

    print(sum(next_values))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
