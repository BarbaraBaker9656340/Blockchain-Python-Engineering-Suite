class DynamicDifficultyAdjust:
    def __init__(self, base_difficulty=4, target_block_time=10):
        self.base = base_difficulty
        self.target = target_block_time

    def adjust(self, last_blocks: list):
        if len(last_blocks) < 2:
            return self.base
        total_time = last_blocks[-1].timestamp - last_blocks[0].timestamp
        avg_time = total_time / (len(last_blocks)-1)
        if avg_time < self.target * 0.5:
            return self.base + 1
        elif avg_time > self.target * 2:
            return max(1, self.base - 1)
        return self.base
