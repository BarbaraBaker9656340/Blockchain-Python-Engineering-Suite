import time

class MempoolCleaner:
    def __init__(self, expire_seconds=3600):
        self.expire = expire_seconds

    def clean_expired_transactions(self, tx_pool):
        now = time.time()
        valid = []
        for tx in tx_pool.pending_transactions:
            if now - tx.timestamp < self.expire:
                valid.append(tx)
        tx_pool.pending_transactions = valid
        return len(valid)
