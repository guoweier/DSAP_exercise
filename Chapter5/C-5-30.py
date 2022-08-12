# When Bob wants to send Alice a message M on the Internet, he breaks M into n data packets, numbers the packets consecutively, and injects them into the network. When the packets arrive at Alice's computer, they may be out of order, so Alice must assemble the sequence of n packets in order before she can be sure she as the entire message. Describe an efficient scheme for Alice to do this, assuming that she knows the value of n. What is the running time of this algorithm?

def rebuild_msg(seq,n):
    '''Rebuild random ordered sequence of n data packets into the original message.
    seq: a list of data packets indices.
    n: the number of data packets.
    This is actually a sorting problem. I use bubble sort algorithm here.'''
    for i in range(n):
        for j in range(0,n-i-1):
            if seq[j] > seq[j+1]:
                seq[j+1],seq[j] = seq[j],seq[j+1]


if __name__ in "__main__":
    seq = [12,2,32,4,1,87,10]
    n = len(seq)
    rebuild_msg(seq,n)
    print(seq)

# This is using O(n2) time.
# for each i, it has (n-i) times in the nested for loop.
# In total, there are (n-1)+(n-2)+(n-3)+...+2+1 times. It equals n*(n-1)/2 = 1/2*n2-1/2*n
# So it is O(n2) time. 
