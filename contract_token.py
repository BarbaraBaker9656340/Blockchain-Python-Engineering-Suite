class TokenContract(SmartContractBase):
    def __init__(self, address, creator, total_supply, token_name):
        super().__init__(address, creator)
        self.token_name = token_name
        self.set_state("total_supply", total_supply)
        self.set_state("balances", {creator: total_supply})

    def transfer(self, from_addr, to_addr, amount):
        balances = self.get_state("balances")
        if balances.get(from_addr, 0) >= amount:
            balances[from_addr] -= amount
            balances[to_addr] = balances.get(to_addr, 0) + amount
            return True
        return False

    def balance_of(self, address):
        return self.get_state("balances").get(address, 0)
