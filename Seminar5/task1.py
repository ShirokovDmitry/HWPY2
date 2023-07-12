# data = {2,4,4,6,8,10,12}
# res1 = {None: item for item in data if item > 4}
# res2 = (item for item in data if item > 4)
# res3 = [[item] for item in data if item > 4]
# print(res1)
# print(res2)
# print(res3)

def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)

for item in gen(10, 1):
    print(f'{item = }')
