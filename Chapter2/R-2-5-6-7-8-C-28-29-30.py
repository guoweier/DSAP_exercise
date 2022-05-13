# enusre that the caller sends a number as a parameter in CreditCard class

import copy


class CreditCard:
    '''A cosumer credit card.'''

    def __init__(self, customer, bank, acnt, limit, balance=0):
        '''Create a new credit card instance.
        The initial balance is zero.
        customer: customer name
        bank: bank name
        acnt: acount identifier
        limit: credit limit
        '''
        self._customoer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
        self._totalpay = 0
        self._set_balance = copy.deepcopy(balance)

    def get_customer(self):
        '''Return customer name.'''
        return self._customer

    def get_bank(self):
        '''Return bank name.'''
        return self._bank

    def get_account(self):
        '''Return account information.'''
        return self._account

    def get_limit(self):
        '''Return current credit limit.'''
        return self._limit

    def get_balance(self):
        '''Return current balance.'''
        return self._balance

    def charge(self, price):
        '''Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        Call ValueError if the input price is not a number.
        '''
        if not isinstance(price, (int,float)):
            raise TypeError('Price must be numberic.')
        else:
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True    
        
    def make_payment(self, amount):
        '''Process customer payment that reduces balances.
        Call ValueError is the input amount is not a number.
        '''
        if not isinstance(amount, (int,float)):
            raise TypeError('Amount must be numberic.')
        elif amount < 0:
            raise ValueError('Amount cannot be negative.')
        else:
            self._balance -= amount 
            self._totalpay += amount

            

class PredatoryCreditCard(CreditCard):
    '''An extension to CreditCard that compounds interest and fees.'''

    def __init__(self, customer, bank, acnt, limit, apr, minfreq=0.5, chargetime=0, balance=0):
        '''Create a new predatory credit card instance.
        '''
        super().__init__(customer, bank, acnt, limit, balance)
        self._apr = apr
        self._ctime = chargetime
        self._minfreq = minfreq

    def charge(self, price):
        '''Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        '''
        success = super().charge(price)
        if not success:
            self._balance += 5
        self._ctime += 1
        return success

    def process_month(self):
        '''Assess monthly interest on outstanding balance.'''
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

    def surcharge(self):
        '''Charge $1 if the customer make ten calls to charge.'''
        self._balance += self._ctime // 10

    def min_payment(self):
        '''Minimun monthly payment based on the current balance (default 50%).
        Late fee is assessed if the customer not pay the minimum amount on time.
        '''
        minpay = self._balance * self._minfreq
        if minpay > self._totalpay:
            self._balance += 0.02 * (minpay - self._totalpay)
        


if __name__ in '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Savings', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 5000))

    for val in range(1,59):
        J1 = wallet[0].charge(val)
        J2 = wallet[1].charge(2*val)
        J3 = wallet[2].charge(3*val)
        cards = [J1,J2,J3]
        for j in range(3):
            if cards[j] == False:
                print([j+1,val])
                break

    