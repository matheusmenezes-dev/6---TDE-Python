from blockchain.wallet import Wallet
from blockchain.block import Block
import json

class BlockChain:
    def __init__(self, new=False) -> None:
        self.__pending_transactions = []
        if new: 
            self.genesis_wallet = Wallet()
            # Bloco Genesis
            self.genesis_block = Block(0, None, [{"sender": "master", "recipient": self.genesis_wallet.public_key, "amount": 100}])
            self.append_to_chain(self.genesis_block)
    
    @property
    def last_block(self):
        return self.chain[-1]
        
    @property
    def pending_transactions(self):
        return self.__pending_transactions

    def add_transaction(self, sender:str, recipient:str, amount:int):
        self.__pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount     
        })
    
    def check_balance(self, wallet:str) -> int:
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["sender"] == wallet:
                   balance -= transaction["amount"]
                if transaction["recipient"] == wallet:
                   balance += transaction["amount"]
        return balance
    
    def verify_transaction(self, transaction) -> bool:
        if not Wallet.verify(transaction["sender"]): 
            return False
        sender_wallet = Wallet(transaction["sender"])
        sender_balance = self.check_balance(sender_wallet.public_key)
        if sender_balance < transaction["amount"]: return False
        if transaction["amount"] <= 0: return False

        # Removendo a private key antes de salvar na blockchain
        # Essa parte não me pareceu segura nem otimizada. Necessita uma solução melhor
        transaction["sender"] = sender_wallet.public_key 
        return True                                      
        
    def create_block(self):
        index = self.last_block.index + 1
        prev_hash = self.last_block.hash
        transactions = [transaction for transaction in self.__pending_transactions
            if self.verify_transaction(transaction)]  
        block = Block(index=index, prev_hash=prev_hash, transactions=transactions)
        self.append_to_chain(block)
         
    def serialize_chain(self):
        json_chain = [block.__dict__ for block in self.__chain]
        with open('blockchain/blocks.json', 'w') as f:
            print(len(json_chain))
            json.dump(json_chain, f)
    
    @property
    def chain(self):
        with open('blockchain/blocks.json', 'r') as f:
            serialized_chain = json.load(f)
            return [Block(block["index"], block["prev_hash"], block["transactions"]) for block in serialized_chain]
    
    def append_to_chain(self, block:Block):
        self.__chain = self.chain
        self.__chain.append(block)
        self.serialize_chain()
          