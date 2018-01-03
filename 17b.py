input = 335
# input = 3


buffer = [0]
index = 0
steps = 50000000
for i in range(steps):
    index = (index + input) % (i + 1) + 1
    # buffer.insert(index, i + 1)
    # print(buffer)
    # if i % 10000 == 0:
    #     print(i)
    if index == 1:
        val = i + 1
print(val)