# -*- coding: utf-8 -*-
"""
Test program comparing solutions with the builtin list-based one.

@author: EDA Team 6 / 85*
NIAs: 100502848 - 100451061
"""

# Classes provided by EDA Team
from bst import BinarySearchTree
from phase2 import BST2
from phase2 import create_tree
import unittest


#function for merging lists for unittests
def merge_lists(a:list, b:list) -> list:
    output=a.copy()

    for i in b:
        if i not in a:
            output.append(i)
    
    return sorted(output)

#function for finding intersection of lists for unittests
def intersection(a:list, b:list) -> list:
    output = [value for value in a if value in b]
    return sorted(output)

#function for finding difference of lists for unittests
def difference(a:list, b:list) -> list:
    output=[]
    for i in a:
        if i not in b:
            output.append(i)
    return sorted(output)

class Test(unittest.TestCase):
    def setUp(self):
        


        input_list_01 = [5, 12, 2, 1, 3, 9]
        input_list_02 = [9, 3, 21]
        input_list_03 = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
        input_list_04 = [14,11,18,19,16,13,10,5,12,15,17,30,31,29,6,4,2,8,24,33,34,32,25,23,9,7,3,1,21,27,36,37,35,28,26,22,20]

        self.lists=[input_list_01,input_list_02, input_list_03, input_list_04]
        
        
        self.tree1 = BST2()
        for x in input_list_01:
            self.tree1.insert(x)
        
        
        self.tree2 = BST2()
        for x in input_list_02:
            self.tree2.insert(x)



        self.tree3 = BST2()
        for x in input_list_03:
            self.tree3.insert(x)
    


        self.tree4 = BST2()
        for x in input_list_04:
            self.tree4.insert(x)
      

        #tree printing variable
        p=False        

        #print or not?
        if p:
            print("Tree 1: ")
            self.tree1.draw()
            
            print("Tree 2: ")
            self.tree2.draw()
            
            print("Tree 3: ")
            self.tree3.draw()
            
            print("Tree 4: ")
            self.tree4.draw()


       
        

       


        #Trees:

        #Merge
        self.tree1_2_M=create_tree(self.tree1, self.tree2, "merge")
        self.tree1_3_M=create_tree(self.tree1, self.tree3, "merge")
        self.tree1_4_M=create_tree(self.tree1, self.tree4, "merge")
        self.tree2_3_M=create_tree(self.tree2, self.tree3, "merge")
        self.tree2_4_M=create_tree(self.tree2, self.tree4, "merge")
        self.tree3_4_M=create_tree(self.tree3, self.tree4, "merge")


        #Intersection
        self.tree1_2_I=create_tree(self.tree1, self.tree2, "intersection")
        self.tree1_3_I=create_tree(self.tree1, self.tree3, "intersection")
        self.tree1_4_I=create_tree(self.tree1, self.tree4, "intersection")
        self.tree2_3_I=create_tree(self.tree2, self.tree3, "intersection")
        self.tree2_4_I=create_tree(self.tree2, self.tree4, "intersection")
        self.tree3_4_I=create_tree(self.tree3, self.tree4, "intersection")



        #Difference
        self.tree1_2_D=create_tree(self.tree1, self.tree2, "difference")
        self.tree1_3_D=create_tree(self.tree1, self.tree3, "difference")
        self.tree1_4_D=create_tree(self.tree1, self.tree4, "difference")

        self.tree2_1_D=create_tree(self.tree2, self.tree1, "difference")
        self.tree2_3_D=create_tree(self.tree2, self.tree3, "difference")
        self.tree2_4_D=create_tree(self.tree2, self.tree4, "difference")

        self.tree3_1_D=create_tree(self.tree3, self.tree1, "difference")
        self.tree3_2_D=create_tree(self.tree3, self.tree2, "difference")
        self.tree3_4_D=create_tree(self.tree3, self.tree4, "difference")

        self.tree4_1_D=create_tree(self.tree4, self.tree1, "difference")
        self.tree4_2_D=create_tree(self.tree4, self.tree2, "difference")
        self.tree4_3_D=create_tree(self.tree4, self.tree3, "difference")

    def test_test01(self):
        
        self.assertEqual(self.tree1.find_dist_k(9,4), [1,3], "Tree1 9-4 error")
        self.assertEqual(self.tree1.find_dist_k(5,0), [5], "Tree1 5-0 error")
        self.assertEqual(self.tree1.find_dist_k(2,1), [1,3,5], "Tree1 2-1 error")
        self.assertEqual(self.tree1.find_dist_k(5,2), [1,3,9], "Tree1 5-2 error")
        self.assertEqual(self.tree1.find_dist_k(5,7), [], "Tree1 5,7 error")
        self.assertEqual(self.tree1.find_dist_k(6,1), [], "Tree1 6-1 error")

        self.assertEqual(self.tree2.find_dist_k(9,1), [3,21], "Tree2 9-1 error")
        self.assertEqual(self.tree2.find_dist_k(9,0), [9], "Tree2 9-0 error")
        self.assertEqual(self.tree2.find_dist_k(9,4), [], "Tree2 9-4 error")
        self.assertEqual(self.tree2.find_dist_k(8,0), [], "Tree2 8-0 error")
        
        self.assertEqual(self.tree2.find_dist_k(21,1), [9], "Tree2 21-1 error")
        self.assertEqual(self.tree2.find_dist_k(3,2), [21], "Tree2 3-2 error")

        self.assertEqual(self.tree3.find_dist_k(50,3), [5,18,24,75], "Tree3 50,3 error")
        self.assertEqual(self.tree3.find_dist_k(50,0), [50], "Tree3 50-0 error")
        self.assertEqual(self.tree3.find_dist_k(25,0), [25], "Tree3 25-0 error")
        self.assertEqual(self.tree3.find_dist_k(5,1), [15], "Tree3 5-1 error")
        self.assertEqual(self.tree3.find_dist_k(20,2), [5,18,24,55], "Tree3 20-2 error")
        self.assertEqual(self.tree3.find_dist_k(60,4), [15,25], "Tree3 60,4 error")
        self.assertEqual(self.tree3.find_dist_k(80,0), [80], "Tree3 80-0 error")
        self.assertEqual(self.tree3.find_dist_k(5,7), [80], "Tree3 5-7 error")

        self.assertEqual(self.tree4.find_dist_k(30,0), [30], "Tree4 30-0 error")
        self.assertEqual(self.tree4.find_dist_k(30,2), [18,24,33], "Tree4 30-2 error")
        self.assertEqual(self.tree4.find_dist_k(12,6), [2,8,15,17,30], "Tree4 12-6 error")
        self.assertEqual(self.tree4.find_dist_k(17,7), [4,6,23,25,32,34], "Tree4 17-7 error")
        self.assertEqual(self.tree4.find_dist_k(26,9), [11,15,17,36], "Tree4 26-9 error")

    def test_test02(self):

        #Merge
        self.assertEqual(self.tree1_2_M.inorder_list(), merge_lists(self.lists[0], self.lists[1]), "Tree 1 - 2 - Merge")
        self.assertEqual(self.tree1_3_M.inorder_list(), merge_lists(self.lists[0], self.lists[2]), "Tree 1 - 3 - Merge")
        self.assertEqual(self.tree1_4_M.inorder_list(), merge_lists(self.lists[0], self.lists[3]), "Tree 1 - 4 - Merge")
        self.assertEqual(self.tree2_3_M.inorder_list(), merge_lists(self.lists[1], self.lists[2]), "Tree 2 - 3 - Merge")
        self.assertEqual(self.tree2_4_M.inorder_list(), merge_lists(self.lists[1], self.lists[3]), "Tree 2 - 4 - Merge")
        self.assertEqual(self.tree3_4_M.inorder_list(), merge_lists(self.lists[2], self.lists[3]), "Tree 3 - 4 - Merge")

        #Intersection
        self.assertEqual(self.tree1_2_I.inorder_list(), intersection(self.lists[0], self.lists[1]), "Tree 1 - 2 - Intersection")
        self.assertEqual(self.tree1_3_I.inorder_list(), intersection(self.lists[0], self.lists[2]), "Tree 1 - 3 - Intersection")
        self.assertEqual(self.tree1_4_I.inorder_list(), intersection(self.lists[0], self.lists[3]), "Tree 1 - 4 - Intersection")
        self.assertEqual(self.tree2_3_I.inorder_list(), intersection(self.lists[1], self.lists[2]), "Tree 2 - 3 - Intersection")
        self.assertEqual(self.tree2_4_I.inorder_list(), intersection(self.lists[1], self.lists[3]), "Tree 2 - 4 - Intersection")
        self.assertEqual(self.tree3_4_I.inorder_list(), intersection(self.lists[2], self.lists[3]), "Tree 3 - 4 - Intersection")

        #Difference
        self.assertEqual(self.tree1_2_D.inorder_list(), difference(self.lists[0], self.lists[1]), "Tree 1 - 2 - Difference")
        self.assertEqual(self.tree1_3_D.inorder_list(), difference(self.lists[0], self.lists[2]), "Tree 1 - 3 - Difference")
        self.assertEqual(self.tree1_4_D.inorder_list(), difference(self.lists[0], self.lists[3]), "Tree 1 - 4 - Difference")

        self.assertEqual(self.tree2_1_D.inorder_list(), difference(self.lists[1], self.lists[0]), "Tree 2 - 1 - Difference")
        self.assertEqual(self.tree2_3_D.inorder_list(), difference(self.lists[1], self.lists[2]), "Tree 2 - 3 - Difference")
        self.assertEqual(self.tree2_4_D.inorder_list(), difference(self.lists[1], self.lists[3]), "Tree 2 - 4 - Difference")

        self.assertEqual(self.tree3_1_D.inorder_list(), difference(self.lists[2], self.lists[0]), "Tree 3 - 1 - Difference")
        self.assertEqual(self.tree3_2_D.inorder_list(), difference(self.lists[2], self.lists[1]), "Tree 3 - 2 - Difference")
        self.assertEqual(self.tree3_4_D.inorder_list(), difference(self.lists[2], self.lists[3]), "Tree 3 - 4 - Difference")

        self.assertEqual(self.tree4_1_D.inorder_list(), difference(self.lists[3], self.lists[0]), "Tree 4 - 1 - Difference")
        self.assertEqual(self.tree4_2_D.inorder_list(), difference(self.lists[3], self.lists[1]), "Tree 4 - 2 - Difference")
        self.assertEqual(self.tree4_3_D.inorder_list(), difference(self.lists[3], self.lists[2]), "Tree 4 - 3 - Difference")


# Some usage examples
if __name__ == '__main__':
    unittest.main()
