# Class 
class Employee:
  company = "HP"
  def get_salary(self):
    print(self)# referes the current object. this print statement print memory location of objects. 
    return 34000
# Object creation
emp1 = Employee()
print(f"Salary of Employee1 {emp1.get_salary()}")
emp2 = Employee()
print(f"Salary of Employee2 {emp2.get_salary()}")