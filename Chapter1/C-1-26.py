# python program takes three integers as input, 
# then determines if they can be used in a correct arithmetic formula

def three_int_ari(a,b,c):
    ints = [a,b,c]
    maxint = max(ints)
    ints_rest = ints.remove(maxint)
    if (ints[0] + ints[1]) == maxint:
        decide = bool(True)
        out_string = str(ints[0]) + "+" + str(ints[1]) + "=" + str(maxint)
    elif (ints[0]*ints[1]) == maxint:
        decide = bool(True)
        out_string = str(ints[0]) + "*" + str(ints[1]) + "=" + str(maxint)
    else:
        decide = bool(False)
        out_string = "The three integer cannot be used in a correct arithmetic formula."
    return decide, out_string

while True:
    try:
        a = int(input("Enter integer a: "))
        b = int(input("Enter integer b: "))
        c = int(input("Enter integer c: "))
        break
    except ValueError:
        print("That is a invalid number.")

print(three_int_ari(a,b,c))