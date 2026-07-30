romanMap = {
    1000 : 'm',
    900 : 'CM',
    500 : 'D',
    400 : 'CD',
    100 : 'C',
    90 : 'XC',
    50 : 'L',
    40 : 'XL',
    10 : 'X',
    9 : 'IX',
    5 : 'V',
    4 : 'IV',
    1 : 'I'
}

num = int(input("Enter a number between 1-3999: "))
res = ""
for key, value in romanMap.items():
    while num>=key:
        res = res + value
        num = num - key
        
print(res)