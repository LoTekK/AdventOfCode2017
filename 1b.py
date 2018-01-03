import utils


with utils.get_input(1) as f:
    input = f.read().strip()
    sum = 0
    for i in range(len(input)):
        ii = (int(i) + int(len(input) / 2)) % len(input)
        sum += int(input[ii]) if input[i] == input[ii] else 0
    print(sum)
