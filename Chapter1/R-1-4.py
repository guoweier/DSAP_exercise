# python function, takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.

while True:
    try:
        n = int(input("Enter the number n: "))
        if n <= 0:
            print("Your number must be positive.")
        if n > 0:
            break
    except ValueError:
        print("That is a invalid number.")

def sum_squares(n):
    total = sum(k*k for k in range(1,n))
    return total

print(sum_squares(n))




