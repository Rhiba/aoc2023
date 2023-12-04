
import sys

def main(in_string):
    points = []
    for card in in_string.splitlines():
        tmp = card.split(":")[1].strip() 
        winning_numbers = tmp.split("|")[0].strip().split(" ")
        winning_numbers = [x for x in winning_numbers if x]
        numbers = tmp.split("|")[1].strip().split(" ")
        numbers = [x for x in numbers if x]
        matches = 0
        for n in numbers:
            if n in winning_numbers:
                matches += 1
        pnts = 2**(matches-1) if matches > 0 else 0
        points.append(pnts)


    print(sum(points))



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
