########################################################################################
# Last exmaple we learnt about writing classvars and instance vars.
# Class vars are vars that are shared among all instances of a class 
# Class vars should be same for each instance 
# Inst vars are unique for each instance like our name, email, pay
# For our Employee class what kind of data can be shared as common. Well let's take this example
# Example: Let's say that annual_raise is a common value for all employee globally

# Below is an example extra method defined to create rasie of employee pay, where we can 
# use a global class variable:
# Now all out methods automatically taker-in the instance
class Employee:
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay * 1.04) #Pay increment by 4% (raise by 4%)

emp_1 = Employee('Corey','Schaffer',50)
emp_2 = Employee('Test','User',60)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

########################################################################################
########################################################################################
