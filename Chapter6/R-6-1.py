# What values are returned during the following series of stack operations, if executed upon an initially empty stack?

# push(5): - | [5]
# push(3): - | [5,3]
# pop(): 3 | [5]
# push(2): - | [5,2]
# push(8): - | [5,2,8]
# pop(): 8 | [5,2]
# pop(): 2 | [5]
# push(9): - | [5,9]
# push(1): - | [5,9,1]
# pop(): 1 | [5,9]
# push(7): - | [5,9,7]
# push(6): - | [5,9,7,6]
# pop(): 6 | [5,9,7]
# pop(): 7 | [5,9]
# push(4): - | [5,9,4]
# pop(): 4 | [5,9]
# pop(): 9 | [5]
