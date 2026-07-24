def rotate(li):
    for i in range (len(li)-1, 0,-1):
        li[i], li[i-1] = li[i-1], li[i]
    return li
    
    
    
li = [1,2,3,4,5,6,7,8,9]

n = int(input("Enter how many times to rotate: "))

for i in range (n):
    rotate(li)
print(li)
