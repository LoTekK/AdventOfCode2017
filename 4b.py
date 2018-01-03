import utils
from pathlib import Path
from collections import Counter


count = 0
invalid = 0
with utils.get_input(4) as f:
    for line in f:
        count += 1
        input = [sorted(dict(Counter(i.strip('\n\r'))).items()) for i in line.split(' ')]
        for i in reversed(range(len(input))):
            if input.pop(i) in input:
                invalid += 1
                break

print(count - invalid)