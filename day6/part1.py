def count_tiles(lines):
    count = 0
    for line in lines:
        count += line.count('X')
    return count + 1

def print_map(lines):
    for line in lines:
        print(''.join(line))

def get_guard(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] in ('<', '>', 'v', '^'):
                return {'dir': lines[y][x], 'x': x, 'y': y}

def move_guard(lines):
    dir, x, y = get_guard(lines).values()
    # print(dir, f'y:{y}', f'x:{x}')
    if dir == '^':
        if y - 1 == -1:
            return 'The guard left'
        elif lines[y - 1][x] == '#':
            lines[y][x] = '>'
            return lines
        else:
            lines[y - 1][x] = '^'
            lines[y][x] = 'X'
            return lines
    if dir == '>':
        if x + 1 == len(lines[0]):
            return 'The guard left'
        elif lines[y][x + 1] == '#':
            lines[y][x] = 'v'
            return lines
        else:
            lines[y][x + 1] = '>'
            lines[y][x] = 'X'
            return lines
    if dir == '<':
        if x - 1 == -1:
            return 'The guard left'
        elif lines[y][x - 1] == '#':
            lines[y][x] = '^'
            return lines
        else:
            lines[y][x - 1] = '<'
            lines[y][x] = 'X'
            return lines
    if dir == 'v':
        if y + 1 == len(lines):
            return 'The guard left'
        elif lines[y + 1][x] == '#':
            lines[y][x] = '<'
            return lines
        else:
            lines[y + 1][x] = 'v'
            lines[y][x] = 'X'
            return lines

def main():
    lab_map = [[y for y in x.rstrip()] for x in open('./day6/input.txt', 'r')]    
    new_map = lab_map
    while not isinstance(new_map, str):
        lab_map = new_map
        # print_map(lab_map)
        # print(get_guard(lab_map))
        new_map = move_guard(lab_map)
    print_map(lab_map)
    print(count_tiles(lab_map))
    
if __name__ == '__main__':
    main()