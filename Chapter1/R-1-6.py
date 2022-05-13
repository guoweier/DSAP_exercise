#python function.
#takes a positive integer n, returns the sum of teh squares of all the odd positive integers smaller than n.

while True:
    try:
        n = int(input("Enter the number n: "))
        if n <= 0:
            print("Your number must be positive.")
        if n > 0:
            break
    except ValueError:
        print("That is a invalid number.")

def sum_odd_squares(n):
    total = sum(k*k for k in range(1,n,2))
    return total

print(sum_odd_squares(n))

