import hashlib
import datetime as date

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = "We are going to encode this string of data!".encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.current_data = ''

    def create_genesis_block(self):
        return Block(date.datetime.now(), 'Genesis Block', '0')

    def add_block(self, data):
        if data is None or data == '':
            print('Error: nullable data is not allowed')
            return
        timestamp = date.datetime.now()
        previous_hash = self.get_latest_block().hash
        new_block = Block(timestamp, data, previous_hash)
        self.chain.append(new_block)
        self.current_data = ''

    def get_latest_block(self):
        return self.chain[-1]

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
my_blockchain = Blockchain()

my_blockchain.add_block('This is the first block')
my_blockchain.add_block('This is the second block')
my_blockchain.add_block('This is the third block')

for block in my_blockchain.chain:
    print(f"Timestamp: {block.timestamp} \r\nData:{block.data} \r\nHash: {block.hash} \r\nPrevious Hash:{block.previous_hash} ")
    print("="*100)

# Test Case 2
my_blockchain = Blockchain()

my_blockchain.add_block(None)
assert len(my_blockchain.chain) == 1

my_blockchain.add_block('')
assert len(my_blockchain.chain) == 1

for block in my_blockchain.chain:
    print(f"Timestamp: {block.timestamp} \r\nData:{block.data} \r\nHash: {block.hash} \r\nPrevious Hash:{block.previous_hash} ")
    print("="*100)

# Test Case 3
my_blockchain = Blockchain()

large_data = 'a' * 1000
my_blockchain.add_block(large_data)

assert len(my_blockchain.chain) == 2

for block in my_blockchain.chain:
    print(f"Timestamp: {block.timestamp} \r\nData:{block.data} \r\nHash: {block.hash} \r\nPrevious Hash:{block.previous_hash} ")
    print("="*100)