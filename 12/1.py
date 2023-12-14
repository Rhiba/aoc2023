from itertools import permutations, combinations
import sys
import copy

def strip_ends(pattern, groups):

    changed = True

    while changed:
        changed = False

        if pattern == '' or groups == []:
            break

        first_group = groups[0]
        last_group = groups[-1]

        if pattern[0] == '.':
            pattern = pattern[1:]
            changed = True
            continue

        if pattern[-1] == '.':
            pattern = pattern[:-1]
            changed = True
            continue

        '''
        if pattern[0] == '#' and pattern[:first_group+1].count('#') == first_group:
            pattern = pattern[first_group+1:]
            groups = groups[1:] if len(groups) > 1 else []
            changed = True
        '''

        if pattern[0] == '#' and all([x=='?' or x=='#' for x in pattern[1:first_group]]):
            pattern = pattern[first_group+1:]
            groups = groups[1:] if len(groups) > 1 else []
            changed = True

        if pattern == '' or groups == []:
            break

        '''
        if pattern[-1] == '#' and pattern[-last_group-1:].count('#') == last_group:
            pattern = pattern[:-last_group-1]
            groups = groups[:-1] if len(groups) > 1 else []
            changed = True
        '''

        if pattern[-1] == '#' and all([x=='?' or x=='#' for x in pattern[-last_group:]]):
            pattern = pattern[:-last_group-1]
            groups = groups[:-1] if len(groups) > 1 else []
            changed = True

        if pattern == '' or groups == []:
            break

        '''
        if not all([x=='?' or x=='#' for x in pattern[:groups[0]]]):
            first_idx = pattern.index('.')
            pattern = pattern[first_idx+1:]
            changed = True
        '''



    return pattern, groups



def verify_correct(pattern, groups):
    c = 0
    group_counter = 0
    acc = ''
    while c < len(pattern):
        if pattern[c] == '.':
            if len(acc) > 0:
                if not acc.count('#') == groups[group_counter]:
                    return False
                group_counter += 1
                acc = ''
        else:
            acc += pattern[c]
        c += 1

    if len(acc) > 0:
        if not acc.count('#') == groups[group_counter]:
            return False
        elif acc.count('#') == groups[group_counter] and group_counter + 1 < len(groups)-1:
            return False
    return True


def main(in_string):
    ways = []
    for row in in_string.splitlines():
        pattern = list(row.split(' ')[0])
        groups = [int(x) for x in row.split(' ')[1].split(',')]
        
        arrangements = 0

        final_states = []
        if not '?' in pattern:
            if verify_correct(pattern, groups):
                arrangements += 1
        else:
            current_pattern = pattern.copy()
            current_groups = groups.copy()

            new_pattern, new_groups = strip_ends(current_pattern, current_groups)
            if new_groups == []:
                arrangements += 1

            elif new_pattern and new_groups:
                #print()
                #print('pattern:',''.join(pattern),"dealing with:", (''.join(new_pattern), new_groups))
                #print()
                sections = [x for x in ''.join(new_pattern).split('.') if x]
                changed = True
                while len(sections) > len(new_groups) and changed:
                    #check everything fits
                    new_sections = []
                    changed = False
                    for s in sections:
                        if not all([len(s) < g for g in new_groups]):
                            new_sections.append(s)
                        else:
                            changed = True
                    sections = new_sections

                #print(sections)

                if len(sections) > len(new_groups):
                    section_arrangements = []
                    combs = combinations(list(range(len(sections))), len(new_groups))
                    true_options = []
                    for comb in combs:
                        # does it make sense?
                        print(comb)
                        valid = True
                        not_comb = [i for i in range(len(sections)) if not i in comb]
                        for nc in not_comb:
                            if sections[nc].count('#') > 0:
                                valid = False

                        hash_count = 0
                        for idy, c_entry in enumerate(comb):
                            hash_count += len(sections[c_entry])
                            if hash_count < sum(new_groups[:idy]):
                                valid = False
                        if valid:
                            true_options.append(comb)
                    print(true_options)

                else:
                    true_options = [tuple(list(range(len(sections))))]

                #print(sections, true_options, pattern, groups)

                arrangements_per_option = []
                #print(true_options)
                #print("whole pattern:",''.join(new_pattern))
                #print("sections:",sections)
                for option in true_options:
                    arrags = []
                    squashed_unjoined = [s for idx, s in enumerate(sections) if idx in option]
                    squashed = '.'.join(squashed_unjoined)
                    #print("squashed",squashed,"remaining groups:",new_groups)
                    #print()
                    tot = sum(new_groups)
                    already = squashed.count('#')
                    to_pick = tot-already
                    q_indices = [idx for idx,x in enumerate(squashed) if x == '?']
                    place_combs = combinations(q_indices,to_pick)
                    for pc in place_combs:
                        fixed = []
                        for idx in range(len(squashed)):
                            if squashed[idx] == '?':
                                if idx in pc:
                                    fixed.append('#')
                                else:
                                    fixed.append('.')
                            else:
                                fixed.append(squashed[idx])

                        #print("option:",fixed)
                        if verify_correct(fixed,new_groups):
                            #print("found:",''.join(fixed))
                            missing = [i for i in range(len(sections)) if not i in option]
                            recombined = []
                            sects = []
                            start_idx = 0
                            for i in range(len(option)):
                                length = len(sections[option[i]])
                                sect = fixed[start_idx:start_idx+length]
                                start_idx += length+1
                                sects.append(sect)
                            for i in range(len(sections)):
                                if i in option:
                                    recombined += sects.pop(0)
                                else:
                                    recombined += ['.' for i in range(len(sections[i]))]
                                recombined += ['.']
                            recombined = recombined[:-1]
                            #print("recombined",''.join(recombined))
                            #print()
                            arrags.append(''.join(recombined))
                    arrangements_per_option += list(set(arrags))
                    #print("option:",option,"string:",squashed,"arrangements:",arrags)
                    
                arrangements += len(list(set(arrangements_per_option)))

            print("pattern:",''.join(pattern),"groups:", groups, "arragnements:",arrangements)
            ways.append(arrangements)
    print(sum(ways))
            

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
