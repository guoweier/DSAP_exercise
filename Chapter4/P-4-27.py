# QUESTION
# Python's os modue provides a function with signature walk(path) that is a generator yielding the tuple (dirpath, dirnames, filenames) for each subdirectory of the directory identified by string path, such taht string dirpath is the full path to the subdirectory, dirnames is a list of the names of the subdirectories within dirpath, and filenames is a list of names of non-directory entries of dirpath. Give your own implementation of such a walk function.

import os

def get_dirs(path,dirnames=list()):
    '''Return all the subdirectory in a list.'''
    for filename in os.listdir(path):
        childpath = os.path.join(path,filename)
        if os.path.isdir(childpath):
            dirnames.append(filename)
    return dirnames

def get_files(path,filenames=list()):
    '''Return all the non-directory file in a list.'''
    for filename in os.listdir(path):
        childpath = os.path.join(path,filename)
        if os.path.isfile(childpath):
            filenames.append(filename)
    return filenames

def walks(path):
    '''Return a tuple with (dirpath, dirnames, filenames).'''
    dirnames = get_dirs(path)
    filenames = get_files(path)
    return (path, dirnames, filenames)


if __name__ in "__main__":
    path = '../DataStructure/'
    print(walks(path))
