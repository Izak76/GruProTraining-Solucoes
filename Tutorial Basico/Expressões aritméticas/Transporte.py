n = 1
for x, y in zip(map(int, input().split()), map(int, input().split())):
    n *= y//x

print(n)
