from blockchain_unit import Blockchain,Block
import time
import random
import copy
from termcolor import colored


#bc to others the new block using the user's id and
def change_chain(bc,id):
    global chain
    global current_chain

    global_chain,local_chain =  chain.chain_len(),bc.chain_len()
    if global_chain <local_chain:
        chain= copy.deepcopy(bc)
        current_chain_id = id
        print("chain replaced by user:",id)
        print("chain lenght:",bc.chain_len(),"chain owner" ,current_chain_id )
    else :
        print("falied to replace the chain with user:",id)


names= ["Mohamed", "Ahmed", "Mahmoud", "Ziad", "Abdelrahman", "Amr", "Omar", "Karim", "Ali", "Ibrahim"]
chain = Blockchain(4)
current_chain_id =0
blocks = []

for n in range(9):
    temp = Block("")
    k = random.randint(1,4)
    for z in range (k):
        while (1):
            i,j = random.randint(0,9),random.randint(0,9)
            Amount = random.randint(1,9)*10
            if i != j :
                temp.add_transaction(names[i]+" pays " + names[j]+ " "+ str(Amount) + "$")
                break
    blocks.append(copy.deepcopy(temp))

miner_chain = copy.deepcopy(chain)
attacker_chain = copy.deepcopy(chain)
#number of blocks in each 
attacker_index = miner_index = 0
while (len(blocks)>miner_index and len(blocks)>attacker_index ):
    # Mining (computaion power)
    miner_chance = attacker_chance = random.randint(1,100) 
    if miner_chance >0 and miner_chance <40 :

        miner_chain.mine(blocks[miner_index])
        change_chain(miner_chain,0)
        miner_index += 1

    if attacker_chance >41 and attacker_chance<101:
        attacker_chain.mine(Block("attack"+str (attacker_index)))
        change_chain(attacker_chain, 1)
        attacker_index += 1


print(colored('**********************************************************\nCURRENT VALID CHAIN ', 'blue', attrs=['bold']))
chain.print_chain()

print(colored('**********************************************************\nMINER CHAIN ', 'blue', attrs=['bold']))
miner_chain.print_chain()
print(colored('**********************************************************\nATTACKER CHAIN ', 'red', attrs=['bold']))
attacker_chain.print_chain()