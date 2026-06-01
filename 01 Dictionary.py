def freqCount(n):
    # freq = {}
    # for i in n:
    #     if i in freq:
    #         freq[i]+=1
    #     else :
    #         freq[i] = 1
    # return freq
    hash_map = {}
    for i in range(0, len(n)):
        hash_map[n[i]] = hash_map.get(n[i],0)+1
    return hash_map

def setHashMap(m):
    hashLi = [0]*11
    for i in m:
        hashLi[i]+=1
    return hashLi

# ---------------------------------------- #
size = int(input("Enter size of array: "))
li = []
print("Enter elements of the array: ")
for i in range(0, size):
    n = int(input(": "))
    li.append(n)
choice = int(input(
    "Enter your choice:\n"
    "1) Count frequency\n"
    "2) Hash map\n"
    ":"
))

match choice:
    case 1:
        print(freqCount(li))
    case 2:
        print(setHashMap(li))
    case _:
        print("Invalid choice")
