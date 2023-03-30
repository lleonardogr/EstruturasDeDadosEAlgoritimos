import sys

import heapq
from collections import defaultdict

def huffman_encoding(data):
    if not data:
        return "", {}

    frequency = defaultdict(int)

    for symbol in data:
        frequency[symbol] += 1

    if len(frequency) == 1:
        tree = {symbol: '0' for symbol in frequency}
        encoded_data = "".join(tree[symbol] for symbol in data)
        return encoded_data, tree

    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huff_tree = heap[0]
    tree = {symbol: code for symbol, code in huff_tree[1:]}

    encoded_data = "".join(tree[symbol] for symbol in data)
    return encoded_data, tree

def huffman_decoding(encoded_data, tree):
    if not encoded_data or not tree:
        return ""

    decoded_data = []
    code = ""

    inv_tree = {v: k for k, v in tree.items()}

    for bit in encoded_data:
        code += bit
        if code in inv_tree:
            decoded_data.append(inv_tree[code])
            code = ""

    return "".join(decoded_data)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Nullable Test Case
data1 = ""
encoded_data1, tree1 = huffman_encoding(data1)
decoded_data1 = huffman_decoding(encoded_data1, tree1)
assert data1 == decoded_data1, f"Excpected: {data1}, Received: {decoded_data1}"

# Test Case 2
# Normal Test
data2 = "Huffman encoding and decoding example"
encoded_data2, tree2 = huffman_encoding(data2)
decoded_data2 = huffman_decoding(encoded_data2, tree2)
assert data2 == decoded_data2, f"Esperado: {data2}, Obtido: {decoded_data2}"

# Test case 3
# Long String
data3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
encoded_data3, tree3 = huffman_encoding(data3)
decoded_data3 = huffman_decoding(encoded_data3, tree3)
assert data3 == decoded_data3, f"Esperado: {data3}, Obtido: {decoded_data3}"

# Test Case 4
# One String Test
data4 = "a"
encoded_data4, tree4 = huffman_encoding(data4)
decoded_data4 = huffman_decoding(encoded_data4, tree4)
assert data4 == decoded_data4, f"Esperado: {data4}, Obtido: {decoded_data4}"

# Test Case 4
# Same letter String Test
data5 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
encoded_data5, tree5 = huffman_encoding(data5)
decoded_data5 = huffman_decoding(encoded_data5, tree5)
assert data5 == decoded_data5, f"Esperado: {data5}, Obtido: {decoded_data5}"
