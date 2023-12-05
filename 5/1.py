
import sys

def main(in_string):
    chunks = in_string.split("\n\n")
    seeds = [int(x) for x in chunks[0].split(':')[1].strip().split(" ")]
    maps = []
    for chunk in chunks[1:]:
        mapping = parse_map(chunk)
        maps.append(mapping)

    final_locations = []
    for seed in seeds:
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
