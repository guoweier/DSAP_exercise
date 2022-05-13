# derivative of polynomial


class Derivative:
    '''The first derivative of a polynomial in standard algebraic notation.'''

    def __init__(self, equation, variable="x"):
        '''Create the polynomial and distinguished the first nomial.'''
        self._first = equation.split('+')[0]
        self._variable = variable
    

    def get_coeff(self):
        '''Return the coeff in the first nomial.'''
        if self._first[0] == self._variable:    # variable is the first element
            coeff = 1
        elif self._variable not in list(self._first):
            coeff = float(self._first)
        else:
            coeff = float(self._first.split('*')[0])
        return coeff

    def get_expo(self):
        '''Return the exponent in the first nomial.'''
        if self._first[-1] == self._variable:   # variable is the last element
            expo = 1
        elif self._variable not in list(self._first):
            expo = 0
        else:
            expo = float(self._first.split('*')[-1])
        return expo

    def get_derivative(self):
        '''Return derivative of the first nomial.'''
        deri_coeff = self.get_coeff()*self.get_expo()
        deri_expo = self.get_expo()-1
        if deri_expo == 0 or (self._variable not in list(self._first)):
            derivative = str(deri_coeff)
        else:
            derivative = str(deri_coeff)+'*x**'+str(deri_expo)
        return derivative
        

if __name__ in '__main__':
    u = Derivative('4')
    print(u.get_derivative())

        