## Square Root Calculation: 
This algorithm calculates the square root of a given number using binary search. The time complexity is O(log(n)) while the space complexity is O(1). The algorithm starts by checking the base cases for 0 and 1, and then initializing the lower and upper bounds for the search. It then proceeds to perform the binary search, comparing the square of the middle value to the target number, and updating the bounds accordingly.

## Rotated Sorted Array Search:

This algorithm searches for a target number in a rotated sorted array, with a time complexity of O(log(n)) and space complexity of O(1). The algorithm uses a modified binary search, where it first finds the pivot (the smallest element in the rotated array) and then performs a regular binary search on the appropriate sub-array based on the target value and pivot.

## Rearrange Array Digits:

This algorithm rearranges the digits in an input list of integers to form the largest and smallest possible numbers, with a time complexity of O(nlog(n)) and space complexity of O(n). The algorithm first sorts the input list, then creates two new lists for the largest and smallest numbers by alternatingly adding the sorted elements to each list. Finally, the largest and smallest numbers are formed by combining the digits in the respective lists.

## Dutch National Flag Problem: 

This algorithm sorts an array containing only 0s, 1s, and 2s, with a time complexity of O(n) and space complexity of O(1). It uses three pointers (low, mid, and high) to traverse the array and swap elements as needed, ensuring that all 0s are to the left, all 1s are in the middle, and all 2s are to the right.

## Trie and Suffixes: 

This algorithm implements a Trie data structure with methods for inserting words and finding suffixes. The time complexity for insertion and search is O(m), where m is the length of the word or prefix being inserted/searched, while the space complexity is O(n), where n is the total number of nodes in the Trie. The Trie is built by recursively adding TrieNode objects, which store the children nodes and a boolean value to indicate if it's the end of a word. The suffixes method retrieves all suffixes for a given prefix, returning a list of words.

## Route Trie and Router: 

This algorithm implements a routing system using a RouteTrie and a Router class. The time complexity for inserting and finding a path is O(m), where m is the length of the path, and the space complexity is O(n), where n is the total number of nodes in the Trie. RouteTrie is a specialized Trie that holds routes and their associated handlers. RouteTrieNode is similar to the TrieNode but has an additional handler attribute. The Router class wraps the RouteTrie, and it provides methods to add handlers, look up routes, and split paths into their components.