n = int(input())

con = "E"
if 1 <= n <= 35:
    con = "D"
elif 36 <= n <= 60:
    con = "C"
elif 61 <= n <= 85:
    con = "B"
elif n >= 86:
    con = "A"

print(con)
