import utils


with utils.get_input(23) as f:
    muls = 0
    registers = dict()
    input = [i.strip().split(' ') for i in f.readlines()]
    # registers['a'] = 1
    # registers['b'] = 0
    # registers['c'] = 0
    # registers['d'] = 0
    # registers['e'] = 0
    # registers['f'] = 0
    # registers['g'] = 0
    # registers['h'] = 0
    pos = 0
    while 0 <= pos < len(input):
        i = input[pos]
        action = i[0]
        try:
            x = int(i[1])
        except ValueError:
            x = i[1]
        if type(x) is int:
            vx = x
        else:
            if x not in registers:
                registers[x] = 0
            vx = registers[x]
        if len(i) > 2:
            try:
                y = int(i[2])
            except ValueError:
                y = i[2]
            if type(y) is int:
                vy = y
            else:
                if y not in registers:
                    registers[y] = 0
                vy = registers[y]
        print(pos, action, x, vx, y, vy)
        if action == 'set':
            registers[x] = vy
        if action == 'sub':
            registers[x] -= vy
        if action == 'mul':
            registers[x] *= vy
            muls += 1
        if action == 'jnz':
            if vx != 0:
                pos += vy
                continue
        pos += 1
print(registers['h'])
