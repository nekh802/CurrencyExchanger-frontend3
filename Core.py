from dataclasses import dataclass

CURRENCY_FORMAT = {
    "USD": {"decimals" : 2, "comma": True},
    "EUR": {"decimals" : 2, "comma": True},
    "JPY": {"decimals" : 0, "comma": True},
    "KRW": {"decimals" : 0, "comma": True},
    "BTC": {"decimals" : 8, "comma": True},
}

def convert_amount(amount, src, dst, rates, base="USD"):
    src = src.upper()
    dst = dst.upper()
    base = base.upper()

    if amount < 0:
        raise ValueError("amount must be non-negative")

    if src == dst:
        return amount

    # src -> base
    if src != base:
        amount /= rates[src]

    # base -> dst
    if dst != base:
        amount *= rates[dst]

    return amount

def format_money(amount: float, currency: str) -> str: 
    currency = currency.upper()
    rule = CURRENCY_FORMAT.get(currency,{"decimals": 2, "comma": True})
    decimals = rule["decimals"]
    comma = rule["comma"]

    if comma: 
        fmt = f"{{:,.{decimals}f}}"
    else : 
        fmt = f"{{:.{decimals}f}}"
    
    return fmt.format(amount)

@dataclass(frozen=True)
class RateTable:
    rates: dict

    def convert(self, amount: float, src: str, dst: str) -> float: 
        src = src.upper()
        dst = dst.upper()

        if amount < 0 : 
            raise ValueError("amount must be non-negative")
        
        if src == dst : 
            return amount
        
        try: 
            rate = self.rates[src][dst]
        except KeyError:
            raise KeyError(f"Missing rate: {src} -> {dst}")
        
        return amount * rate
    
'''
DEFAULT_RATES = RateTable(
    rates = {
        "USD" : {"KRW": 1330.0, "JPY": 155.0},
        "KRW" : {"USD": 1/1330.0, "JPY": 155.0/1330.0},
        "JPY" : {"KRW" : 1330.0/155.0},
    }
)'''