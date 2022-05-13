'''Report all entries of the file system rooted at the given path having the given file name.

path:       rooted path
filename:   the target filename
'''

import os

def find(path, filename):
    if os.path.isfile(path):
        print(path)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            childpath = os.path.join(path,item)
            if os.path.isdir(childpath):
                find(childpath, filename)
        childpath = os.path.join(path,filename)
        find(childpath, filename)


if __name__ in '__main__':
    path = '/Users/wendy/Desktop/DataStructure/'
    filename = 'try.txt'
    find(path,filename)
