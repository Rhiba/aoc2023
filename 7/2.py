
import sys

def main(in_string):
    hands = [(x.split(' ')[0],int(x.split(' ')[1])) for x in in_string.splitlines()]
    sorted_hands = sorted(hands, key=lambda x: (get_type(x[0]), value_mapping(x[0])))

    acc = 0
    for idx, (hand,bid) in enumerate(sorted_hands):
        acc += (idx+1)*bid

    print(acc)


def value_mapping(hand):
    value_list = []
    for card in hand:
        if card.isdigit():
            value_list.append(int(card))
        elif card == 'T':
            value_list.append(10)
        elif card == 'Q':
            value_list.append(11)
        elif card == 'K':
            value_list.append(12)
        elif card == 'A':
            value_list.append(13)
        elif card == 'J':
            value_list.append(1)

    return value_list


def get_type(hand):
    # 1 = high card, 2 = one pair, 3 = two pair, 4 = three of a kind, 5 = full house
    # 6 = four of a kind, 7 = five of a kind
    dupes = list(set((i,hand.count(i)) for i in hand if hand.count(i) > 1 and not i == 'J'))
    jokers = hand.count('J')
    if jokers:
        if len(dupes) == 0:
            if jokers == 5:
                dupes = [('X',jokers)]
            else:
                dupes = [('X',jokers+1)]
        elif len(dupes) == 1:
            dupes = [(dupes[0][0],dupes[0][1]+jokers)]
        elif len(dupes) == 2:
            dupes = [(dupes[0][0],dupes[0][1]+jokers)] + [dupes[1]]


    if len(dupes) == 0:
        return 1
    elif len(dupes) == 1:
        if dupes[0][1] == 2:
            return 2
        elif dupes[0][1] == 3:
            return 4
        elif dupes[0][1] == 4:
            return 6
        elif dupes[0][1] == 5:
            return 7
    elif len(dupes) == 2:
        if dupes[0][1] == 2 and dupes[1][1] == 2:
            return 3
        elif (dupes[0][1] == 2 and dupes[1][1] == 3) or (dupes[0][1] == 3 and dupes[1][1] == 2):
            return 5


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
