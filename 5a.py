import utils
from pathlib import Path


with utils.get_input(5) as f:
    input = [int(n) for n in f.read().splitlines()]
    count = 0
    index = 0
    try:
        while True:
            input[index] += 1
            index += input[index] - 1
            count += 1
    except:
        print(count)