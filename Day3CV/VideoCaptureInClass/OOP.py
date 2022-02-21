class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def coughUp(self, name): 
        return ("{} is coughing".format(name))
    
Peter = Person("Rono", 12)
print("{} is {} years old".format(Peter.name, Peter.age)) 
print(Peter.coughUp("Peter Sasa")  )           
