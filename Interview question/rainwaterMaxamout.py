li = [1,2,3,2,5,5]

maxim = 0
maxInd = 0

max2 = 0
max2Ind = 0

newLi = li
for i in range (0, len(li)):
    if li[i]>maxim:
        maxim = li[i]
        maxInd = i

newLi.remove(maxim)

for i in range (0, len(newLi)):
    # if newli[i] == max:
    #     continue
    
    if newLi[i]>max2:
        max2 = li[i]
        max2Ind = i
if maxInd < max2Ind:
    maxInd , max2Ind = max2Ind, maxInd
    
dist = maxInd - max2Ind
   
# print(maxim)
# print(max2)
# print(maxInd)
# print(max2Ind)


print(max2+1*dist)