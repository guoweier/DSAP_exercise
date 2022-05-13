# python function, is_even(k).
# takes an integer value and returns True if k is even, and False otherwise. 
# cannot use the multiplication, modulo, or division operator.

while True:
    try:
        k = int(input("Enter the number k: "))
        break
    except ValueError:
        print("That is a invalid number.")

def is_even(k):
    a = bool(True if k%2==0 else False)
    return a

print(is_even(k))