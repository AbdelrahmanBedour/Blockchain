from block_unit import Block


class Blockchain:

    def __init__(self, x):
        self.diff=x*4
        self.maxNonce = 2 ** 64
        self.block = Block("Genesis")
        dummy = self.head = self.block
        self.target = 2 ** (256 - self.diff)
        for n in range(self.maxNonce):
            if int(self.block.hash(), 16) <= self.target:
                break
            else:
                self.block.nonce =self.block.nonce+ 1


    def Set_N (self,N):
        self.diff = N*4
        self.target = 2 ** (256 - self.diff)

    def is_valid_proof(self, block):
        if int(block.hash(), 16) <= self.target:
            return True
        else:
            return False

    def add(self, block):
        if block.previous_hash == self.block.hash() and self.is_valid_proof( block) :
            self.block.next = block
            self.block = self.block.next
    def chain_len(self):
        counter = 0
        temp_head = self.head

        while (temp_head != None):
            counter += 1
            temp_head = temp_head.next
        return counter

    def print_chain(self):
        Temp_head = self.head
        while Temp_head != None:
            # print(blockchain.head.previous_hash)
            print(Temp_head)
            Temp_head = Temp_head.next

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
