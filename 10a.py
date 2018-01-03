import utils
from contextlib import contextmanager


@contextmanager
def rotate(l, n):
    l[:] = l[-n:] + l[:-n]
    yield l
    l[:] = l[n:] + l[:n]


index = 0
skip = 0
nums = [n for n in range(256)]
# nums = [n for n in range(5)]
with utils.get_input(10) as f:
    input = [int(n) for n in f.read().split(',')]
    # input = [3, 4, 1, 5]
    for n in input:
        r = max(0, index + n - len(nums))
        with rotate(nums, -r):
            ri = (index - r) % len(nums)
            nums[ri:ri+n] = reversed(nums[ri:ri+n])
            index = (index + n + skip) % len(nums)
            skip += 1

print(nums[0] * nums[1])