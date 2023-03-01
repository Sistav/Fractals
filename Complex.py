# Program     : Complex number class
# Name        : Georgios Dialynas-Vatsis
# Date        : May 5, 2022
# Description : a super simple complex number class for the fractal program


# This class is super self explanatory, there really isn't much to write about.
class Complex():
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, second):
        # How the 
        real = self.real + second.real
        imaginary = self.imaginary + second.imaginary
        return Complex(real, imaginary)
    
    def __mul__(self, second):
        real = (self.real * second.real) - (self.imaginary * second.imaginary)
        imaginary = (self.imaginary * second.real) + (self.real * second.imaginary)
        return Complex(real,imaginary)