data = [1, 2, 3, 4]

def double_inplace(xs):
    for i in range(len(xs)):
        xs[i] *= 2
    return xs

a = data
b = double_inplace(data)    # „transformacja”, która zmienia oryginał
print("a:", a)              # a: [2, 4, 6, 8]  ← oryginał skażony
print("b:", b)              # b: [2, 4, 6, 8]
