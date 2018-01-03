import utils
from pathlib import Path


results = []
with utils.get_input(6) as f:
    count = 0
    input = [int(n) for n in f.read().split('\t')]
    bank_count = len(input)
    result = ' '.join([str(n) for n in input])
    while True:
        block_count = sorted(input)[len(input) - 1]
        bank = input.index(block_count)
        input[bank] = 0
        while block_count > 0:
            bank = (bank + 1) % bank_count
            input[bank] += 1
            block_count -= 1
        count += 1
        result = ' '.join([str(n) for n in input])
        if result in results:
            original_loop = results.index(result) + 1
            break
        results.append(result)

print(count, original_loop, count - original_loop)