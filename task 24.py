n = int( input('n = '))
lis = [ int(x) for x in input('-> ').split()]
n = len(lis)
lis = lis + lis[:2]
a = 0
for i in range(n):
    a = max(a, lis[i] + lis[i+1] + lis[i+2])
print(a)