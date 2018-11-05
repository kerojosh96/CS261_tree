# run with python -m unittest test_bst
#Josh Cook
import unittest
from bst import BinarySearchTreeNode

class TestBinarySearchTree(unittest.TestCase):
    def __init__(self):
        self.root = None
        self.NumberOfNodes = 0
                
    def test_instantiation(self): 
        try:
            BinarySearchTreeNode()#instantiates bst class
        except NameError():
            self.fail("could not instantiate Binary Search")
    
    def test_initial_value(self,val):
        bst = BinarySearchTreeNode(val)
        #self.assertEqual(10, bst.value)
        print(bst.getVal())
        print("hello accessing function")

    def test_insert_Root(self,newVal):
        self.NumberOfNodes = self.NumberOfNodes + 1
        print(self.root)
        if self.root == None:
            self.root = BinarySearchTreeNode(newVal)
            print(self.root.value)
        else:
            self.test_insert_Nonroot(newVal,self.root)

         
        
  
    def test_insert_Nonroot(self,newVal,currentNode): # puts values in their proper order
        
        if currentNode.value > newVal: # checks if the current node is greater then the new value
            if currentNode.left == None:
                currentNode.left = BinarySearchTreeNode(newVal) #adds a new node to current's left
                currentNode.left.parent = currentNode
            else:
                self.test_insert_Nonroot(newVal,currentNode.left)# this goes to the next left value
        else:
            if currentNode.value < newVal: # checks to see if current Node is greater than the new val
                if currentNode.right == None:
                    currentNode.right = BinarySearchTreeNode(newVal)
                    currentNode.right.parent = currentNode
                else:
                    self.test_insert_Nonroot(newVal,currentNode.right)
        
    
    def inorderTrav(self,currentNode):#traverses 
        if currentNode == None:
            pass
        else:
            self.inorderTrav(currentNode.left)
            print(str(currentNode.value))
            self.inorderTrav(currentNode.right)

    def callInorder(self): #calls inorderTrav
        if self.root !=None:
            self.inorderTrav(self.root)
    def postOrder(self,currentNode):
        
        if currentNode!= None:
            self.postOrder(currentNode.left)
            self.postOrder(currentNode.right)
            print(str(currentNode.value))

    def callPostorder(self): #calls inorderTrav
        if self.root !=None:
            self.postOrder(self.root) 

    def how_many_nodes():
        return self.NumberOfNodes()

    def has_left(self,currentNode):
        if currentNode.left != None:
            return True

    def has_right(self,currentNode):
        if currentNode.right !=None:
            return True

    def getParent(self,currentNode):
        if currentNode != None:
            return self.parent

    def is_it_a_leaf(self,currentNode):
        if currentNode.left == None and currentNode.right == None:
            return True

    def get_node_left(self,currentNode):
        return currentNode.left.value
    
    def find(self,value,currentNode,Deleting=False):
        if currentNode.value == value:
            if Deleting == False: # reuses the function for deletion 
                print("Found "+ str(currentNode.value))

            return currentNode
        elif currentNode.value > value and self.has_left(currentNode):
            return self.find(value,currentNode.left)
            
        elif currentNode.value < value and self.has_right(currentNode):
            return self.find(value,currentNode.right)
        
    def call_find(self,SearchNumber,Deleting=False): 
        if self.root == None:
            print("There are no Nodes.This is an empty tree.")
            
            return None
        else:
            return self.find(SearchNumber,self.root,Deleting)
    
    def Deletion(self,SearchNumber,currentNode): # doesnt work
        a = self.call_find(SearchNumber,True)
        if a == self.is_it_a_leaf(currentNode):
            print("this is a leaf")
        
           
    def call_deletion(self,searchNumber): # doesnt work
        return self.Deletion(searchNumber,self.call_find(searchNumber))



if __name__ == '__main__':
    #unittest.main()
    
    pass
    #need test_



 
