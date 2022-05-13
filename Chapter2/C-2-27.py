# class Range modification

from time import time

class Range:
    '''A class that mimic's the build-in range class.'''

    def __init__(self, start, stop=None, step=1):
        '''Initialize a Range instance.
        semantics is similar to built-in range class.
        '''
        if step == 0:
            raise ValueError('step cannot be 0.')

        if stop is None:
            start, stop = 0, start

        # calcualte the effective length once.
        self._length = max(0, (stop-start+step-1)//step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        '''Return number of entries in the range.'''
        return self._length

    def __getitem__(self, k):
        '''Return entry at index k (using standard interpretation if negative).'''
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

if __name__ in '__main__':
    u = Range(100000)
    st1 = time()
    u.__getitem__(4)
    en1 = time()
    e1 = en1 - st1

    st2 = time()
    u.__getitem__(99996)
    en2 = time()
    e2 = en2 - st2

    print(str(e1)+' '+str(e2)) 