n, m = map(int, input().split())

ponts = [int(input()) for _ in range(n)]
ponts.sort(reverse=True)

for p in ponts[:m]:
    print(p)