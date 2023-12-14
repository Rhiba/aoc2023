from itertools import permutations, combinations
import sys
import copy

def is_completable(building, pattern, groups):
    sectors = [x for x in building.split('.') if x]

    if len(sectors) > len(groups):
        return False

    already = building.count('#')
    total = sum(groups)

    existing = pattern[len(building):].count('#')
    q_marks = pattern[len(building):].count('?')
    if already + existing + q_marks < total:
        return False


    for idx in range(len(sectors)):
        if idx < len(groups) and idx < len(sectors)-1 and not len(sectors[idx]) == groups[idx]:
            return False
        elif idx < len(groups) and len(sectors[idx]) > groups[idx]:
            return False

    return True

cache = dict()

def arrangements(building, pattern, groups):

    global cache

    combs = 0
    building_groups = [len(x) for x in building.split('.') if x]

    if building:
        key = (str(building_groups), len(building), building[-1])
        if key in cache:
            return cache[key]
    
    if len(building) == len(pattern):
        sectors = [x for x in building.split('.') if x]
        if not len(sectors) == len(groups):
            return 0

        for idx in range(len(sectors)):
            if not len(sectors[idx]) == groups[idx]:
                return 0
        return 1
    else:
        if not is_completable(building,pattern,groups):
            return 0

    new_idx = len(building)
    if pattern[new_idx] =='?':
        combs = arrangements(building+'.',pattern,groups) + arrangements(building+'#',pattern,groups)
    else:
        combs = arrangements(building+pattern[new_idx],pattern,groups)
    
    if building:
        cache[key] = combs 

    return combs

def main(in_string):

    global cache

    ways = []
    for row in in_string.splitlines():
        cache = dict()
        pattern = list(row.split(' ')[0])
        orig_pattern = pattern.copy()
        for i in range(4):
            pattern += ['?'] + orig_pattern
        groups = [int(x) for x in row.split(' ')[1].split(',')]
        groups_orig = groups.copy()
        for i in range(4):
            groups += groups_orig
        print(''.join(pattern),groups)
        tmp = arrangements('',pattern,groups)
        print(''.join(pattern),tmp,"\n",end='')
        ways.append(tmp)

    print(sum(ways))

         

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
