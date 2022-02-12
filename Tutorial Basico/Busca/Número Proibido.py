def gen():
    while True:
        try:
            yield nums.get(input(), "nao")
            
        except EOFError:
            break

input()
nums = dict.fromkeys(input().split(), "sim")

print("\n".join(gen()))
