import utils
import re


sum = 0
with utils.get_input(9) as f:
    # input = f.read();
    score = 0
    skip = False
    input = re.sub(r'!.', '', f.read())
    for c in input:
        if c == '<':
            skip = True
            continue
        if skip:
            if c == '>':
                skip = False
            continue
        if c == '{':
            score += 1
        if c == '}':
            sum += score
            score -= 1
print(sum)
