# Fibonacci progression


from cmath import sqrt


class Progression:
    '''Iterator producing a generic progression.
    Default iterator produces the whole numbers 0,1,2,...
    '''

    def __init__(self, start=0):
        '''Initialize current to the first value of the progression.'''
        self._current = start

    def _advance(self):
        '''Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the end of a finite progression.'''
        self._current += 1

    def __next__(self):
        '''Return the next element, or else raise StopIteration error.'''
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        '''By convention, an iterator must return itself as an iterator.'''
        return self

    def print_progression(self, n):
        '''Print next n values of the progression.'''
        print(' '.join(str(next(self)) for j in range(n)))


class FibonacciProgression(Progression):
    '''Iterator producing a generalized Fibonacci progression.'''

    def __init__(self, first=0, second=1):
        '''Create a new fibonacci progression.
        
        first the first term of the progression (default 0)
        second the second term of the progression (default 1)
        '''
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        '''Update current value by taking sum of previous two.'''
        self._prev, self._current = self._current, self._prev+self._current


class ArithmeticProgression(Progression):
    '''Iterator producing an arithmetic progression.'''

    def __init__(self, increment=1, start=0):
        '''Create a new arithmetic progression.
        
        increment  the fixed constant to add to each term (default 1).
        start      the first term of the progression (default 0).
        '''
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        '''Update current value by adding the fixed increment.'''
        self._current += self._increment

class AbsFibonacciProgression(Progression):
    '''Iterator producing a Fibonacci progression with two numbers difference.'''

    def __init__(self, first=2, second=200):
        '''Create a progression, each value is the difference between two previous values.
        first   the first number
        second  the second number
        '''
        super().__init__(first)
        self._prev = abs(first+second)

    def _advance(self):
        '''Update the current value by taking the difference between previous two.'''
        self._prev, self._current = self._current, abs(self._prev-self._current)


class SqrtProgression(Progression):
    '''Iterator producing a progression with square root.'''

    def __init__(self, start=65536):
        '''Create a progression, each value is the square root of the previous value.
        start   the first value
        '''
        super().__init__(start)

    def _advance(self):
        '''Update the current value by taking the square root of the previous value.'''
        self._current = sqrt(self._current)


if __name__ in '__main__':
    u = FibonacciProgression(2,2)
    u.print_progression(8)
    v = ArithmeticProgression(7,0)
    time = 0
    while v.__next__() < 63:
        time += 1
    print(time)

    x = AbsFibonacciProgression()
    x.print_progression(8)

    w = SqrtProgression()
    w.print_progression(8)
    