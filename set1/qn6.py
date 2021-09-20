# Q6
import math


class circle:

    def __init__(self,radius):
        self.radius=radius
        self.area()
    def area(self):
        self.areA=2*math.pi*self.radius**2
        print('Area of the circle with radius {} = {:.4f} sq.units'.format(self.radius,self.areA) )
        return self.areA

c1=circle(float(input('enter the radius of circle :')))

