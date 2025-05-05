tuple= (1, 2, 3, 4, "S", 2.34)
print(tuple)
print(tuple[2])

#tuple unpacking
tup=(2, 3, 4)
a, b, c = tup
print(a, b, c)

# assigning single value in tuple 
single = (1)
print(single, "Type of single: ", type(single))
single = (1,)
print(single, "Type of single: ", type(single))

# Methods under the tuple
t= (1, 3, 4, 2, 34, 234, "moon", 2, "moon", 2, 2, 2)
print(f"Number of 2 present in t = {t.count(2)}")
print(f"First occurence of index of 2 = {t.index(2)}")
