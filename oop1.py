# class definition
class SoftwareEngineer:

    # constructor method.  Setting up instance attributes
    # self is the instance of the class and must be passed
    def __init__(self, name, age, level, salary):
      self.name = name
      self.age = age
      self.level = level
      self.salary = salary
    
    # class attribute
    alias = 'Software Engineer'

    # instance method
    def code(self):
      print(f'{self.name} is writing code...')

    def code_in_language(self, language):
      print(f'{self.name} is writing code in {language}')

    def information(self):
      information = f'{self.name} is a {self.alias} and is {self.age} years old.'
      return information

    # "dunder" methods are provided by python for all classes
    def __str__(self):
      information = f'{self.name} is a {self.alias} and is {self.age} years old.'
      return information

    #checks if two objects are equal.  can use all of the instance attributes or just a few.
    def __eq__(self, other):
      return self.name == other.name and self.age == other.age and self.level == other.level and self.salary == other.salary

    @staticmethod # decorator used to define a static method and allow self not to be passed
    def entry_salary(age):
      if age < 25:
        return 5000
      if age < 30:
        return 7000
      return 9000

# class instance
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)

# instance attributes specific to this instance
print(se1.name, se1.age)
print(se2.name, se2.age)

# class attribute that is shared by all instances
print(se1.alias)
print(se2.alias)

# calling instance methods specific to this instance
se1.code()
se2.code()
se1.code_in_language('Python')
se2.code_in_language('Java')

# __str__ method is called when the object is printed
print(se1.information())
print(se1)

# __eq__ method is called when the object is compared
se3 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)
print(se1 == se3) # false
print(se2 == se3) # true

# using a class's static method
print(se1.entry_salary(24)) # accessed by instance
print(SoftwareEngineer.entry_salary(25)) # accessed by class