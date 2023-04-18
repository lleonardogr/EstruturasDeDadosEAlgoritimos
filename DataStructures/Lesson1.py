class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def put(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
         if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.put(node)
            return node.value
         return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.put(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            del self.cache[self.tail.prev.key]
            self.remove(self.tail.prev)

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


assert our_cache.get(1) == 1       # returns 1
assert our_cache.get(2) == 2       # returns 2
assert our_cache.get(9) == -1      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

assert our_cache.get(3) == -1      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Test Cache LRU with null and empty values
cache1 = LRU_Cache(3)
cache1.set(1, None)
cache1.set(2, "")
cache1.set(3, "normal_value")
cache1.set(4, 4)  # Remove o elemento menos usado recentemente (1)

assert cache1.get(1) == -1  # Retorna -1, pois 1 foi removido
assert cache1.get(2) == ""  # Retorna ""
assert cache1.get(3) == "normal_value"  # Retorna "normal_value"

# Test Case 2
# Test Cache LRU with very large values
large_value = "A" * (10 ** 6)
cache2 = LRU_Cache(2)
cache2.set(1, large_value)
cache2.set(2, large_value)
cache2.set(3, large_value)  # Remove o elemento menos usado recentemente (1)

assert cache2.get(1) == -1  # Retorna -1, pois 1 foi removido
assert len(cache2.get(2)) >= 10**6  # Retorna o valor grande

# Test Case 3
# Teste da Cache LRU normal
cache3 = LRU_Cache(3)
cache3.set(1, 1)
cache3.set(2, 2)
cache3.set(3, 3)
cache3.set(4, 4)  # Remove o elemento menos usado recentemente (1)

assert cache3.get(1) == -1  # Retorna -1, pois 1 foi removido
assert cache3.get(2) == 2  # Retorna 2
assert cache3.get(3) == 3 # Retorna 3