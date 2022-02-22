class Person:
    
    _gender = "male"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def coughUp(self, name): 
        return ("{} is coughing".format(name))
    
Peter = Person("Rono", 12)
print("{} is a  {} years old {}".format(Peter.name, Peter.age, Peter._gender)) 
print(Peter.coughUp("Peter Sasa")  )           
