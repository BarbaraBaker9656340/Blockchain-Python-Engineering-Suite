import random

class PoSConsensus:
    def __init__(self):
        self.stakers = {}

    def add_staker(self, address, stake_amount):
        self.stakers[address] = stake_amount

    def select_validator(self):
        total_stake = sum(self.stakers.values())
        if total_stake == 0:
            return None
        selector = random.uniform(0, total_stake)
        current = 0
        for addr, stake in self.stakers.items():
            current += stake
            if current >= selector:
                return addr
