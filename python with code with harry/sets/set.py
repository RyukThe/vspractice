s= {1, 2, 43, 34, "Hello"}
print(s, type(s))
# print(s[0]) not allowed in set 

# method underset
s = {1, 3, 4, 343, 234}
print(s)

set1= {2, 34, 1, 3, "tom", 'queen'}
set2= {'zebra', 23, 32, 34, 2, 'queen'}
unionSet= set1.union(set2)
print(unionSet)
print(set1.intersection(set2))

l=[1,2,3,4,2,34,234,1]
sets=set(l)
print(sets)
print(type(sets))


