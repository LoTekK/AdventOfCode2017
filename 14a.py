import utils
from contextlib import contextmanager


@contextmanager
def rotate(l, n):
    l[:] = l[-n:] + l[:-n]
    yield l
    l[:] = l[n:] + l[:n]


def knot_to_bits(k):
    return ''.join([str.format('{:04}', int(bin(int(c, 16))[2:])) for c in k])


input = 'ugkiagan'
# input = 'flqrgnkx'
suffix = [17, 31, 73, 47, 23]
count = 0
for i in range(128):
    index = 0
    skip = 0
    nums = [n for n in range(256)]
    hash_input = [ord(n) for n in f'{input}-{i}'] + suffix
    for step in range(64):
        for n in hash_input:
            r = max(0, index + n - len(nums))
            with rotate(nums, -r):
                ri = (index - r) % len(nums)
                nums[ri:ri+n] = reversed(nums[ri:ri+n])
                index = (index + n + skip) % len(nums)
                skip += 1
    h = list()
    for j in range(16):
        h.append(0)
        for k in range(16):
            h[j] ^= nums[j * 16 + k]
        h[j] = str.format('{:02x}', h[j])
    bits = knot_to_bits(''.join(h))
    count += bits.count('1')
    print(bits, count)
print(count)
