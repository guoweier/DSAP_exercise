# class sequence iterator modification

class SequenceIterator:
    '''An iterator for any of Python's sequence types.'''

    def __init__(self, sequence):
        '''Create an iterator for the given sequence.'''
        self._seq = sequence    # keep a ref to the underlying data
        self._k = 1             # will increment to 0 on first call to next

    def __next__(self):
        '''Return the next element, or else raise StopIteration error.'''
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        '''By convension, an iterator must return itself as an iterator.'''
        return self


class ReversedSequenceIterator(SequenceIterator):
    '''A reverse iterator.'''

    def __init__(self, sequence):
        '''Create a new interator for the sequence.
        '''
        super().__init__(sequence)

    def __next__(self):
        '''Return the previous element, or else raise StopIteration error.'''
        self._k += 1
        if self._k <= len(self._seq):
            return(self._seq[-(self._k)])
        else:
            raise StopIteration()


if __name__ in '__main__':
    u = ReversedSequenceIterator([1,2,3,4,5])
    i = 1
    while i < 5:
        print(u.__next__())
        i += 1
