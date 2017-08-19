

def rollString(input_str, i, j, op):
    out_str = []
    for idx, c in enumerate(input_str):
        if idx < i:
            out_str.append(c)
            continue
        if idx > j:
            out_str.append(c)
            continue
        if op == 'L':
            if c == 'z':
                c = 'a'
            else:
                c = chr(ord(c) + 1)
        elif op == 'R':
            if c == 'a':
                c = 'z'
            else:
                c = chr(ord(c) - 1)
        out_str.append(c)

    return out_str


if __name__ == '__main__':
    input_str = 'abc'
    i = 0
    j = 2
    op = 'L'
    k = [(0, 0, 'L'), (0,0,'R')]
    out_str = input_str
    for sub in k:
        out_str = rollString(out_str, sub[0], sub[1], sub[2])
    print ''.join(out_str)