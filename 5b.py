import utils
from pathlib import Path


with utils.get_input(5) as f:
    input = [int(n) for n in f.read().splitlines()]
    count = 0
    index = 0
    try:
        while True:
            i = index
            index += input[index]
            input[i] += 1 if input[i] < 3 else -1
            count += 1
    except:
        print(count)