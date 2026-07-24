name = "abhishekanil"
check = {}

for i in name:

    if i not in check:
        check[i] = 1
        
    else :
        check[i]+=1
        
print(check)