"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

"""

class TrieNode:
    def __init__(self):
        self.children = {}

class WordDictionary(object):

    def __init__(self):
        self.root = {}

    def addWord(self, word):

        temp = self.root
        for char in word:
            if char in temp:
                temp = temp[char]
            else:
                temp[char] = {}
                temp = temp[char]
        temp['*'] = {}

    def search(self, word):

        def helper(trie, word, index):
            if index == len(word):
                if '*' in trie:
                    return True
                return False
            if word[index] == '.':
                for char in trie:
                    if helper(trie[char], word, index + 1):
                        return True
            elif word[index] in trie:
                if helper(trie[word[index]], word, index + 1):
                    return True
            return False
        return helper(self.root, word, 0)