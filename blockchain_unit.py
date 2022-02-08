from block_unit import Block


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