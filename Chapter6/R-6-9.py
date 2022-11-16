# Had the queue of the previous problem been an instance of ArrayQueue that used an initial array of capacity 30, and had its size never been greater than 30, what would be the final value of the _front instance variable?

# Let's assume the 5 Empty errors are happened at the start.
# Then it remains 32 enqueue and (15-5)=10 dequeue.
# Only dequeue change _front. (enqueue has no effect on _front)
# Let's assume it first enqueue 30 times. So the capacity is full.
# Then it dequeue 10 times. Based on formula:
# _front.new = (_front.old + 1) % len(data)
# so every time, the new _front can add 1 compared with the _front.old.
# So after 10 times dequeue, _front = 9 (python counts from 0)
# And last, there are 2 enqueue. Because enqueue does not have effect on _front.
# So finally, _front = 9.
