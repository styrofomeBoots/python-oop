# encapsulation is the process of hiding the details of a class

class SoftwareEngineer:

  def __init__(self, name, age):
    self.name = name
    self.age = age
    # protected attribute defined by one underscore. private by two.
    # protected can be accessed outside the class, but generally shouldn't be.
    # private can only be accessed inside the class and is enforced by python.
    self._salary = None
    self._num_bugs_solved = 0
  
  # a getter method is a method that returns an attribute
  def get_salary(self):
    return self._salary

  # a setter should be the only way to modify an attribute
  def set_salary(self, salary):
    self._salary = self._calculate_salary(salary)

  def code(self):
    self._num_bugs_solved += 1

  # a method that calculates the salary inside of the class
  # this is private and should only be accessed by the setter
  def _calculate_salary(self, base_salary):
    if self._num_bugs_solved < 10:
      return base_salary
    if self._num_bugs_solved < 100:
      return base_salary * 2
    return base_salary * 3


se = SoftwareEngineer("John", 30)
print(se.name, se.age)

# solve bugs and get paid
for i in range(70):
  se.code()

se.set_salary(2000)
print(se.get_salary())