class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
        
    @property    
    def life_stage(self):
        if self.age < 13:
            return "child"
        elif 13 <= self.age <= 17:
            return "teenager"
        elif 18 <= self.age <= 64:
            return "adult"
        else:
            return "senior"
        

person1 = Person("Asiyah", 16)
person2 = Person("Mandy", 45)
person3 = Person("Eliza", 6)
person4 = Person("Amy", 75)

print(person1.name)
print(person1.is_adult)
print(person1.life_stage)

print(person2.name)
print(person2.is_adult)
print(person2.life_stage)

print(person3.name)
print(person3.is_adult)
print(person3.life_stage)

print(person4.name)
print(person4.is_adult)
print(person4.life_stage)
