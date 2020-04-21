def is_degenerated(line):
    p1, p2 = line
    return p1 == p2

def is_vertical(line):
    (x1, y1), (x2, y2) = line
    return x1 == x2 and y1 != y2

def is_horizontal(line):
    (x1, y1), (x2, y2) = line
    return x1 != x2 and y1 == y2

def is_inclined(line):
    return not (
            is_vertical(line) or is_horizontal(line) or is_degenerated(line))

def def_line_type(line):
    if is_degenerated(line):
        print('degenerated line')
    elif is_vertical(line):
        print('vertical line')
    elif is_horizontal(line):
        print('horizontal line')
    elif is_inclined(line):
        print('inclined line')
