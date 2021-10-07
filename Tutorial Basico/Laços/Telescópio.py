a = int(input())
c = 0
for _ in range(int(input())):
    if int(input())*a >= 4e7:
        c += 1

print(c)
