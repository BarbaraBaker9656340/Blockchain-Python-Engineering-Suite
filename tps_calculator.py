import time

class TPSCalculator:
    def __init__(self):
        self.start_time = None
        self.tx_count = 0

    def start(self):
        self.start_time = time.time()
        self.tx_count = 0

    def add_transaction(self):
        self.tx_count += 1

    def get_tps(self):
        if not self.start_time:
            return 0
        duration = time.time() - self.start_time
        return self.tx_count / duration if duration > 0 else 0
