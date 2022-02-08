import datetime
import hashlib
import numpy as np
import time



class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = np.uint64(0)
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nNonce: " + str(int(self.nonce)) + "\n--------------"

class Blockchain:

    def __init__(self, x):
        self.diff=x*4
        self.maxNonce = 2 ** 64
        self.block = Block("Genesis")
        dummy = self.head = self.block
        self.target = 2**(256-self.diff)

    def Set_N (self,N):
        self.diff = N*4
        self.target = 2 ** (256 - self.diff)

    def add(self, block):
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                # print(block)
                break
            else:
                block.nonce =block.nonce+ 1

blockchain = Blockchain(4)
lst = []
for n in range(3):
    start = time.time()
    blockchain.mine(Block("Block " + str(n+1)))
    end = time.time()
    print(end - start)
    lst.append(end-start)
    # print(end - start,start,end)


blockchain.head = blockchain.head.next
i=0
while blockchain.head != None:

    # print(blockchain.head.previous_hash)
    print(blockchain.head)
    print (lst[i])
    i+=1

    blockchain.head = blockchain.head.next
print(lst)