
# QN5


class calc:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print('Sum of {} and {} is : {}'.format(self.num1,self.num2,self.num2+self.num1))

    def sub(self):
        print('Difference of {} and {} is : {}'.format(self.num2, self.num1,self.num2 - self.num1))

    def mul(self):
        print('Product of {} and {} is : {:.3f}'.format(self.num1,self.num2,self.num1 * self.num2))

    def div(self):
        print('Quotient of {} and {} is : {:.3f}'.format(self.num1,self.num2,self.num1 / self.num2))

a=float(input('Enter the first no :'))
b=float(input('Enter the second no :'))
c1=calc(a,b)

c1.add()
c1.sub()
c1.mul()
c1.div()
