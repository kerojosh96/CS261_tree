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

    def test_insert_Call(self,newVal):
        self.NumberOfNodes = self.NumberOfNodes + 1
        print(self.root)
        if self.root == None:
            self.root = BinarySearchTreeNode(newVal)
            print(self.root.value)
        else:
            self.test_insert_Nonroot(newVal,self.root)
    def print_parent(self,currentNode):
        #print("Node "+ str(currentNode.value)+" has a parent of " +str(self.GetValue(currentNode.parent)))
        pass   
    def GetValue(self,currentNode):
        if currentNode == None:
            pass
        else:
            return currentNode.value

    def test_insert_Nonroot(self,newVal,currentNode): # puts values in their proper order
    
        if currentNode.value > newVal: # checks if the current node is greater then the new value
            if currentNode.left == None: # adds to the left side first 
                a = BinarySearchTreeNode(newVal)
                currentNode.left = a #adds a new node to current's left
                a.parent = currentNode
                self.print_parent(a)
                
                
            else:
                self.test_insert_Nonroot(newVal,currentNode.left)# this recurses to the next left value
        else:
            if currentNode.value < newVal: # checks to see if current Node is greater than the new val
                if currentNode.right == None:
                    b = BinarySearchTreeNode(newVal)
                    currentNode.right = b
                    b.parent = currentNode
                    self.print_parent(b)
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

    def is_it_a_leaf(self,currentNode):
        if currentNode.left == None and currentNode.right == None:
            return True
        else:
            return False
    def get_node_left(self,currentNode):
        return currentNode.left.value
    
    def find(self,value,currentNode,Deleting=False):
        if currentNode.value == value:

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
    def set_node_value(self,currentNode,newVal):
        currentNode.value = newVal
    def set_node_parent(self,currentNode,x):
        currentNode.parent = x
    def Get_Parent_Node(self,currentNode):
        return currentNode.parent
    def Get_Parent_Value(self,currentNode):
        return self.Get_Parent_Node(currentNode).value

    def set_node_left(self,currentNode,newVal):
        currentNode.left = newVal
    def set_node_right(self,currentNode,newVal):
        currentNode.right = newVal
    def child_is_left(self,currentNode):
       # print(" nodes left is "+ str(self.Get_Parent_Value(currentNode).left))
       pass

    def Deletion(self,SearchNumber,currentNode): 
        
        if self.is_it_a_leaf(currentNode):#looks for a leaf
        
            if self.GetValue(self.Get_Parent_Node(currentNode).left) != currentNode.value: # removes right leaf
           
             self.set_node_right(self.Get_Parent_Node(currentNode),None) 
             
            if self.GetValue(self.Get_Parent_Node(currentNode).left) == currentNode.value:# removes left leaf
            
             self.set_node_left(self.Get_Parent_Node(currentNode),None) 
        #........................... case 2 has 1 child
        elif self.is_it_a_leaf(currentNode) == False:# doesnt work

            if self.GetValue(currentNode.right) and currentNode.left == None:
                print("has 1 right child")
                Node_parent = currentNode.parent
                Node_child = currentNode.right
            if self.GetValue(currentNode.left) and currentNode.right == None:
                print("has 1 left child")
    def call_deletion(self,searchNumber): 
        return self.Deletion(searchNumber,self.call_find(searchNumber))



if __name__ == '__main__':
    #unittest.main()
    
    pass
    #need test_



 
