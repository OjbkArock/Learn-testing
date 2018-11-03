# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 20:08:08 2018

@author: Arock
"""

class Node:
    def __init__(self):
        self.value = None
        self.children = {}    # children is of type {char, Node}                                                                                                       

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key):      # key is of type string                                                                                                                
        # key should be a low-case string, this must be checked here!                                                                                                  
        node = self.root
        _list=[]
        for i in range(0,len(key),2):
            _list.append(key[i:i+2])
        for char in _list:
            if char not in node.children:
                child = Node()
                node.children[char] = child
                node = child
				
            else:
                node = node.children[char]
        node.value = key

    def search(self, key):
        node = self.root
        _list=[]
        for i in range(0,len(key),2):
            _list.append(key[i:i+2])
        for char in _list:
            if char not in node.children:
                return None
            else:
                node = node.children[char]
        return node.value

#    def display_node(self, node):
#        if (node.value != None):
#            print node.value
#        for char in :
#            if char in node.children:
#                self.display_node(node.children[char])
#        return
#
#    def display(self):
#        self.display_node(self.root)


T1=Trie()
with open("C:\Users\Arock\Desktop\words.dic","r") as file:
    lines=file.readlines()
    for line in lines:
        TStr=line.decode("utf-8")
#        print TStr
        T1.insert(TStr)
    s_str = "申论".decode("utf-8")
#    print type(s_str)
    print T1.search(s_str)
#for i in T1.root.children:
#    print i
#    print T1.root.children