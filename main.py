
from agents import Agent, Runner, function_tool
import requests
from typing import List, Dict
from connection import config

@function_tool
def get_all_coins() -> List[Dict]:
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return [{"error": f"Failed to fetch all coins: {str(e)}"}]

@function_tool
def get_coin_by_symbol(symbol: str) -> Dict:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch {symbol.upper()}: {str(e)}"}

crypto_agent = Agent(
    name="CryptoAgent",
    instructions=(
        "You are a helpful assistant that provides real-time cryptocurrency prices "
        "using the Binance API. Use the tools to answer questions accurately."
    ),
    tools=[get_all_coins, get_coin_by_symbol]
)

# Run synchronously with prompt
result = Runner.run_sync(
    crypto_agent,
    # "What is the price of ETHUSDT?",
    "What is the price of BTCUSDT?",
    run_config=config
)

# Print the final output
print(result.final_output)
