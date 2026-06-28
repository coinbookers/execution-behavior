import json

from web3 import Web3
from eth_account import Account

NODE = "https://rpc.example.org"
PRIVATE = "YOUR_PRIVATE_KEY"

terms = (
    "illustrates",
    "endpoint",
    "delivers",
)

rpc = Web3(
    Web3.HTTPProvider(NODE)
)

wallet = Account.from_key(
    PRIVATE
)

events = []

for item in terms:
    events.append(
        {
            "value": item
        }
    )

transaction = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 120000,
    "gasPrice": rpc.to_wei(
        4,
        "gwei"
    ),
    "nonce": rpc.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(
    transaction
)

output = {
    "wallet": wallet.address,
    "size": len(
        signed.raw_transaction.hex()
    ),
    "events": events,
}

with open(
    "endpoint.json",
    "w"
) as file:
    json.dump(
        output,
        file,
        indent=2
    )

for item in terms:
    print(item)

print(wallet.address)

print(transaction["nonce"])

print("Stored")
