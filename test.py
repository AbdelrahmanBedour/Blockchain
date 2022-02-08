from blockchain_unit import Blockchain,Block
import time
import random

names= ["Mohamed", "Ahmed", "Mahmoud", "Ziad", "Abdelrahman", "Amr", "Omar", "Karim", "Ali", "Ibrahim"]

chain = Blockchain(4)
time_lst = []

# Blocks Generation
for n in range(10):
    temp = Block("")
    k = random.randint(1,4)
    for z in range (k):
        while (1):
            i,j = random.randint(0,9),random.randint(0,9)
            Amount = random.randint(1,9)*10
            if i != j :
                temp.add_transaction(names[i]+" pays " + names[j]+ " "+ str(Amount) + "$")
                break

    # Mining
    start = time.time()
    chain.mine(temp)
    end = time.time()
    time_lst.append(end-start)
    # print(end - start,start,end)

# Print Chain
Temp_head = chain.head.next
i=0
while Temp_head != None:
    # print(blockchain.head.previous_hash)
    print(Temp_head)
    print (time_lst[i])
    i+=1
    Temp_head = Temp_head.next
print(time_lst)
print ('AVG Time Taken: ', sum(time_lst) / float(len(time_lst)))
# print(chain.head)