#przykład 2 - iluzja transformacji
data = [1, 2, 3, 4]

def double_inplace(xs):
    for i in range(len(xs)):
        xs[i] *= 2
    return xs

a = data
b = double_inplace(data)    # „transformacja”, która zmienia oryginał
print("a:", a)              # a: [2, 4, 6, 8]  ← oryginał skażony
print("b:", b)              # b: [2, 4, 6, 8]

#bezpieczniej
def double_pure(xs):
    return [x*2 for x in xs]

data = [1, 2, 3, 4]
c = double_pure(data)
print(f"data: {data}")
print(f"c: {c}")

print(sorted(data))
data.sort(reverse=True)
print(data)
data.extend([5,2,7])
print(data)
