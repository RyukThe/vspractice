mark = [53, 64, 88, 90, 23]
mixed = ["Hello", 234, 2.4]
print(mark)
print(mixed)
print(mixed[0])
print(mark[0:3])

#Method of list
marks =[1, 2, 3, 5]

def ListOfTable(num=int(input("Enter a Number:"))):
    """The method will create the List of Mathematical table

    Args:
        num (int, optional): Enter a number. Defaults to int(input("Enter a Number:")).
    """
    table=[num*i for i in range(1,11)]
    return f"This is Table of {num} in list format\n{table}"
table=ListOfTable()
print(table)
