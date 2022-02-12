for n in iter(lambda: int(input()), 0):
    print(f"f91({n}) = {91 if n<=100 else n-10}")