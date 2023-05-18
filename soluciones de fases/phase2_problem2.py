from bst import BinarySearchTree
from bintree import BinaryTree, BinaryNode
import bintree as b


### auxiliary functions


def get_descendant_k(node: BinaryNode, level: int, k: int, lst: list) -> None:
    """adds to lst, all descendant nodes from node with a distance k"""
    if level > k:
        return
    if node is not None:
        if level == k:
            lst.append(node.elem)
            return

        get_descendant_k(node.left, level + 1, k, lst)
        get_descendant_k(node.right, level + 1, k, lst)


def get_ancestors(current_node: BinaryNode, e: int, lst: list) -> None:
    """adds all ancestors for e,
    Complejidad depth del nodo. Peor caso, altura del árbol.
    O(log n) si el árbol está equilibrado (+ o -)"""
    if current_node:
        if e == current_node.elem:
            # we just found it, stop the search
            return

        lst.append(current_node.elem)
        if e < current_node.elem:
            get_ancestors(current_node.left, e, lst)
        else:
            get_ancestors(current_node.right, e, lst)

        print (lst)

class BST2(BinarySearchTree):
    def find_dist_k(self, e: int, k: int) -> list:
        """return all elements with a distance of k to e"""

        if not isinstance(k, int) or k < 0:
            print(k, " must be integer and k>=0")
            return []

        # search the node
        node = self.search(e)       # O(log n)
        if node is None:
            print(e, " does not exist")
            return []

        result = []
        # first, save the descendant from node with a distance of k
        get_descendant_k(node, 0, k, result)    # O(log n)

        # print("descendants from ", e, result)
        # gets all ancestors of e from root,
        # the list contains the path from root to the parent of e
        path2e = []
        get_ancestors(self.root, e, path2e)     # O(log n)
        # print("ancestors:", path2e)
        depth2e = self.depth(node)              # O(log n)
        # the first ancestor (root) has distance == depth(node) to e
        # Complejidad del bucle, log n * log n
        for anc in path2e:
            if depth2e == k:
                result.append(anc)
            elif depth2e < k:
                node_ancestor = self.search(anc)
                if e < anc:
                    get_descendant_k(node_ancestor.right, 1, k-depth2e, result)
                elif e > anc:
                    get_descendant_k(node_ancestor.left, 1, k-depth2e, result)
            depth2e -= 1

        return result


if __name__ == "__main__":

    input_tree = BST2()
    #data = [14, 11, 18, 10, 13, 16, 19, 5, 12, 15, 17, 30, 4, 6, 29, 31, 2, 8, 24, 33, 1, 3, 7, 9, 23, 25, 32, 34, 21, 27, 36, 20, 22, 26, 28, 35, 37]
    data = [50, 25, 30, 60, 20, 5, 31, 23, 65, 22, 28]
    for x in data:
        input_tree.insert(x)
    input_tree.draw()
    x = 30
    # for d in [0, 1, 2]:
    #   print("find_dist_k({},{})={}".format(x, d, input_tree.find_dist_k(x, d)))
    d = 2
    print("find_dist_k({},{})={}".format(x, d, input_tree.find_dist_k(x, d)))

    """
    x = 25
    dist = 0
    print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 1
    print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 2
    print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 3
    print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    """
    """
    x = 20
    # dist = 0
    # print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    # dist = 1
    # print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 2
    print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))

    dist = 3
    print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 4
    print("find_dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    """
