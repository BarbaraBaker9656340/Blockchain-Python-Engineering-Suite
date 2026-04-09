class TransactionPool:
    def __init__(self):
        self.pending_transactions = []

    def add_transaction(self, tx):
        if tx not in self.pending_transactions:
            self.pending_transactions.append(tx)

    def remove_transactions(self, tx_list):
        self.pending_transactions = [tx for tx in self.pending_transactions if tx not in tx_list]

    def get_pending_count(self):
        return len(self.pending_transactions)

    def clear_pool(self):
        self.pending_transactions = []
