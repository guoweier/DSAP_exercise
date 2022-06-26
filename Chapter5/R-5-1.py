# Execute the experiment from Code Fragment 5.1 and compare the results on your system to those we report in Code Fragment 5.2.

import sys
data = []
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)

# my result:
# Length: 0; Size in bytes: 64
# Length: 1; Size in bytes: 96
# Length: 2; Size in bytes: 96
# ...

# Code Fragment 5.2 results:
# Length: 0; Size in bytes: 72
# Length: 1; Size in bytes: 104
# Length: 2; Size in bytes: 104
# ...
