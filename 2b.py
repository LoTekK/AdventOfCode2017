import utils


input = list()
with utils.get_input(2) as f:
    for line in f:
        input.append(sorted([int(x) for x in line.split('\t')]))
    sum = 0
    for i in input:
        # sum += abs(i[0] - i[len(i) - 1])
        for ii in reversed(range(len(i))):
            numerator = i[ii]
            divisors = [n for index, n in enumerate(i) if index < ii]
            for n in divisors:
                if numerator % n is 0:
                    sum += numerator / n
                    break
print(sum)
