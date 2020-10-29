# @Author Julius Alphonso
# Proof of Concept for Lookup trees

class Node:

    def __init__(self, letter, value=None):
        self.letter = letter
        self.value = value
        self.children = dict()


class LookupTree:

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.root = Node(None)


    def insert(self, string, value):
        temp = self.root
        for letter in string:
            if not letter in temp.children:
                temp.children[letter] = Node(letter)
            temp = temp.children[letter]
        temp.value = value

    def lookup(self, string):
        temp = self.root
        for letter in string:
            if letter in temp.children:
                temp = temp.children[letter]
            else:
                return None
        return temp.value

    def delete(self, string):
        temp = self.root
        for letter in string:
            if letter in temp.children:
                temp = temp.children[letter]
            else:
                return
        temp.value = None