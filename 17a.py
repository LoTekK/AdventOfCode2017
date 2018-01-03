input = 335
# input = 3


buffer = [0]
index = 0
steps = 2017
for i in range(steps):
    index = (index + input) % len(buffer) + 1
    buffer.insert(index, i + 1)
print([buffer[b] for b in range(index - 2, index + 3)])