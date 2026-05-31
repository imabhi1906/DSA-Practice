def printDigitsRev(n):
    li = []
    while n>0:
        li.append(n%10)
        n = n//10
    return li

def countDigits(n):
    i=0
    while n>0:
        n=n//10
        i+=1
    return i


def revDigit(n):
    res = 0
    while n>0:
        rem = n%10
        res = res*10+rem
        n=n//10
    return res

def palindromeCheck(n):
    if (n==revDigit(n)):
        return True
    else:
        return False

number = int(input("Enter a number: "))

choice = int(input(
    "Enter your choice:\n"
    "1) Print array of digits reversed\n"
    "2) Count digits\n"
    "3) Reverse digits\n"
    "4) Palindrome check\n"
    ":"
))

match choice:
    case 1:
        print(printDigitsRev(number))
    case 2:
        print(countDigits(number))
    case 3:
        print(revDigit(number))
    case 4:
        print(palindromeCheck(number))
    case _:
        print("Invalid choice")