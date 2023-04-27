# -*- coding: utf-8 -*-
# Implementation of Binary Tree
# A node only saves the references to its children

from slistH import SList


class BinaryNode:
    def __init__(self, elem: object,
                 node_left: 'BinaryNode' = None,
                 node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    def __eq__(self, other: 'BinaryNode') -> bool:
        """checks if two nodes (subtrees) are equal o not"""
        return other is not None and self.elem == other.elem and \
               self.left == other.left and self.right == other.right

    def __str__(self) -> str:
        return str(self.elem)


class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def __eq__(self, other_tree: 'BinaryTree') -> bool:
        """checks if two binary trees are equal o not"""
        return other_tree is not None and self._root == other_tree._root

    def size(self) -> int:
        """Returns the number of nodes"""
        return self._size(self._root)

    def _size(self, node: BinaryNode) -> int:
        """return the size of the subtree from node"""
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def height(self) -> int:
        """Returns the height of the tree"""
        return self._height(self._root)

    def _height(self, node: BinaryNode) -> int:
        """return the height of node"""
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))
        

    def min_elem(self) -> int:
            if self.size!=0:
                nodo=root
                while nodo.left is not None:
                    nodo=nodo.left
                return nodo.elem



    def max_elem(self) -> object:
        return self._max_elem(self._root)
    
    def _max_elem(self, node: BinaryNode) -> object:
        if node is None:
            return None
        elif node.right is None:
            return node
        else:
            return self._max_elem(node.right)





    def preorder(self) -> None:
        """prints the preorder (root, left, right) traversal of the tree"""
        # self.draw()
        print('Preorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._preorder(self._root)
        print()

    def _preorder(self, node: BinaryNode) -> None:
        """prints the preorder (root, left, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            print(node.elem, end=' ')  # end=' ' avoid new line
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder_list(self) -> list:
        """returns a list with the preorder traversal"""
        # self.draw()
        result = []
        self._preorder_list(self._root, result)
        return result

    def _preorder_list(self, node: BinaryNode, pre_list: list) -> None:
        """populates pre_list with the preorder traversal of the subtree node"""
        if node is not None:
            pre_list.append(node.elem)
            self._preorder_list(node.left, pre_list)
            self._preorder_list(node.right, pre_list)

    def postorder(self) -> None:
        """prints the postorder (left, right, root)  traversal of the tree"""
        # self.draw()
        print('Postorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._postorder(self._root)
        print()

    def _postorder(self, node: BinaryNode) -> None:
        """prints the postorder (left, right, root) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem, end=' ')  # end=' ' avoid new line

    def postorder_list(self) -> list:
        """returns a list with the postorder traversal of the tree"""
        # self.draw()
        result = []
        self._postorder_list(self._root, result)
        return result

    def _postorder_list(self, node: BinaryNode, post_list: list) -> None:
        """populates post_list with the postorder traversal of the subtree node"""
        if node is not None:
            self._postorder_list(node.left, post_list)
            self._postorder_list(node.right, post_list)
            post_list.append(node.elem)

    def inorder(self) -> None:
        """prints the inorder (left, root, right)  traversal of the tree"""
        # self.draw()
        print('Inorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._inorder(self._root)
        print()

    def _inorder(self, node: BinaryNode) -> None:
        """prints the inorder (left, root, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._inorder(node.left)
            print(node.elem, end=' ')  # end=' ' avoid new line
            self._inorder(node.right)

    def inorder_list(self) -> list:
        """returns a list with the inorder traversal of the tree"""
        # self.draw()
        result = []
        self._inorder_list(self._root, result)
        return result

    def _inorder_list(self, node: BinaryNode, in_list: list) -> None:
        """populates in_list with the inorder traversal of the subtree node"""
        if node is not None:
            self._inorder_list(node.left, in_list)
            in_list.append(node.elem)
            self._inorder_list(node.right, in_list)

    def level_order(self) -> None:
        """prints the level order of the tree. O(n)"""
        if self._root is None:
            print('tree is empty')
        else:
            print("Level order: ", end=' ')  # avoid the new line

            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.add_last(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.remove_first()
                print(current.elem, end=' ')
                if current.left is not None:
                    list_nodes.add_last(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.add_last(current.right)  # O(1)

            print()

    def level_order_list(self) -> list:
        """prints the level order of the tree. O(n)"""
        result = []
        if self._root is not None:
            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.add_last(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.remove_first()  # O(1)
                result.append(current.elem)
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.add_last(current.right)  # O(1)

        return result

    def depth(self, node):
        """ returns the depth of the node; this is the length from
        the root to the node"""

        if self._root is None:
            print('Error: the tree is empty')
        else:
            # we can use SList with tail and head
            depth_level = 0

            list_nodes = SList()
            list_nodes.add_last(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.remove_first()  # O(1)
                if current == node:
                    return depth_level
                if current.left is not None and node.elem < current.elem:
                    list_nodes.add_last(current.left)  # O(1)
                if current.right is not None and node.elem > current.elem:
                    list_nodes.add_last(current.right)  # O(1)
                depth_level += 1

        print('Not found ', node.elem)
        return None

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def sum_elems(self) ->object:
        return self._sum_elems(self._root)

    def _sum_elems(self, node:BinaryNode) -> object:
        if node is None:
            return 0
        else:
            return node.elem + self._sum_elems(node.right)+self._sum_elems(node.left)
        
    def new_func(self) -> int:
        return 0



    def getCount(self, low: int, up: int):
        if self._root:
            return self._getCount(self._root, low, up)
            
        else:
            return None

    def _getCount(self, node: BinaryNode, low:int, up:int):
        
        if node:
            if node.elem >low and node.elem < up:
                return 1 + self._getCount(node.left, low,up) + self._getCount(node.right,low,up)
            elif node.elem < low:
                return 0 + self._getCount(node.right,low,up)
            elif node.elem > up:
                return 0 + self._getCount(node.left,low,up)
            elif node.elem == low:
                return 1 + self._getCount(node.right,low,up)
            elif node.elem == up:
                return 1 + self._getCount(node.left,low,up)
        else:
            return 0


    def get_average_range(self, low:int, up:int):
        if self._root:
            l=[0,0]
            self._get_average_range(self._root, low, up, l)
            return l[0]/l[1]

        else:
            return 0            
    def _get_average_range(self, node: BinaryNode, low:int, up:int, l:list):
        if node:
            if node.elem >low and node.elem < up:
                l[0]+=node.elem
                l[1]+=1
                self._get_average_range(node.right,low,up,l)
                self._get_average_range(node.left,low,up,l)
            elif node.elem > up:
                self._get_average_range(node.left,low,up,l)
            elif node.elem < low:
                self._get_average_range(node.right,low,up,l)
            elif node.elem == low:
                l[0]+=node.elem
                l[1]+=1
                self._get_average_range(node.right,low,up,l)
            elif node.elem == up:
                l[0]+=node.elem
                l[1]+=1
                self._get_average_range(node.left,low,up,l)
    
    def _myfind(self, nodo: BinaryNode, x:int):
        if nodo == None:
            return False
        elif nodo.elem > x:
            return self._myfind(nodo.left, x)
        elif nodo.elem < x:
            return self._myfind(nodo.right, x)
        elif nodo.elem== x:
            return True
    
    def countPairs(self, otherTree, k:int):
        return self._countPairs(self._root, k)/2 + otherTree._countPairs(otherTree._root, k)/2
    
    def _countPairs(self, node:BinaryNode, k:int):
        if node==None:
            return 0
        elif node.elem>=k or node.elem == k/2:
            return 0 + self._countPairs(node.left, k)
        elif node.elem < k:
            find_x=k-node.elem
            if self._myfind(self._root, find_x):
                return 1 + self._countPairs(node.left,k) + self._countPairs(node.right, k)
            else:
                return 0 + self._countPairs(node.left,k) + self._countPairs(node.right, k)

    def lwc (self, a:int, b:int):
        if self._root:
            if b>a:
                return self._lwc(self._root, a,b)
            else:
                return self._lwc(self._root, b,a)
        else:
            return None
    def _lwc(self, node:BinaryNode, a:int, b:int):
        if node == None:
            return None
        elif node.elem>b:
            return self._lwc( node.left, a,b)
        elif node.elem < a:
            return self._lwc( node.right, a,b)
        elif node.elem >= a and node.elem <= b:
            if self._myfind1(self._root, a) and self._myfind1(self._root, b):
                return node.elem
            else:
                return None
        else:
            return None
    
    def _myfind1(self, nodo:BinaryNode, x:int):
        if nodo==None:
            return False
        elif nodo.elem == x:
            return True
        elif nodo.elem < x:
            return self._myfind1(nodo.right, x)
        elif nodo.elem > x:
            return self._myfind1(nodo.left, x)
        else:
            return False


    def is_zig_zag(self):
        if self._root:
            #0 - left, 1- right
            if self._is_zig_zag(self._root, self._root.left, self._root.right) or self._is_zig_zag(self._root, self._root.right, self._root.left):
                return True
        else:
            return False
        
    def _is_zig_zag(self, node:BinaryNode, x:BinaryNode, nx:BinaryNode):
        if node == None:
            return True
        elif x and nx==None:
            return True * self._is_zig_zag(node.right, x.right, x.left)
        else:
            return False


    def is_left_odd_right_even(self):
        if self._root: 
            return self._ilore(self._root.left, self._root.right)
        else:
            return False
        
    def _ilore(self, l:BinaryNode, r:BinaryNode):
        if l== None and r==None:
            return True
        elif l and r==None:
            if l.elem % 2 ==1:
                return True * self._ilore(l.left, l.right)
            else:
                return False
        elif l==None and r:
            if r.elem % 2 == 0:
                return True * self._ilore(r.left, r.right)
            else:
                return False
        elif l.elem%2 == 1 and r.elem%2 == 0:
            return True * self._ilore(l.left,l.right) * self._ilore(r.left, r.right)
        else:
            return False


    def is_same_shape(self, otherTree):
        if self._root ==None and otherTree._root == None:
            return False
        elif self._root and otherTree._root:
            if self._iss(self._root, otherTree._root):
                return True
            else:
                return False
        else:
            return False
        
    def _iss(self, node:BinaryNode, onode:BinaryNode):
        if node == None and onode== None:
            return True
        elif node and onode:
            return True and self._iss(node.left, onode.left) and (node.right, onode.right)
        else:
            return False



    def sumInsideRange(self, min:int, max:int) -> int:
        if self._root and min <=max:
            return self._isr(self._root, min, max)
        else:
            return None
    
    def _isr(self, node:BinaryNode, min: int, max: int) -> int:
        if node == None:
            return 0
        elif node.left== None and node.right == None:
            return 0
        elif node.elem < min:
            return 0 + self._isr(node.left, min, max)
        elif node.elem > max:
            return 0 + self._isr(node.right, min, max)
        else:
            return node.elem + self._isr(node.left, min, max) + self._isr(node.right, min, max)




#list            
'''
def find_first_last(l:list, x:int):
    return [ff(l, x), fl(l, x)]
def ff(l:list, x:int):
    if len(l) > 0 and l[0]==x:
        return 0
    elif len(l)>0 and l[0]!=x:
        return 1+ ff(l[1:], x)
    else:
        return -1
    

def fl(l:list, x:int):
    if len(l) > 0 and l[-1] == x:
        return len(l)
    elif len(l)>0 and l[-1] != x:
        llen=len(l)
        return 0 + fl(l[:llen-2],x)
    else:
        return -1
   '''







if __name__ == '__main__':
    tree = BinaryTree()
    newNode = BinaryNode(2)
    left = BinaryNode(3, newNode, None)
    right = BinaryNode(9)
    right.left = BinaryNode(8)
    right.right = BinaryNode(20)
    rrNode = right.right
    rrNode.right = BinaryNode(30)

    root = BinaryNode(5, left, right)
    tree._root = root



    tree2 = BinaryTree()
    tr2m = BinaryNode(6)
    tr2n= BinaryNode(10,tr2m, None)
    tr3m=BinaryNode(4)
    
    tree2._root = BinaryNode(5, tr3m,tr2n)
    

    lev2 = BinaryNode(5)
    lev1 = BinaryNode(2, None, lev2)
    lev0 = BinaryNode(6, lev1, None)

    tree3 = BinaryTree()
    tree3._root = lev0
    #tree3.draw()
    #tree.draw()
   


    b17=BinaryNode(17)
    b20=BinaryNode(20)
    b18=BinaryNode(18, b17, b20)
    b8=BinaryNode(8)
    b120=BinaryNode(120)
    b7=BinaryNode(7, b120, b8)
    b10=BinaryNode(10,b7,b18)
    tree4=BinaryTree()
    tree4._root=b10

    b16=BinaryNode(16)
    b19=BinaryNode(19)
    b17=BinaryNode(17, b16, b19)
    b6=BinaryNode(6)
    b5=BinaryNode(5, None, b6)
    b9=BinaryNode(9,b5,b17)



    tree.draw()
    tree5=BinaryTree()
    tree5._root=b9

    #tree4.draw()
    #tree5.draw()
    

    print(tree.sumInsideRange(4,21))


'''
    print("Iss: ",tree4.is_same_shape(tree5))
    
    print("t4 ilore:", tree4.is_left_odd_right_even())
    print("lwc: ", tree.lwc(5,30))
    print("is zig zag: ", tree.is_zig_zag())
    print("tree3 zig:", tree3.is_zig_zag())
    '''

#list
'''
    l1 = [-2,3,-2,3,0,1,2-1,-1,5]
    print (l1)
    print (find_first_last(l1,-1))
'''     
    #Show the tree
    
    #tree2.draw()
    

#main
'''
    print('pairs:', tree.countPairs(tree2, 11))

    print('tree 2 min: ', tree2.min_elem())

    print('min elem: ', tree.min_elem())

    print('max elem:', tree.max_elem())
    print('sum of elems: ', tree.sum_elems())

    print("Range: ", tree.getCount(5,8))
    print("AVR range: ", tree.get_average_range(1,11))




    # size, height
    print('Size of the tree:', tree.size())
    print('Height of the tree:', tree.height())
    print('root of the tree:', tree._height(root))
    print()

    # traversals
    tree.preorder()
    tree.postorder()
    tree.inorder()
    # save into a list
    print("Preorder: ", tree.preorder_list())
    print("Postorder: ", tree.postorder_list())
    print("Inorder: ", tree.inorder_list())
    tree.level_order()
    # save into a list
    print("Level order:", tree.level_order_list())
    print()

    # depth of some nodes
    print('depth of root:', tree.depth(root))
    print('depth of root.left:', tree.depth(left))
    print('depth of root.right:', tree.depth(right))
    print('depth of root.right.left:', tree.depth(right.left))
    print('depth of root.right.right.right:', tree.depth(rrNode.right), rrNode.right.elem)

'''



