# take a positive integer greater than 2 as input
# calculate the number of times for division by 2 to get a value less than 2.

def PrintTimesDivideByTwo(number,k=0):
    if number < 2:
        print(k)
        return
    newNumber = number/2
    k += 1
    PrintTimesDivideByTwo(newNumber,k)

if __name__ in "__main__":
    try:
        number1 = input("Enter the number greater than 2: ")
        if number1 < 2:
            print("Your number must be larger than 2.")
        else:
            PrintTimesDivideByTwo(number1)
    except ValueError:
        print("That is an invalid number.")
    