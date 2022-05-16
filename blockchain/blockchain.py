from blockchain.wallet import Wallet
from blockchain.block import Block
import json
import os

class BlockChain:
    def __init__(self, chain_path) -> None:
        self.__chain_path = chain_path
        self.__pending_transactions = []
        # Inicializa uma nova blockchain caso a blockchain indicada
        # ainda não exista
        if not os.path.isfile(self.__chain_path):
            self.genesis_wallet = Wallet()
            self.__genesis_block = Block(index=0, previous_hash=None, transactions=[{
                "sender": "master",
                "recipient": self.genesis_wallet.public_key,
                "amount": 100
                }])
            with open(self.__chain_path, 'w') as f:
               json.dump([self.__genesis_block.__dict__], f) 
    
    @property
    def last_block(self) -> Block:
        return self.blocks[-1]
    
    @property
    def genesis_block(self) -> Block:
        return self.blocks[0]
        
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
        for block in self.blocks:
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
        previous_hash = self.last_block.hash
        transactions = [transaction for transaction in self.__pending_transactions
            if self.verify_transaction(transaction)]  
        block = Block(index=index, previous_hash=previous_hash, transactions=transactions)
        self.append_to_blocks(block)
        self.__pending_transactions = []
         
    def serialize_blocks(self):
        blocks = [block.__dict__ for block in self.__blocks]
        with open(self.__chain_path, 'w') as f:
            json.dump(blocks, f)
    
    @property
    def blocks(self):
        with open(self.__chain_path, 'r') as f:
            serialized_blocks = json.load(f)
            return [Block.from_dict(block) for block in serialized_blocks]
    
    def append_to_blocks(self, block:Block):
        self.__blocks = self.blocks
        self.__blocks.append(block)
        self.serialize_blocks()
    
    @property
    def is_valid(self):
        last_block_hash = self.genesis_block.hash 
        for block in self.blocks:
            # Desconsideramos o genesis_block (indice 0)
            if block.index:
                if block.previous_hash != last_block_hash:
                    return False
                last_block_hash = block.hash
        return True