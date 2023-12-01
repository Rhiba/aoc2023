
import sys

def main(in_string):
    total = 0
    for line in in_string.splitlines():
        digit_string = ''
        for char in line:
            if char.isdigit():
                digit_string += char
                break
        for char in line[::-1]:
            if char.isdigit():
                digit_string += char
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
