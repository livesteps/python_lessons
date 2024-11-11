### Explain Class and Instance of a class
# Class is a blueprint of creating any instances and each unique employee 
#that we create using our employee class will be an instance of that class


### Ex: Simple class and body is left empty for now ####################################
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

# Here emp_1, emp_2 equals employee then, each of these are going to be their own unique
# instances of the employee class
# From print(),  We can observe unique Memory allocation space for both employee objects
# instance of the class
########################################################################################
# Now let's learn diff b/w instance-variables and class-variables
# Instance vars contain data that are unique to each instance.
# Now, we could manually create instance_vars->attributes for each employee by doing something like below
# emp_1.attrs, emp_2.attrs which are unique respective to each instance_var
# In below example, we can printout emp_1.email and emp_2.email 
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first='Corey'
emp_1.last='Corey'
emp_1.email='Corey.Schaffer@Company.com'
emp_1.pay=50000

emp_2.first='Test'
emp_2.last='User'
emp_2.email='Test.User@Company.com'
emp_2.pay=60000

print(emp_1.email)
print(emp_2.email)
########################################################################################
# Now let's say we wanted to set all of the attr for each employee(class variable)
# when they are created instead of doing all of this manual-edits as above...
# We don't want to manually set these vars everytime you cansee it's a lot of code and
# it's also prone to mistakes.
# Now inorder to reap quicker benefits, using the clesses, to make this to setup automatically 
# when we create the employee we are 
# going to create a special init method inside our Employee class.
# We can think of this __init__ method as "initialize", as in any other language as a  constructor.
# Now when we create methods within a class, they receive the instance as first argument automatically.
# By default we call the 1st arg as self or in any other name. But let's follow convention.
# after self, we can specify whatever other arguments for the method.
# So our next arguments that we declare are first, last, pay
# Let's form the email using first, and last names.
# Then for body of the __init__  method(), we create self along with respective vars
# like self.var1, self.var2 ...etc
#  Finally when creating the object/instances of the Employee class, the __init__ method is automatically
# initialized , yet we can pass the values that we can specify in out __init__()
# Now our init method takes the instance which we call it "self" and the first name and 
# last name and pay as arguments, but when we create our employee down here the instance
# is passed automatically, so we can leaveoff 'self' and we can pass all the same information
#we did manually down there and for the second one too...

class Employee:
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'

emp_1 = Employee('Corey','Schaffer',50)
emp_2 = Employee('Test','User',60)

print(emp_1)
print(emp_2)

"""
emp_1.first='Corey'
emp_1.last='Corey'
emp_1.email='Corey.Schaffer@Company.com'
emp_1.pay=50000

emp_2.first='Test'
emp_2.last='User'
emp_2.email='Test.User@Company.com'
emp_2.pay=60000
"""

print(emp_1.email)
print(emp_2.email)

########################################################################################
# Now let's say, we want to add some action such as ability to display the fullname of the employee 
# Thus using last print() with format() we could print out the full name.
## But thats a lot to type to display full name of employee. So let's create a method next.
class Employee:
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'

emp_1 = Employee('Corey','Schaffer',50)
emp_2 = Employee('Test','User',60)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))

########################################################################################
# Here we can define additional methods to the class Employee to achieve.
class Employee:
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey','Schaffer',50)
emp_2 = Employee('Test','User',60)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)
emp_1.fullname()
print(Employee.fullname(emp_1)) ### Another way to print full name using class variable
emp_2.fullname()
print(Employee.fullname(emp_2))

