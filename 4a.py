import utils
from pathlib import Path


count = 0
invalid = 0
with utils.get_input(4) as f:
    for line in f:
        count += 1
        input = [i.strip('\n\r') for i in line.split(' ')]
        for i in reversed(range(len(input))):
            if input.pop(i) in input:
                invalid += 1
                break

print(count - invalid)