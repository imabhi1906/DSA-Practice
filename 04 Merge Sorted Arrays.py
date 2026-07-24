l1=[1,2,3,4]
l2=[1,1,3,4,5,6,7]
res = []
i,j = 0,0
n,m = len(l1), len(l2)

while i<n and j<m:
    if l1[i]<=l2[j]:
        res.append(l1[i])
        i+=1
    else:
        # l1[i]>l2[j]:
        res.append(l2[j])
        j+=1

if i<n:
    for i in range (i, n):
        res.append(l1[i])

if j<m:
    for j in range (j, m):
        res.append(l2[j])


print(res)