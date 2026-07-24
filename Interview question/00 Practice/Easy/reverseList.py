def revli(l):
    i=0
    j=len(l)-1
    
    while i<j or i!=j:
        l[i], l[j]=l[j], l[i]
        i+=1
        j-=1
    return l 
    

li = [1,2,3,4,5,6,7,8,9]

print(revli(li))
