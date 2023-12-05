
import sys

def main(in_string):
    chunks = in_string.split("\n\n")
    seeds_raw = [int(x) for x in chunks[0].split(':')[1].strip().split(" ")]

    seeds = []
    for i in range(0,len(seeds_raw),2):
        seed_start = seeds_raw[i]
        seed_end = seed_start + seeds_raw[i+1]
        seeds.append((seed_start,seed_end))

    maps = []
    for chunk in chunks[1:]:
        mapping = parse_map(chunk)
        maps.append(mapping)


    states = list(zip(seeds,[0 for i in range(len(seeds))]))
    final_ranges = []

    while len(states) > 0:
        state = states.pop()
        if state[1] == len(maps):
            final_ranges.append(state[0])
        else:
            mapping = maps[state[1]]
            span = state[0]
            untouched = True
            for entry in mapping:
                if span[0] >= entry[0] and span[1] <= entry[1]:
                    # contained within
                    new_span = (span[0]+entry[2],span[1]+entry[2])
                    new_state = (new_span,state[1]+1)
                    states.append(new_state)
                    untouched = False
                elif span[0] < entry[0] and span[1] > entry[0] and span[1] <= entry[1]:
                    #underlapping <-
                    new_span1 = (span[0],entry[0])
                    new_span2 = (entry[0],span[1])
                    states.append((new_span1,state[1]))
                    states.append((new_span2,state[1]))
                    untouched = False
                elif span[0] >= entry[0] and span[0] < entry[1] and span[1] > entry[1]:
                    #overlapping ->
                    new_span1 = (span[0],entry[1])
                    new_span2 = (entry[1],span[1])
                    states.append((new_span1,state[1]))
                    states.append((new_span2,state[1]))
                    untouched = False

            if untouched:
                new_state = (span,state[1]+1)
                states.append(new_state)

    min_num = None
    for r in final_ranges:
        if not min_num:
            min_num = r[0]
        elif r[0] < min_num:
            min_num = r[0]

    print(min_num)


    '''
    final_locations = []
    for seed_range in seeds:
        acc_offset = 0
        for mapping in maps:
            seed_loc = seed + acc_offset
            for entry in mapping:
                if seed_loc >= entry[0] and seed_loc < entry[1]:
                    acc_offset += entry[2]
                    break

        end_dest = seed + acc_offset
        final_locations.append(end_dest)

    print(min(final_locations))
    '''


def parse_map(chunk):
    tmp = chunk.splitlines()
    mapping = []
    for line in tmp[1:]:
        spl = [int(x) for x in line.split(" ")]
        dest = spl[0]
        source = spl[1]
        ran = spl[2]
        offset = dest-source
        map_entry = (source,source+ran,offset)
        mapping.append(map_entry)

    return mapping

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
