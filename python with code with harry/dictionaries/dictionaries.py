mark={"name":"marks", "rahul":47, "tom":45, "Alice":45}
print(mark, type(mark))
print(f"Value of name is {mark["name"]}")
mark["raman"]=45 # new key:value pair is added
print(mark)
mark["rahul"]=87 # marks of rahul is updated
print(mark)
# method of dictionary
print(mark.keys(), "Type of keys", type(mark.keys()))
print(mark.values(), "Type of Values", type(mark.values()))
mark.pop("tom")
print(mark)
mark.clear()
print(mark)

#list comprenshive
table_of_5={i:5*i for i in range(1, 11)}
print(table_of_5)

dic_for_square={i:i**2 for i in range(1,6) }
print(dic_for_square)

square= lambda s: s**2
print(square(5))
