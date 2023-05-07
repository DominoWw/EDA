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
        #lets check whether the node exist
        N=self.search(n)
        if N:   
            L=[]
            #if the distance is 0, we are interested just in that particular node, so the placement does not matter
            if k==0:
                L.append(n)
            #if k is greater than 0, we have evaluate the whole tree
            else:
                #d is going to be used as depth of the searched node
                d=self.depth(N)
                #as the function will be comparing the values, distance, we provide that parameters,
                #apart from that, it will also check de depth difference - hence d
                #the funcion _parent_nodes is going to be used recursively on nodes - hence we provide a node (here root)
                #proper nodes' values are going to be placed in the list L, that is going to be returned at the end
                #for convenience, in order not to check the node with .search() function, we provide node N as well 
                self._parent_nodes(n, k, d, self._root, L, N)
            return sorted(L)
        else:
            return []


        #this function evaluates the subtrees starting with root and then proceeding in the direction of the N node
        #once it reaches N, calls a function listing elements for the last time and does not proceed further into the tree
    def _parent_nodes(self, n:int, k:int, d:int, node:BinaryNode, L:list, N:BinaryNode):
        if node==None:
            return

        #node is on the left-hand side of the subtree
        elif node.elem > n:
            #at first lets check whether this is the node we should list
            if k==d-self.depth(node):
                L.append(node.elem)
            #if not - we search for elements to be listed on the right-hand side of the subtree
            else:
                            #we decrease de declared distance in regard to the difference of depths od the nodes
                self._list_elem(k- (d-self.depth(node)), node.right, L)
            #either way, we proceed towards the wanted node    
            self._parent_nodes(n, k, d, node.left, L, N)

        #node is on the right hand side of the subtree
        elif node.elem < n:
            if k==d-self.depth(node):
               L.append(node.elem)
            else:
                self._list_elem(k- (d-self.depth(node)), node.left, L)
            self._parent_nodes(n, k, d, node.right, L, N)

        #once we found the node, the only thing that is left is to find elements in the subtree 
        elif node==N:
            self._list_elem(k, node.left, L)
            self._list_elem(k, node.right, L)
 
    
    #listing elements that are in a given distance from parent node
    #if x == 1 -> thats the element we are looking for, if grater than 1 -> we have to search children
    def _list_elem(self, x:int, node:BinaryNode, L:list):
        if node==None:
            return
        #if the distance is 1 - this is the element we are looking for
        # (we were searching for a node that is placed 1 -unit- from the origin node)
        elif x==1:
            L.append(node.elem)
            return
        elif x>1:
            #if the distance is greater than 1, we decrease it and proceed to search
            self._list_elem(x-1, node.left, L)
            self._list_elem(x-1, node.right, L)
        else:
            return
        



def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:

    #copy function for merge function
    def copy_tree(node:BinaryNode, output:BinarySearchTree) -> None:
        if node:
            output.insert(node.elem)
            copy_tree(node.left, output)
            copy_tree(node.right, output)

    #inner funcion intersection - recursive
    def intersection(node:BinaryNode, input_tree2:BinarySearchTree, output:BinarySearchTree) -> None:
        if node:
            if input_tree2.search(node.elem) != None:
                output.insert(node.elem)

            intersection(node.left, input_tree2, output)
            intersection(node.right, input_tree2, output)
            
    #inner funcion merge - recursive
    def merge(node:BinaryNode, output:BinarySearchTree) -> None:
        if node:
            if output.search(node.elem) == None:
                output.insert(node.elem)
            
            merge(node.left, output)
            merge(node.right, output)

    #inner funcion difference - recursive
    def difference(node:BinaryNode, input_tree2:BinarySearchTree, output:BinarySearchTree) -> None:
        if node:
            if input_tree2.search(node.elem) == None:
                output.insert(node.elem)

            difference(node.left, input_tree2, output)
            difference(node.right, input_tree2, output)

    output=BinarySearchTree()

    if opc == "merge":
        #we will add missing node from tree 1 to nodes from tree 2
        copy_tree(input_tree2._root, output)
        merge(input_tree1._root, output)

    elif opc == "intersection":
        intersection(input_tree1._root, input_tree2, output)

    elif opc == "difference":
        difference(input_tree1._root, input_tree2, output)
    
    #returning the output
    return output
    



    


# Some usage examples
if __name__ == '__main__':
    input_list = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
    
    task1 = [14,11,18,19,16,13,10,5,12,15,17,30,31,29,6,4,2,8,24,33,34,32,25,23,9,7,3,1,21,27,36,37,35,28,26,22,20]

    treeTask1=BST2()
    for x in task1:
        treeTask1.insert(x)
    #treeTask1.draw()


    tree0=BST2()
    for x in input_list:
        tree0.insert(x)
    #tree0.draw()

    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]



    input_list_01 = [5, 12, 2, 1, 3, 9]
    input_list_02 = [9, 3, 21]

    # Build and draw first tree
    tree1 = BST2()
    for x in input_list_01:
        tree1.insert(x)
    print("Tree 1: ")
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    print("Tree 2: ")
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    tree_output=create_tree(tree1, tree2, "merge")
    print("Output:")
    tree_output.draw()
    print("Tree 2 after merge: ")
    tree2.draw()


    '''
    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()
    '''


    # X=treeTask1.find_dist_k(30,5)
    # print(X)