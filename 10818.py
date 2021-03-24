N = int(input())
li = list(map(int, input().split()))
maxa =-1000000
mina =1000000

for i in li:
    if i > maxa :
        maxa= i
    if i < mina :
        mina = i
print(mina,maxa)
# print('{} {}'.format(min(li), max(li)))
