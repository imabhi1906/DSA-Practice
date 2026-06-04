def recurs(n):
    if n==0:
        return
    print(n)
    recurs(n-1) 

def sumRecursion(n):
    if n==0:
        return n
    return n + sumRecursion(n-1)

def factRecursion(n):
    if n==1:
        return n
    return n * (factRecursion(n-1))

def revArray(li, left, right):
    if left>=right:
        return li
    li[left], li[right] = li[right], li[left]
    return revArray(li, left+1, right-1)

def palindromeCheck(li, left, right):
    if left>=right:
        return True
    elif li[left]!=li[right]:
        return False
    
    return palindromeCheck(li, left+1, right-1)
    


# ---------------------------------------- #
choice = int(input(
    "Enter your choice:\n"
    "1) Print decending order \n"
    "2) Print sum of numbers\n"
    "3) Print factorial\n"
    "4) Reverse array\n"
    "5) Palindrome check\n"
    ":"
))

n = int(input("\n Enter a number/size: "))

match choice:
    case 1:
        (recurs(n))
    case 2:
        print(sumRecursion(n))
    case 3:
        print(factRecursion(n))
    case 4:
        li=[]
        print("Enter values for list :-\n")
        for i in range (0,n):
            a = int(input(": "))
            li.append(a)
        print(revArray(li, 0, n-1))
    case 5:
        li=[]
        print("Enter values for list :-\n")
        for i in range (0,n):
            a = input(": ")
            li.append(a)
        print(palindromeCheck(li, 0, n-1))
    case _:
        print("Invalid choice")


