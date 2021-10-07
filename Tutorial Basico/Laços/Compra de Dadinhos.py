while True:
    n, c, d = map(int, input().split())
    if not any((n, c, d)):
        break

    print(n*c*d)
