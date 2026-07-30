d = {}
# 1. Add a new key value pair
d['name'] = 'John'

# 2. update existing key
d.update({'age' : 20})

# 3. Remove a key safely
d.pop('salary', None)

# 4. Print all keys
print(d.keys())

# 5. Print all values
print(d.values())

# 6. Print all key-value pairs
for key, val in d.items():
    print(key, " -> ", val)

# 7. Check if a key exists
k = 'salary'
if k in d:
    print(True)
else:
    print(False)

#  8. Difference between
# d["age"]
# and
# d.get("age")
# When should you use each?
# we should use .het() when we wanna safely print the value for the key

# 9. What happens here?
# d = {}
# d[1] = "One"
# d[1] = "Hello"
# print(d)
#  {1:"Hello"}

# 10. Output?
# d = {1: "A", 2: "B"}
# print(len(d))
# the output should be 2

# 11. Reverse key and value
dit = {
    "a": 1,
    "b": 2
}
dit.update({
    1: 'a',
    2: 'b'
})
dit.pop('a')
dit.pop('b')

# 12. Print only the keys whose values are even
d12 = {x:x**2 for x in range(6)}
li = []
for k, v in d12.items():
    if v%2==0:
        li.append(k)
print(li)

# 13. Sum all values
sum = 0
for val in d12.values():
    sum = sum + val
print(sum)

# 14. Find the largest value
max = list(d12.keys())[0]
for kay, vel in d12.items():
    if kay >= vel:
        if kay > max:
            max = kay
    else:
        if vel > max:
                max = vel

# 15. Find the key having the maximum value
#  Didn't understand this question

# 16. Count frequency of every character
char = 'malayalam'
f = {}
for i in char:
    if i not in f:
        f[i] = 1
    else:
        f[i]+= 1
print(f)

# 17. Count frequency of every word
sentence = "apple banana apple orange banana apple"
f = {}
for i in sentence.split():
    if i not in f:
        f[i] = 1
    else:
        f[i]+= 1

# 18. First non-repeating character
inp = 'aabbcde'
f = {}
for i in inp:
    if i not in f:
        f[i] = 1
    else:
        f[i]+= 1

for key, val in f.items():
    if val == 1:
        print(key)
        break
    
# 19. First repeating character
inp = 'aabbabcaefcde'
f = {}
for i in inp:
    if i not in f:
        f[i] = 1
    else:
        f[i]+= 1


for key, val in f.items():
    if val > 1:
        print(key)
        break

# 20. Find duplicates in a list

li = [1,2,3,4,2,5,3]
f = {}
for i in li:
    if i not in f:
        f[i] = 1
    else:
        f[i]+= 1

for key, val in f.items():
    if val > 1:
        print(key, ' ',end="")
print()

# 21. Print all student names.
students = {
    101:{
        "name":"John",
        "marks":80
    },
    102:{
        "name":"Alice",
        "marks":95
    }
}

for key in students:
    print(students[key]['name'])

# 22. Print the student having highest marks.
high = 0
for key in students:
    if students[key]['marks'] > high:
        high = students[key]['marks']
print(high)

# 23. Increase everyone's marks by 5.
for key in students:
    students[key]['marks']+= 5

print(students.values())

# 24. Add 'grade : A' to every student.
for key in students:
    students[key]['grade'] = 'A'
print(students.values())

# 25. Create
# {
# 1:1,
# 2:4,
# 3:9,
# 4:16,
# 5:25
# }
# using dictionary comprehension.
ditcomp = {x:x**2 for x in range(1, 6)}
print(ditcomp)

# 26. Create a dictionary containing only even numbers.
ditcomp = {x:x*2 for x in range(1, 6)}
print(ditcomp)

# 27. Swap keys and values using comprehension
student = {
    "name": "John",
    "age": 25,
    "city": "Delhi"
}
swappedstudents= {value: key for key, value in student.items()}
print(swappedstudents)

# 28. Predict the output
a = {}
print(bool(a))
#  The output. should be false as the dictionary is empty

# 29. Predict the output
a = {}
print(a.get("age"))
# the answer will be None

# 30. Predict the output
a = {}
print(a["age"])
#  This will throw an error as the data is not called safelyand the age doesnt exist in dictionary a

# 31. Predict the output
a = {
    1:10,
    True:20
}
print(a)
#  True is treated as 1 in python so it took the final value and initial key

# 32. Predict the output
a = {
    1:"One",
    1.0:"Float"
}
print(a)
# Python sees 1 and 1.0 as the same also so it kept the first key and the last value