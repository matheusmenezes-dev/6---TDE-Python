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
        self.new = False
        self.blockchain = BlockChain(self.new)
        self.test_wallet1 = Wallet()
        self.old_wallet = """
        657f3e19eaa2eb029897f6bd35f57a0f9aae64cdf94741bef3296d5fb66ea145:b5c367db2773ba95b1a7b00ae7bbb0bfa5bcbecf842c3b85dfda07ab98d95cde
        """
    
    def test_add_transaction(self):
        if self.new: self.skipTest()
        self.blockchain.add_transaction(self.old_wallet, self.test_wallet1.public_key, 10)
        self.blockchain.create_block()
        self.assertEqual(self.blockchain.check_balance(self.test_wallet1.public_key), 10)

    def test_new_blockchain(self):
        if not self.new: self.skipTest()

        self.blockchain.add_transaction(
            sender=self.blockchain.genesis_wallet.key_pair,
            recipient=self.test_wallet1.public_key,
            amount=10)
        self.blockchain.create_block()

        self.assertEqual(self.blockchain.check_balance(self.test_wallet1.public_key), 10)
        self.assertEqual(
            self.blockchain.check_balance(self.blockchain.genesis_wallet.public_key), 90)

    def test_chain(self):
       pass 
        
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
