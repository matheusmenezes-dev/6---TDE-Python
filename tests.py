from datetime import datetime
import unittest
import os
import json
from blockchain.block import Block
from blockchain.blockchain import BlockChain
from blockchain.wallet import Wallet

class TestBlock(unittest.TestCase):
    def setUp(self):
        mock_transactions = [
            {
               "sender": "Matheus",
               "receiver": "Jorge",
               "amount": 10 
            },
            {
               "sender": "Jorge",
               "receiver": "Matheus",
               "amount": 10 
            },
        ]
        self.block = Block(index=1, previous_hash="abc123", transactions=mock_transactions)


class TestWallet(unittest.TestCase):
    def test_verification(self):
        public_key = "56d9d295c2454bc077565f1f44a2787c20db9562282e88be0927e04f81e4568c"
        private_key = "f1c617680f107cc192b02f2270f4a2ca54fef3a3eabc206dc8ff93392171c82d"
        self.assertTrue(Wallet.verify(public_key=public_key, private_key=private_key))

    def test_key_pair_verification(self):
        wallet = Wallet()    
        self.assertTrue(Wallet.verify(wallet.key_pair))
    

class TestBlockChain(unittest.TestCase):
    def setUp(self) -> None:
        self.chain_path='blockchain/chains/tempchain.json'
        if os.path.isfile(self.chain_path): os.remove(self.chain_path)
        self.blockchain = BlockChain(chain_path=self.chain_path) 

    def test_new_chain(self):
        self.assertTrue(self.blockchain.last_block.hash, self.blockchain.blocks[0].hash)
    
    def test_transaction(self):
        recipient_wallet = Wallet()
        self.blockchain.add_transaction(
            self.blockchain.genesis_wallet.key_pair,
            recipient=recipient_wallet.public_key,
            amount=10)
        self.blockchain.create_block()
        self.assertEqual(self.blockchain.check_balance(recipient_wallet.public_key), 10)
        self.assertEqual(
            self.blockchain.check_balance(self.blockchain.genesis_wallet.public_key), 90)
        
    def test_verification(self):
        # Criamos multiplos blocos, e comparamos as hashes
        # atuais com as hashes previas inscritas nos blocos
        # o teste passa se a propriedade is_valid é: True para uma blockchain integra
        #                                            False para uma blockchain adulterada

        recipient_wallet = Wallet()
        for i in range(1, 10):
            self.blockchain.add_transaction(
                self.blockchain.genesis_wallet.key_pair,
                recipient=recipient_wallet.public_key,
                amount=1)
            self.blockchain.create_block()
            
        self.blockchain.create_block()
        self.assertTrue(self.blockchain.is_valid)
        
        # Adulteraremos a blockchain indevidamente e testaremos novamente,
        # dessa vez, esperando is_valid=False
        
        with open(self.chain_path, 'r') as f:
            blocks = json.load(f)
            bloco = blocks[0]
        # Alterando o timestamp da blockchain 
        bloco["timestamp"] = str(datetime.now())
        with open(self.chain_path, 'w') as w:
            json.dump(blocks, w)
        self.assertFalse(self.blockchain.is_valid)

    if __name__ == '__main__':
        unittest.main()