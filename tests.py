import unittest
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
        self.block = Block(index=1, prev_hash="abc123", transactions=mock_transactions)
    
    def test_hashing(self):
        print(f"HASH: {self.block.hash}")
        self.assertEqual(1, 1)

class TestBlockChain(unittest.TestCase):
    def setUp(self) -> None:
        self.blockchain = BlockChain(new=False)
        self.test_wallet1 = Wallet()
    
    def test_add_transaction(self):
        #self.blockchain.add_transaction(self.blockchain.genesis_wallet.key_pair, self.test_wallet1.public_key, 10)
        self.blockchain.add_transaction("6131559a8b2ec1f0d362aceb1466f9bb83f6d2ae9c455f531e59e7fcc0a2e132:db0faa01cdc7d92fe5e706232141d92077f7dbca29992f65559536897bc6d355", self.test_wallet1.public_key, 10)
        self.blockchain.create_block()
        self.assertEqual(self.blockchain.check_balance(self.test_wallet1.public_key), 10)
        #self.assertEqual(self.blockchain.check_balance(self.blockchain.genesis_wallet.public_key), 90)

    def test_deserialize(self):
        #self.blockchain.serialized_chain
        print(self.blockchain.last_block)
        
class TestWallet(unittest.TestCase):
    def test_verification(self):
        public_key = "56d9d295c2454bc077565f1f44a2787c20db9562282e88be0927e04f81e4568c"
        private_key = "f1c617680f107cc192b02f2270f4a2ca54fef3a3eabc206dc8ff93392171c82d"
        self.assertTrue(Wallet.verify(public_key=public_key, private_key=private_key))

    def test_key_pair_verification(self):
        wallet = Wallet()    
        self.assertTrue(Wallet.verify(wallet.key_pair))
    

    if __name__ == '__main__':
        unittest.main()
