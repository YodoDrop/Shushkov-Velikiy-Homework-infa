alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Node:
    def __init__(self):
        self.to = {}
        self.is_terminal = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, string):
        v = self.root
        for c in string:
            if c in v.to:
                v = v.to[c]
            else:
                new_v = Node()
                v.to[c] = new_v
                v = new_v
        v.is_terminal = True

    def build_trie(self, words):
        for word in words:
            self.add(word)

    def find(self, word):
        v = self.root
        for c in word:
            if c not in v.to:
                return False
            v = v.to[c]
        return v.is_terminal

    def remove(self, word):
        v = self.root
        for c in word:
            if c not in v.to:
                return False
            v = v.to[c]
        if not v.is_terminal:
            return False
        v.is_terminal = False
        return True


