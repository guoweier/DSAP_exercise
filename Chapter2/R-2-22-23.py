# collection sequence class

class Sequence:
    '''Our ow version of collections.Sequence abstract base class.'''

    def __init__(self, seq):
        self._elements = seq

    def __len__(self):
        '''Return the length of the sequence.'''
        return len(self._elements)

    def __getitem__(self,j):
        '''Return the element at index j of the sequence.'''
        return self._elements[j]

    def __contains__(self, val):
        '''Return True if val found in the sequence; False otherwise.'''
        for j in range(len(self)):
            if self[j] == val:
                return True
            return False
    def index(self, val):
        '''Return leftmost index at which val is found (or raise ValueError).'''
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        '''Return True if two seqs are the same.'''
        return self._elements == other._elements

    def __lt__(self, other):
        '''Return True if seq1 < seq2.'''
        for j in range(len(self)):
            if self._elements[j] >= other._elements[j]:
                return False
        return True
 
if __name__ in '__main__':
    u = Sequence([1,2,3,4,5])
    v = Sequence([3,4,5,6,7])
    print(u.__eq__(v))
    print(u.__lt__(v))
    

