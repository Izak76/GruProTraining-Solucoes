d = int(input())
r = map(lambda x: int(x)>=d, input().split())
print("S" if all(r) else "N")