from bitcoin.rpc import RawProxy
from struct import pack, unpack, unpack_from
from binascii import unhexlify
import datetime, calendar
import sys
import hashlib
import binascii


p = RawProxy()

if len(sys.argv) != 2:
    print("Too many arguments or no block height passed!")
    sys.exit()

height = int(sys.argv[1])

blockHash = p.getblockhash(height)

block = p.getblock(blockHash)

version = block['version']
hashPrevBlock = block['previousblockhash'].decode('hex')
merkle = block['merkleroot'].decode('hex')
timestamp = block['time']
bits = block['bits']
nonce = block['nonce']

version = pack('<I', version).encode('hex_codec') 
hashPrevBlock = hashPrevBlock[::-1].encode('hex_codec')
merkle = merkle[::-1].encode('hex_codec')
timestamp = pack('<I', timestamp).encode('hex_codec')
bits = pack('<I', int(bits, 16)).encode('hex_codec') 
nonce = pack('<I', nonce).encode('hex_codec')


header = (version+hashPrevBlock+merkle+timestamp+bits+nonce)
headerByte = header.decode('hex')

hash = hashlib.sha256(hashlib.sha256(headerByte).digest()).digest()
hash = hash[::-1].encode('hex_codec')

if hash == blockHash:
    print("Hash is correct")
else:
    print("Hash is incorrect")
    