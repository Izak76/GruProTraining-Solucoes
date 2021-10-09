n = int(input())
t = 1
while n:
    p1 = input()
    p2 = input()

    print(f"Teste {t}")
    for _ in range(n):
        print(p1 if not sum(map(int, input().split()))%2 else p2)

    print()
    t += 1
    n = int(input())
