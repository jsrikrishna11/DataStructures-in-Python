class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance."""
        self._customer = customer
        self._account = acnt
        self._balance = 0
        self._bank = bank
        self._limit = limit
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_balance(self):
        return self._balance
    def get_limit(self):
        return self._limit
    def charge(self, price):
        if price + self._balance> self._limit:
            return False
        else :
            self._balance +=price
            return False
    def make_payment(self, amount):
        if self._balance - amount > 0:
            self._balance -=amount
            return "Transaction Success"
        else:
            return "Insuffience balance"
    
cc = CreditCard("JSK", "Bank", '5391037512341234', limit=1000)

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('JRK', 'Cali','13421324132', 2500))
    wallet.append(CreditCard('JPK', 'Cal','13421324132', 1500))
    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[0].__getattribute__()
    for c in range(2):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Balance = ', wallet[c].get_balance())
        print('Limit = ', wallet[c].get_limit())
    print("EOP")


    
    
