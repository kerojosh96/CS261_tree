import unittest
from bst import BinarySearchTreeNode
from test_bst import TestBinarySearchTree

bb = TestBinarySearchTree()
bb.test_insert_Root(50)
bb.test_insert_Root(6)
bb.test_insert_Root(56)
bb.test_insert_Root(23)
bb.test_insert_Root(2)
bb.test_insert_Root(200)
bb.test_insert_Root(59)
bb.test_insert_Root(125)
bb.test_insert_Root(126)
#bb.callInorder()
print("calling Post Order")
bb.callPostorder()
print("calling In Order")
bb.callInorder()
print(str(bb.NumberOfNodes)+" number of nodes" )
bb.call_find(56)
bb.call_find(59)

#bb.call_find(46)
#bb.call_deletion(200)
