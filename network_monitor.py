import time

class NetworkMonitor:
    def __init__(self):
        self.metrics = {"tps": 0, "node_count": 0, "hash_rate": 0}

    def update_tps(self, tx_count, duration):
        self.metrics["tps"] = tx_count / duration if duration > 0 else 0

    def update_node_count(self, count):
        self.metrics["node_count"] = count

    def update_hash_rate(self, hashes_per_second):
        self.metrics["hash_rate"] = hashes_per_second

    def get_status(self):
        return self.metrics
