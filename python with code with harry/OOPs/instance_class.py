class Employee:
    company="Asus"
    def __init__(self, salary, name, bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company 
        
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Company Name : {Employee.company :^10}\nEmployee Info\nName : {self.name:^10}\nSalary : {self.salary:^10}\nBond : {self.bond:^10}")
e1= Employee(45000, "Ruman", 4,"Zoom")
e1.get_info()
print(e1.company) # this always refers the instance variable.
print(Employee.company) # this will always refers the class varialbe. 
#python object introspection
print(dir(e1))

