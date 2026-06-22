class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def details(self):
        return f"{self.name} earns {self.salary} per month."
    
class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    @property
    def details(self):
        return f"{self.name} earns {self.salary} per month and manages {self.team_size} people."
    
class Intern(Employee):

    def __init__(self, name, salary, duration):
        super().__init__(name, salary)
        self.duration = duration

    @property
    def details(self):
        return f"{self.name} earns {self.salary} per month and their internship is {self.duration} months."
    

employee1 = Employee("Brenda", 4000)
employee2 = Manager("Amy", 45000,21)
employee3 = Intern("Scott", 1500, 15)

print(employee1.details)
print(employee2.details)
print(employee3.details)
