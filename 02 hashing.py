def hash_map(n):
    hmap = {}
    for i in range(0, len(n)):
        hmap[n[i]] = hmap.get(n[i],0)+1
    return hmap



# ---------------------------------------- #
size = int(input("Enter size of array: "))
li = []
print("Enter elements of the array: ")
for i in range(0, size):
    n = (input(": "))
    li.append(n)
choice = int(input(
    "Enter your choice:\n"
    "1) Count frequency\n"
    ":"
))

match choice:
    case 1:
        print(hash_map(li))
    case _:
        print("Invalid choice")
