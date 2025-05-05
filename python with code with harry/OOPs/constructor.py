class Employee:
    def __init__(self, salary, name, bond):
        self.salary=salary # create an instance attribute/variable of name salary and assign it with salary
        self.name=name
        self.bond=bond
    
    def get_salary(self):
        return self.salary 
    def get_info(self):
        print(f"Name Of Employee : {self.name}\nSalary : {self.salary}\nBond : {self.bond}")
    
e1= Employee(34000,"Tom", "2 Years")
e1.get_info()
