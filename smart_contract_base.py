class SmartContractBase:
    def __init__(self, contract_address, creator):
        self.contract_address = contract_address
        self.creator = creator
        self.state = {}

    def set_state(self, key, value):
        self.state[key] = value

    def get_state(self, key):
        return self.state.get(key)

    def execute(self, function_name, params):
        method = getattr(self, function_name, None)
        if method:
            return method(**params)
        return "函数不存在"
