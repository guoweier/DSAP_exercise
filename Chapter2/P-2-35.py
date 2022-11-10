from venv import create


class AutoPackets:
    '''An Internet application for automatic sending packets and receiving packets.'''

    def __init__(self, Alice=0, Bob=0):
        '''Create two new parties, Alice and Bob, initializing the number of packets and their periods.

        Alice       the number of packets Alice create.
        Bob         the number of packets Bob receive.
        '''
        self._Alice = Alice
        self._Bob = Bob

    def read_packet(self):
        '''Bob read packets and delet them.'''
        if self._Bob > 0:
            self._Bob = 0

    def send_packet(self):
        '''Send packet from Alice to Bob.'''
        if self._Alice > 0:
            self._Alice = 0
            self._Bob += self._Alice
        self.read_packet()
        return self._Bob

    def create_packet(self,k):
        '''Alice create packet.'''
        self._Alice += k
        self.send_packet()
        return self._Bob



if __name__ in '__main__':
    u = AutoPackets(3,0)
    print(u.create_packet(5))
