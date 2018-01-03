import utils
from contextlib import contextmanager


@contextmanager
def rotate(l, n):
    l[:] = l[-n:] + l[:-n]
    yield l
    l[:] = l[n:] + l[:n]


suffix = [17, 31, 73, 47, 23]
index = 0
skip = 0
nums = [n for n in range(256)]
with utils.get_input(10) as f:
    hash_input = [ord(n) for n in f.read() if not n.isspace()] + suffix
    for step in range(64):
        for n in hash_input:
            r = max(0, index + n - len(nums))
            with rotate(nums, -r):
                ri = (index - r) % len(nums)
                nums[ri:ri + n] = reversed(nums[ri:ri + n])
                index = (index + n + skip) % len(nums)
                skip += 1
h = list()
for j in range(16):
    h.append(0)
    for k in range(16):
        h[j] ^= nums[j * 16 + k]
    h[j] = str.format('{:02x}', h[j])
print(''.join(h))
