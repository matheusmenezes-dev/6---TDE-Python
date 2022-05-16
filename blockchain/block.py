from datetime import datetime
import json
from hashlib import sha256


class Block:
    def __init__(self, index:int, previous_hash:str, transactions:list, timestamp:datetime=None) -> None:
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = str(datetime.now()) if not timestamp else timestamp 

    @property
    def hash(self):
        encoded_obj = self.json.encode()
        rhash = sha256(encoded_obj)
        return rhash.hexdigest()
    
    @property
    def json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def from_dict(block:dict):
       return Block(block["index"], block["previous_hash"], block["transactions"], block["timestamp"]) 
    