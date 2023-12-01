
import sys

def main(in_string):

    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']

    total = 0
    for line in in_string.splitlines():
        digit_string = ''
        acc = ''
        for char in line:
            acc += char
            if char.isdigit():
                digit_string += char
                break
            else:
                broken = False
                for idx,n in enumerate(numbers):
                    if n in acc:
                        digit_string += str(idx)
                        broken = True
                        break
                if broken:
                    break
        acc = ''
        for char in line[::-1]:
            acc = char + acc
            if char.isdigit():
                digit_string += char
                break
            else:
                broken = False
                for idx,n in enumerate(numbers):
                    if n in acc:
                        digit_string += str(idx)
                        broken = True
                        break
                if broken:
                    break



        num = int(digit_string)
        total += num

    print(total)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
