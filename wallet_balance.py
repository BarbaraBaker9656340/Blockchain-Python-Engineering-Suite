class WalletBalance:
    @staticmethod
    def calculate_balance(address, blockchain):
        balance = 0.0
        for block in blockchain.chain:
            for tx in block.transactions:
                if tx.get("recipient") == address:
                    balance += tx.get("amount", 0)
                if tx.get("sender") == address:
                    balance -= tx.get("amount", 0)
        return balance
