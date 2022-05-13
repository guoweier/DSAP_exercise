# make change

bills = [100,50,20,10,5,1,0.25,0.1,0.05,0.01]

def GiveChange(charged, given):
    forchange = charged - given
    for bill in bills:
        k = 0
        while forchange >= bill:
            forchange = forchange - bill
            k += 1
        if k == 0:
            continue
        else:
            yield [bill,k]



if __name__ in "__main__":
    charged = input("Enter the monetary amound charged: ")
    given = input("Enter the monetary amount given: ")
    print(list(GiveChange(charged,given)))
