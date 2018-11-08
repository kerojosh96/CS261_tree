import unittest
from bst import BinarySearchTreeNode
from test_bst import TestBinarySearchTree
def Create_test():
    print(" ")
    print(" ")
    bb = TestBinarySearchTree()
    bb.test_insert_Call(50)
    bb.test_insert_Call(6)
    bb.test_insert_Call(56)
    bb.test_insert_Call(23)
    bb.test_insert_Call(2)
    bb.test_insert_Call(200)
    bb.test_insert_Call(59)
    bb.test_insert_Call(125)
    bb.test_insert_Call(126)
    cc = TestBinarySearchTree()
    cc.test_insert_Call(200)
    cc.test_insert_Call(210)
    cc.test_insert_Call(190)

    cc.call_deletion(190) #deletes leaf
    cc.call_deletion(210) #deletes leaf
    print("calling Post Order")
    print(" ")
    bb.callPostorder()
    print("calling In Order")
    bb.callInorder()
    print(str(bb.NumberOfNodes)+" number of nodes" )
    bb.call_find(56)
   
    
Create_test()
