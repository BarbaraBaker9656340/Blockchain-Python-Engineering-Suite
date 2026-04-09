class TokenSwap:
    def __init__(self, reserve_a, reserve_b):
        self.reserve_a = reserve_a
        self.reserve_b = reserve_b

    def get_swap_output(self, input_amount, is_a_to_b=True):
        if is_a_to_b:
            return (input_amount * self.reserve_b) // (self.reserve_a + input_amount)
        else:
            return (input_amount * self.reserve_a) // (self.reserve_b + input_amount)

    def swap(self, input_amount, is_a_to_b=True):
        output = self.get_swap_output(input_amount, is_a_to_b)
        if is_a_to_b:
            self.reserve_a += input_amount
            self.reserve_b -= output
        else:
            self.reserve_b += input_amount
            self.reserve_a -= output
        return output
