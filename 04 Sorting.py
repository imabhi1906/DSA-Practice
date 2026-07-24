def selectionSort(li):
    for i in range(0, len(li)):
        minIndx = i
        for j in range (i,len(li)):
            if li[j]<li[minIndx]:
                minIndx = j
        li[i], li[minIndx] = li[minIndx], li[i]
    return li

def bubbleSort(li):
    limit = len(li)
    for i in range (limit-2, -1, -1):
        swap = False
        for j in range (0, i+1):
            if li[j]>li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                swap = True
        if swap == False:
            break 
    return li

def insertionSort(li):
    lm = len(li)
    for i in range (1, lm):
        if li[i-1]>li[i]:
            key = li[i]
            for j in range (i-1, -1, -1):
                if li[j]>key:
                    li[j+1] = li[j]
                    if j==0:
                        li[j]=key
                elif li[j]<=key:
                    li[j+1] = key
                    break
    return li
                    
def mergeSort(li):
    pass



# ---------------------------------------- #

# li = [5,7,8,4,1,6,9,2]
li = [3,5,6,4,8,9,10,7,1]
# li = [3,1,2,4,1,5,2,6,4]

choice = int(input(
    "Enter your choice:\n"
    "1) Use Selection Sort \n"
    "2) Use Bubble Sort\n"
    "3) Use Insertion Sort\n"
    "4) Use Merge Sort\n"
    ":"
))


match choice:
    case 1:
        selectionSort(li)
        
    case 2:
        bubbleSort(li)
        
    case 3:
        insertionSort(li)
    
    case 4:
        mergeSort(li)
        
    case _:
        print("Invalid choice")



print(li)