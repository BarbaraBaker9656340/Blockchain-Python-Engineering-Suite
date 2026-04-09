class BatchTransaction:
    def __init__(self):
        self.transactions = []

    def add_tx(self, tx):
        self.transactions.append(tx)

    def batch_sign(self, wallet):
        signatures = []
        for tx in self.transactions:
            sign = wallet.sign_data(str(tx.to_dict()))
            tx.sign_transaction(sign)
            signatures.append(sign)
        return signatures

    def get_batch_size(self):
        return len(self.transactions)
