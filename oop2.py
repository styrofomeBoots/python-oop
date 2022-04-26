# inheritence - process of inheriting attributes and methods from a parent class

# base class.  can be inherited, extended, or overridden
from unittest.util import safe_repr


class Employee:
  
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def work(self):
    print(f'{self.name} is working...')


# inheriting from Employee
class SoftwareEngineer(Employee):
  
  def __init__(self, name, age, salary, level):
    super().__init__(name, age, salary) # calling the parent class constructor by "super"
    self.level = level

  def debug(self):
    print(f'{self.name} is debugging...')

  # overriding the parent class method
  def work(self):
    print(f'{self.name} is writing code...')


# inheriting from Employee
class Designer(Employee):
  
  def draw(self):
    print(f'{self.name} is drawing...')
  
  #overriding the parent class method
  def work(self):
    print(f'{self.name} is designing...')


se = SoftwareEngineer('Max', 20, 5000, 'Junior')
print(se.name, se.age, se.salary, se.level)
se.work()
se.debug()

d = Designer('Phillip', 27, 7000)
print(d.name, d.age)
d.work()
d.draw()


# polymorphism - ability to use the same method name on different types of objects
# polymorphism is achieved by using the same method name but different method implementations
employees = [SoftwareEngineer('Max', 20, 5000, 'Junior'),
             SoftwareEngineer('Lisa', 25, 7000, 'Senior'),
             Designer('Phillip', 27, 7000)]

def motivate_employees(employees):
  for employee in employees:
    employee.work()

motivate_employees(employees)