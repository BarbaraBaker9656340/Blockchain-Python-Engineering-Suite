class StakingModule:
    def __init__(self):
        self.stakes = {}
        self.reward_rate = 0.05

    def stake(self, address, amount):
        if address in self.stakes:
            self.stakes[address] += amount
        else:
            self.stakes[address] = amount

    def unstake(self, address, amount):
        if self.stakes.get(address, 0) >= amount:
            self.stakes[address] -= amount
            return True
        return False

    def calculate_reward(self, address):
        return self.stakes.get(address, 0) * self.reward_rate
