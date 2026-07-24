def printConsec(li, key):
    posib=0
    for i in range(0, len(li)):
        count=0
        for j in range(i, len(li)):
            if li[j] == key:
                count+=1
            else :
                break
        if count >= 7:
            posib+=1
    return posib


li = [1,2,3,4,5,5,5,5,5,5,5,5,8,9,5]

print(printConsec(li, 5))
