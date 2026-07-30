dit = {"Masala": "spicy", "Ginger": "Zesty", "Green": "Mild"}

# print(dit)

for i in dit:
    # print(i, dit[i])
    pass
    
for key, val in dit.items():
    # print(key, val)
    pass
    
if "Masala" in dit:
    # print ("I have masala chai")
    pass
sqnum = {x:x**2 for x in range(6)}
# print(sqnum)

# dit.get("salary, 10")
# print(dit)

for val in dit.values():
    # print(val)
    pass
    
print("Masala" in dit.values())