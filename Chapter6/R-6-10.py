# Consider what happens if the loop in the ArrayQueue._resize method at lines 53-55 of Code Fragment 6.7 had been implemented as:
# for k in range(self._size):
# self._data[k] = old[k]
# Give a clear explanation of what could go wrong.

# walk = self._front
# This define the location of the first element. This might not stay at the beginning of the capacity data list.
# if self._data[k] = old[k]
# This does not start at the actual first element of the queue.
# then it will lose the elements located forward of old[0].
