from hummingbot.market.binance.binance_market import BinanceMarket
from hummingbot.market.bybit.bybit_market import BybitMarket
from hummingbot.market.gateio.gateio_market import GateioMarket
from hummingbot.market.bitfinex.bitfinex_market import BitfinexMarket
from hummingbot.market.huobi.huobi_market import HuobiGlobalMarket
from hummingbot.market.kucoin.kucoin_market import KucoinMarket
from config import (
    binance_key, binance_secret, 
    bybit_key, bybit_secret, 
    gateio_key, gateio_secret, 
    bitfinex_key, bitfinex_secret, 
    huobi_key, huobi_secret, 
    kucoin_key, kucoin_secret
)
# Initialize the markets
binance = BinanceMarket()
bybit = BybitMarket()
gateio = GateioMarket()
bitfinex = BitfinexMarket()
huobi = HuobiGlobalMarket()
kucoin = KucoinMarket()

# List of markets to be used in the strategy
markets = [binance, bybit, gateio, bitfinex, huobi, kucoin]

# Configure API keys in hummingbot
with open("hummingbot_config.yml", 'w') as config_file:
    config_file.write(f"""
binance:
  api_key: {binance_key}
  secret_key: {binance_secret}
bybit:
  api_key: {bybit_key}
  secret_key: {bybit_secret}
gateio:
  api_key: {gateio_key}
  secret_key: {gateio_secret}
bitfinex:
  api_key: {bitfinex_key}
  secret_key: {bitfinex_secret}
huobi:
  api_key: {huobi_key}
  secret_key: {huobi_secret}
kucoin:
  api_key: {kucoin_key}
  secret_key: {kucoin_secret}
""")

# Start the hummingbot client
app = Application(strategy_file_path="./hummingbot_strategy.py", config_path="hummingbot_config.yml")
app.start()
