# 22. Print the student having highest marks.
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
high = float('-inf')
for key in students:
    if students[key]['marks'] > high:
        high = students[key]['marks']
print(high)