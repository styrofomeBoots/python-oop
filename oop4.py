# pythonically getting, setting, and deleting attributes
# by using the dot operator

class SoftwareEngineer:

  def __init__(self):
    self._salary = None
  
  @property
  def salary(self):
    return self._salary

  @salary.setter
  def salary(self, salary):
    self._salary = salary

  @salary.deleter
  def salary(self):
    del self._salary


se = SoftwareEngineer()
se.salary = 6000
print(se.salary)

del se.salary
# print(se.salary) # running this will cause an error