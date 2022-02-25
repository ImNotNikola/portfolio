import hashlib

class NeuralCoinBlock:
    
    def __init__(self, previousBlockHash, transactionList):
        self.previousBlockHash = previousBlockHash
        self.transactionList = transactionList

        self.blockData = "-".join(transactionList) + "-" + previousBlockHash
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()

t1 = "Ana sends 2 NeuralCoin to Mike"
t2 = "Bob sends 4.1 NeuralCoin to Mike"
t3 = "Mike sends 3.2 NeuralCoin to Bob"
t4 = "Daniel sends 0.3 NeuralCoin to Ana"
t5 = "Mike sends 1 NeuralCoin to Charlie"
t6 = "Mike sends 5.4 NeuralCoin to Daniel"

initialBlock = NeuralCoinBlock("Initial String", [t1, t2])

print(initialBlock.blockData)
print(initialBlock.blockHash)

secondBlock = NeuralCoinBlock(initialBlock.blockHash, [t3, t4])

print(secondBlock.blockData)
print(secondBlock.blockHash)

thirdBlock = NeuralCoinBlock(secondBlock.blockHash, [t5, t6])

print(thirdBlock.blockData)
print(thirdBlock.blockHash)
