n = list(map(int, input().split()))
c = sorted(n)
d = c[::-1]

if n == c:
    print("C")
elif n == d:
    print("D")
else:
    print("N")
