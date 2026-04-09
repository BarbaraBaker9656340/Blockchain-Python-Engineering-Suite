import requests

class OracleModule:
    @staticmethod
    def fetch_price(symbol="BTC"):
        try:
            res = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd", timeout=2)
            return res.json().get(symbol.lower(), {}).get("usd", 0)
        except:
            return 0

    def write_to_chain(self, contract, key, value):
        contract.set_state(key, value)
