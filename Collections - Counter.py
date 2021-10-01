from collections import Counter
x = int(input())
mylist = input().split()
c = Counter(mylist)
k = Counter(mylist).keys()
n = int(input())
sum = 0
for i in range(n):
    a,b = input().split()
    for j in k:
        if str(j) == str(a):
            index = j
            o = c.get(str(index))
            if o>0:
                sum += int(b)
                c[str(index)] = c.get(str(index)) - 1
            else:
                continue
        else:
            continue
print(sum)
