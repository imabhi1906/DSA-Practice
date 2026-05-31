def countDigits(n):
    i=0
    while n>0:
        n=n//10
        i+=1
    return i


def printDigitsRev(n):
    li = []
    while n>0:
        li.append(n%10)
        n = n//10
    return li


number = int(input("Enter a number: "))
# print(printDigitsRev(number))
print(countDigits(number))
