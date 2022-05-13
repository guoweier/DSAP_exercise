#python function that find vowels in a given character string. 

def find_vowels(charstring):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    total = len([char for char in charstring if char in vowels])
    return total

charstring = "MerryChristmasBaibey"
print(find_vowels(charstring))

