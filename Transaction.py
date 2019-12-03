# `pc_transaction.py` example
from bitcoin.rpc import RawProxy

import sys

p = RawProxy()

if len(sys.argv) != 2:
    print("Too many arguments or no transaction ID passed! ")
    sys.exit()

# Alice's transaction ID
txid = str(sys.argv[1])

# First, retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(txid)

# Decode the transaction hex into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx)

s = 0

for output in decoded_tx['vin']:
    vindex = output['vout']
    raw_New = p.getrawtransaction(output['txid'])
    decode_New = p.decoderawtransaction(raw_New)
    for index, outp in enumerate(decode_New['vout']):
        if index == vindex:
            s=outp['value'] + s
        
s2 = 0

for output in decoded_tx['vout']:
    s2+= output['value']

finalValue = s-s2

print(finalValue)
    