import utils

with utils.get_input(1) as f:
    input = f.read().strip()
    sum = 0
    for i in range(len(input)):
        ii = (int(i) + 1) % len(input)
        sum += int(input[ii]) if input[i] == input[ii] else 0
    print(sum)
