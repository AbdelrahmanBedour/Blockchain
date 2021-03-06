import datetime
import hashlib
import numpy as np


class Block:
    blockNo = 0
    data = None
    next = None
    nonce = np.uint64(0)
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def add_transaction(self,trans):
        if len(self.data)==0:
            self.data = self.data + trans
        else:
            self.data = self.data + '\n'+trans

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
        return "Previous Hash: "+ str (self.previous_hash) + "\nBlock Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nNonce: " + str(int(self.nonce)) + "\n--------------"
