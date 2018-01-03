import utils


registers = dict()
with utils.get_input(8) as input:
    for line in input:
        statements = [s.split(' ') for s in line.strip().split(' if ')]
        instruction = statements[0]
        condition = statements[1]
        if not condition[0] in registers:
            registers[condition[0]] = 0
        if not instruction[0] in registers:
            registers[instruction[0]] = 0
        if eval(f'{registers[condition[0]]} {condition[1]} {condition[2]}'):
            if instruction[1] == 'inc':
                registers[instruction[0]] += int(instruction[2])
            else:
                registers[instruction[0]] -= int(instruction[2])
registers = [(k, registers[k]) for k in reversed(sorted(registers, key=registers.get))]
print(registers)