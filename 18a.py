import utils


with utils.get_input(18) as f:
    last_sound = 0
    rcv = 0
    registers = dict()
    input = [i.strip().split(' ') for i in f.readlines()]
    pos = 0
    while pos >= 0 and pos < len(input):
        print(pos)
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
        print(action, x, vx, y, vy)
        if action == 'snd':
            last_sound = vx
        if action == 'set':
            registers[x] = vy
        if action == 'add':
            registers[x] += vy
        if action == 'mul':
            registers[x] *= vy
        if action == 'mod' and vy is not 0:
            registers[x] %= vy
        if action == 'rcv' and vx is not 0:
            rcv = vx
            break
        if action == 'jgz':
            if vx > 0:
                pos += y
                continue
        pos += 1
print(last_sound)
