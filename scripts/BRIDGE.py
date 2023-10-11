import json
from web3 import Web3
import asyncio


#connect to web3 providers

# FILL IN WITH CORRECT PORT 
web3_eth = Web3(Web3.HTTPProvider('http://127.0.0.1:8585'))      
web3_bsc = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


# FILL IN WITH CORRECT ID 
ETH_NETWORK_ID = '1678146187539'
BSC_NETWORK_ID = '56'

BSC_ADMIN_PRIVATE_KEY = '0x' # replace with your BSC admin private key CAN BE FOUND UNDER 'PRIVATE KEYS' in Ganache CLI


#load BridgeEth.json and BridgeBsc.json ABI

with open('/build/contracts/BridgeEth.json') as f:
    data = json.loads(f.read())
    bridge_eth_abi = data['abi']
    bridge_eth_address =  data['networks'][ETH_NETWORK_ID]["address"]
    
with open('/build/contracts/BridgeBsc.json') as f:
    data = json.loads(f.read())
    bridge_bsc_abi = data['abi']
    bridge_bsc_address = data['networks'][BSC_NETWORK_ID]["address"]



#set admin private key and account address for BSC

admin_priv_key = BSC_ADMIN_PRIVATE_KEY
admin_address = web3_bsc.eth.account.from_key(admin_priv_key).address

#create contract instances

#bridge_eth_address =  BridgeBsc.networks['4447'].address # '0x...' # replace with BridgeEth contract address
bridge_eth = web3_eth.eth.contract(address=bridge_eth_address, abi=bridge_eth_abi)

#bridge_bsc_address = '0x...' # replace with BridgeBsc contract address
bridge_bsc = web3_bsc.eth.contract(address=bridge_bsc_address, abi=bridge_bsc_abi)

#listen for Transfer events on BridgeEth contract

def handle_transfer_event(event):
    # extract event data
    from_address = event['args']['from']
    to_address = event['args']['to']
    amount = event['args']['amount']
    date = event['args']['date']
    nonce = event['args']['nonce']
    signature = event['args']['signature']

    # prepare transaction to mint tokens on BridgeBsc contract
    tx = bridge_bsc.functions.mint(from_address, to_address, amount, nonce, signature)
    gas_price = web3_bsc.eth.gas_price
    gas_cost = tx.estimateGas({'from': admin_address})
    data = bridge_bsc.encodeABI('mint', [from_address, to_address, amount, nonce, signature])
    tx_data = {#tx.buildTransaction({
        'from': admin_address,
        'to': bridge_bsc_address ,  #bridge_bsc_address,
        'gas': gas_cost,
        'gasPrice': gas_price,
        'data': data
    }
    # send transaction and print receipt
    tx_hash = web3_bsc.eth.sendTransaction(tx_data)
    receipt = web3_bsc.eth.waitForTransactionReceipt(tx_hash)
    print(f'Transaction hash: {receipt.transactionHash}')

    # print processed transfer information
    print(f'Processed transfer:\n- from {from_address}\n- to {to_address}\n- amount {amount} tokens\n- date {date}\n- nonce {nonce}\n')

#bridge_eth.events.Transfer().on('data', handle_transfer_event)

async def log_loop(event_filter, poll_interval):
    while True:
        print('waiting for events...')
        #events = bridge_eth.events.Transfer().getLogs(fromBlock='latest')
        for PairCreated in event_filter.get_new_entries():
            print(PairCreated)
            handle_transfer_event(PairCreated)
        await asyncio.sleep(poll_interval)

event_filter = bridge_eth.events.Transfer.createFilter(fromBlock='latest')
    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(
        asyncio.gather(
            log_loop(event_filter, 2)))
            # log_loop(block_filter, 2),
            # log_loop(tx_filter, 2)))
finally:
    print('closing event loop')
    # close loop to free up system resources
    loop.close()