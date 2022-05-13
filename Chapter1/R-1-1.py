# Write a short Python function, is_multiple(n,m).
# Takes two integer values and returns True if n is a multiple of m.
# False otherwise. 

n = int(input("Enter the number n: "))
m = int(input("Enter the number m: "))

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

print(is_multiple(n,m))    