class UTXO:
    def __init__(self):
        self.utxo_set = {}

    def add_utxo(self, tx_id, index, address, amount):
        key = f"{tx_id}_{index}"
        self.utxo_set[key] = {"address": address, "amount": amount}

    def remove_utxo(self, tx_id, index):
        key = f"{tx_id}_{index}"
        self.utxo_set.pop(key, None)

    def get_address_balance(self, address):
        total = 0
        for utxo in self.utxo_set.values():
            if utxo["address"] == address:
                total += utxo["amount"]
        return total
