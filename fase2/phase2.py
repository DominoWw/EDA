"""
Case #2. Exercise  3
@author: EDA Team
"""

# Classes provided by EDA Team
from dlist import DList
from bintree import BinaryNode
from bst import BinarySearchTree

class BST2(BinarySearchTree):
    def find_dist_k(self, n: int, k:int) -> list:
        if self._root:

            #checking whether exists simultaneously checking the depth
            N=self.search(n)
            if N:
                
                d=self.depth(N)
                L=[]
                self._parent_nodes(n, k, d, self._root, L, N)
                return L



            
            else:
                return []
            
        else:
            return []



    def _parent_nodes(self, n:int, k:int, d:int, node:BinaryNode, L:list, N:BinaryNode):
        if node==None:
            return
        elif node==N:
            
            self._list_elem(k-1, node.left, L)
            self._list_elem(k-1, node.right, L)

        
        
        #node is on the left-hand side of the tree
        elif node.elem > n:

            if k==d-self.depth(node):
                L.append(node.elem)
            
            else:
                self._list_elem(k- 1- (d-self.depth(node)), node.right, L)
            
            self._parent_nodes(n, k, d, node.left, L, N)

        
        elif node.elem < n:

            if k==d-self.depth(node):
               L.append(node.elem)
            
            else:
                self._list_elem(k- 1- (d-self.depth(node)), node.left, L)
            
            self._parent_nodes(n, k, d, node.right, L, N)
            
        
        

             





    #listing elements from the other side of the parent node
    #if x == 0 -> thats the element we are looking for, if grater than 0 -> we have to search children
    def _list_elem(self, x:int, node:BinaryNode, L:list):
        if node==None:
            return
        elif x==0:
            L.append(node.elem)
            return
        elif x>0:
            self._list_elem(x-1, node.left, L)
            self._list_elem(x-1, node.right, L)

        







def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    ...
    


# Some usage examples
if __name__ == '__main__':
    input_list = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]

    tree0=BST2()
    for x in input_list:
        tree0.insert(x)
    tree0.draw()




    input_list_01 = [5, 12, 2, 1, 3, 9]
    input_list_02 = [9, 3, 21]

    # Build and draw first tree
    tree1 = BST2()
    for x in input_list_01:
        tree1.insert(x)
    #tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    #tree2.draw()

    function_names = ["merge", "intersection", "difference"]


    '''
    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()
    '''


    X=tree0.find_dist_k(15,1)
    print(X)