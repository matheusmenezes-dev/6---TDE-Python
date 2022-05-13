from datetime import datetime
import json
from hashlib import sha256


class Block:
    def __init__(self, index:int, prev_hash:str, transactions:list) -> None:
        self.index = index
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = str(datetime.now())

    @property
    def hash(self):
        encoded_obj = self.json.encode()
        rhash = sha256(encoded_obj)
        return rhash.hexdigest()
    
    @property
    def json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def from_dict(block):
       return Block(block["index"], block["prev_hash"], block["transactions"]) 
    