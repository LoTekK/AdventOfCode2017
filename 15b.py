import utils
import re


reqs = {'A': 4, 'B': 8}
factors = {'A': 16807, 'B': 48271}
divisor = 2147483647
num_pairs = 5000000
# num_pairs = 1100

def generator(k, start):
    value = start
    while True:
        value *= factors[k]
        value %= divisor
        if value % reqs[k] == 0:
            yield value

with utils.get_input(15) as f:
    matches = 0
    input = {re.sub(r'.*\s', '', k.strip()): int(v.strip()) for (k, v) in [l.split('starts with') for l in f.readlines()]}
    # input['A'] = 65
    # input['B'] = 8921
    A = generator('A', input['A'])
    B = generator('B', input['B'])
    for i in range(num_pairs):
        a = next(A)
        b = next(B)
        if a & 0xFFFF == b & 0xFFFF:
            matches += 1
        print(i, matches)
print(matches)


# # num_pairs = 1100
# pairs_remaining = num_pairs
# matches = 0
# with utils.get_input(15) as f:
#     input = {re.sub(r'.*\s', '', k.strip()): int(v.strip()) for (k, v) in [l.split('starts with') for l in f.readlines()]}
#     input['A'] = 65
#     input['B'] = 8921
#     pairs = {'A': [], 'B': []}
#     comp = dict()
#     while pairs_remaining > 0:
#         for k, v in input.items():
#             input[k] = (input[k] * factors[k]) % divisor
#             if input[k] % reqs[k] == 0:
#                 value = format(input[k], '016b')[-16:]
#                 if k not in comp:
#                     comp[k] = value
#                     # print(comp[k])
#                 else:
#                     pairs[k].insert(0, value)
#                     # print(pairs[k])
#         if len(comp) == 2:
#             pairs_remaining -= 1
#             if comp['A'] == comp['B']:
#                 matches += 1
#             # print(num_steps, comp, matches)
#             comp = dict()
#             for k in input.keys():
#                 if len(pairs[k]) > 0:
#                     comp[k] = pairs[k].pop()
#         print(num_pairs - pairs_remaining, matches)
# print(matches)