# class Vector modification

from time import time


class Vector:
    '''Represent a vector in a multidimensional space.'''

    def __init__(self,d):
        '''Creat d-dimentional vector of zeros.'''
        if isinstance(d,int):
            self._coords = [0]*d
        elif isinstance(d,list):
            self._coords = d

    def __len__(self):
        '''Return the dimension of the vector.'''
        return len(self._coords)
    def __getitem__(self, j):
        '''Return jth coordinate of vector.'''
        return self._coords[j]

    def __setitem__(self, j, val):
        '''Set jth coordinate of vector to given value.'''
        self._coords[j] = val
    
    def __add__(self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        '''Return the differences between two vectors.'''
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        '''Return a negative vector.'''
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __mul__(self,other):
        '''If other is numeric, return a multiplied vector.
        If other is a vector, return a dot product.
        '''
        if isinstance(other, (int,float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*other
            return result
        elif isinstance(other, list):
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            result = 0
            for j in range(len(self)):
                result += self[j]*other[j]
            return result
    
    def __eq__(self, other):
        '''Return True if vector has same coordinates as others.'''
        return self._coords == other._coords
    
    def __ne__(self, other):
        '''Return True if vector differs from others.'''
        return not self == other
    
    def __str__(self):
        '''Produce string representation of vector.'''
        return '<'+str(self._coords)[1:-1] + '>'


if __name__ in '__main__':
    u = Vector(5)
    v = Vector(5)
    k = 3
    for j in range(len(u)):
        u.__setitem__(j,j)
        v.__setitem__(j,j)
    print(u.__sub__(v))
    print(v.__neg__())
    print(u.__add__([5,3,10,-2,1]))
    print(u.__mul__(v))
    w = Vector([5,4,7])

    '''C-2-25'''
    start_time1 = time()
    print(u.__mul__(v))
    end_time1 = time()
    elapsed1 = end_time1-start_time1

    start_time2 = time()
    print(u.__mul__(k))
    end_time2 = time()
    elapsed2 = end_time2-start_time2

    print(str(elapsed1)+' '+str(elapsed2))