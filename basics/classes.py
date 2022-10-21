"""
Python is OOP Language, everything is a class with its method


"""

# defining a class 
class HelloWorld:
    """
    This a class named HelloWorld
    
    self ==> reference to current instance of the class
    """
    
    def __init__(self, name) -> None:
        #This function is always executed when a class os initiated
        self.name = name
        pass
    
    def __str__(self) -> str:
        return "It is not a string"
    
    x = list((45,67,54,87,98,65,43,35))    #it is property of class


#creating object
obj = HelloWorld("Aditya")
print(obj)
     