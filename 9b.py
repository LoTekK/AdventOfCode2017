import utils
import re


sum = 0
with utils.get_input(9) as f:
    # input = f.read();
    count = False
    input = re.sub(r'!.', '', f.read())
    for c in input:
        if c == '<' and not count:
            count = True
            continue
        if c == '>':
            count = False
            continue
        if count:
            sum += 1
print(sum)
