import unittest
import os
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
    
    def test_hashing(self):
        print(f"HASH: {self.block.hash}")
        self.assertEqual(1, 1)


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
        chain_path='blockchain/chains/tempchain.json'
        if os.path.isfile(chain_path): os.remove(chain_path)
        self.blockchain = BlockChain(chain_path=chain_path) 

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

    if __name__ == '__main__':
        unittest.main()