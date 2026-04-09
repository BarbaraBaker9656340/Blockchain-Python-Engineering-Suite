class AccountModel:
    def __init__(self):
        self.accounts = {}

    def create_account(self, address, initial_balance=0):
        if address not in self.accounts:
            self.accounts[address] = initial_balance

    def transfer(self, from_addr, to_addr, amount):
        if self.accounts.get(from_addr, 0) < amount:
            return False
        self.accounts[from_addr] -= amount
        self.accounts[to_addr] = self.accounts.get(to_addr, 0) + amount
        return True

    def get_balance(self, address):
        return self.accounts.get(address, 0)
