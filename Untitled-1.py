class pet:
    def __init__(self,specie,age):
        self.specie=specie
        self.age=age
    def __str__(self):
        return f"name of animal is {self.specie}and age is {self.age} age"
    def __call__(self):
        return f"name of animal is {self.specie}and age is {self.age} ageeeeee"

a=pet("cat",12)
print(a)
print(a())