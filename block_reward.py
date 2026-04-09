class BlockReward:
    def __init__(self, initial_reward=10, halving_cycle=100):
        self.initial = initial_reward
        self.cycle = halving_cycle

    def get_reward(self, block_height):
        halvings = block_height // self.cycle
        return self.initial / (2 ** halvings)
