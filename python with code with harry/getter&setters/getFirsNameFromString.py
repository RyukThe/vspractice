class Employee:
    def __init__(self, name, salary):
            self.name=name
            self.salary= salary
            
    @property
    def first_name(self):
       ful =self.name.split(" ")
       return ful[0]
    @first_name.setter 
    def first_name(self, new):
        ful=self.name.split(" ")
        new_name=f"{new} {ful[1]}"
        self.name=new_name

    

e = Employee("Montu kumar", 10343)
# print(e.get_First_Name())

# print(e.set_first_Name("golu"))
# print(e.get_First_Name())
'''Instead using above we can use '''
print(e.first_name)
e.first_name="rahul"
print(e.name)
         