def solve(s):
    b = sum(1 for i in s if i.islower())
    c = sum(1 for i in s if i.isupper())
    if b > c or b == c:
        return s.lower()
    if c > b:
        return s.upper()