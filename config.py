# load .env
from dotenv import load_dotenv, dotenv_values
load_dotenv() 

config = dotenv_values(".env")

# print(f"config {config}")

# Add the exchange credentials
binance_key = config["binance_key"]
binance_secret = config["binance_secret"]
bybit_key = config["bybit_key"]
bybit_secret = config["bybit_secret"]
gateio_key = config["gateio_key"]
gateio_secret = config["gateio_secret"]
bitfinex_key = config["bitfinex_key"]
bitfinex_secret = config["bitfinex_secret"]
huobi_key = config["huobi_key"]
huobi_secret = config["huobi_secret"]
kucoin_key = config["kucoin_key"]
kucoin_secret = config["kucoin_secret"]


# print(bybit_key)