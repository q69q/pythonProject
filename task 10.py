a = int(input())
b = 0
for i in range(a):
    d = int(input())
    if d == 1:
        b += 1
print(b if b < a/2 else a - b)
