from base64 import encode
from datetime import datetime
import time
from hashlib import sha256

class Wallet:
    def __init__(self, key_pair=None, public_key=None, private_key=None):
        if key_pair:
            self.__public_key, self.__private_key = key_pair.split(':')
        elif public_key and private_key:
            self.__public_key, self.__private_key = public_key, private_key
        else:
            self.generate_keys()
        
    def generate_keys(self): 
        # Preciso de um metodo melhor para gerar as keys
        # utilizar ms para randomizar (mesmo procedimento do modulo random)
        # não é seguro suficiente para o funcionamento em produção
        salt = str(datetime.now()) + "a0d7jiL9jVmN8mOl4Rj"
        self.__private_key = sha256(salt.encode()).hexdigest()
        self.__public_key = sha256(self.private_key.encode()).hexdigest()
        time.sleep(0.1)
    
    @property
    def private_key(self):
        return self.__private_key

    @property
    def public_key(self):
        return self.__public_key
    
    @property
    def key_pair(self):
        return f"{self.public_key}:{self.private_key}"

    @staticmethod
    def verify(key_pair=None, public_key=None, private_key=None):
        if key_pair:
            try:
                public_key, private_key = key_pair.split(':')
            except:
                raise KeyError("Invalid key pair")
        return public_key == sha256(private_key.encode()).hexdigest()