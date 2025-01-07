# Recursion Problems

# Part 1 is a collection of various problems solved with recursion. There are doctests accompanying 
# each function, and they can all be tested at the end of the document.

# Part 2 is an implementation of a binary search tree that utilizes recursion.



# ========= PART 1 ================


# This function determines if the second number "num" is an integer power of "base" greater than or equal to 0.
def is_power_of(base, num):
    """
        >>> is_power_of(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
        True
        >>> is_power_of(5, 1)    # pow(5, 0) = 1
        True
        >>> is_power_of(5, 5)    # pow(5, 1) = 5
        True
        >>> is_power_of(5, 15)   # 15 is not a power of 5 (it's a multiple)
        False
        >>> is_power_of(3, 9)
        True
        >>> is_power_of(3, 8)
        False
        >>> is_power_of(3, 10)
        False
        >>> is_power_of(1, 8)
        False
        >>> is_power_of(2, 0)    # 0 is not a power of any positive base.
        False
        >>> is_power_of(4, 16)
        True
        >>> is_power_of(4, 64)
        True
        >>> is_power_of(4, 63)
        False
        >>> is_power_of(4, 65)
        False
        >>> is_power_of(4, 32)
        False
    """
    if num == 1:     # Base case for True
        return True
    elif num == 0:   # 0 is not a power of any positive base
        return False
    elif base == 1:  # 1 is not the base of any number other than 1
        return False
    elif num % base == 0:
        return is_power_of(base, num // base)
    else:
        return False



# This function takes a list, and once it finds a negative number, it removes a corresponding number of 
# elements after the number, as well as the negative number itself. The absolute value of the negative 
# number determines the number of elements removed after the number.
def cut(a_list):
    """
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 1
        [5, 7, 6, 785, 5, 0, 42]
        >>> cut([1, 2, 3, -4, 0, 0, 0, 1, 1])
        [1, 2, 3, 1, 1]
	"""
    if len(a_list) == 1:    # If last digit (base case)
        if a_list[0] >= 0:
            return a_list
        else:
            return []
    else:
        if a_list[0] >= 0:
            return [a_list[0]] + cut(a_list[1:])
        else:
            x = -1 * a_list[0]
            try:
                return cut(a_list[x:])   # Removes the negative number and x-1 elements after the number
            except IndexError:           # If the negative digit tries to remove more items than there are left in the list
                return []



# This function replaces each number with the maximum number out of all of the numbers to the right of the number (and the number itself).
def right_max(num_list):
    """
        >>> right_max([3, 7, 2, 8, 6, 4, 5])
        [8, 8, 8, 8, 6, 5, 5]
        >>> right_max([1, 2, 3, 4, 5, 6])
        [6, 6, 6, 6, 6, 6]
        >>> right_max([1, 25, 3, 48, 5, 6, 12, 14, 89, 3, 2])
        [89, 89, 89, 89, 89, 89, 89, 89, 89, 3, 2]
    """
    if len(num_list) == 1:      # Base case
        return num_list
    elif num_list[-2] < num_list[-1]:    # When second-to-last num < last num, second-to-last num becomes the value of last num
        return right_max(num_list[:-2] + [num_list[-1]]) + [num_list[-1]]
    else:
        return right_max(num_list[:-1]) + [num_list[-1]]



# This function returns true if the number has consecutive digits, and returns false if it does not.
def consecutive_digits(num):
    """
        >>> consecutive_digits(2222466666678)
        True
        >>> consecutive_digits(12345684562)
        False
        >>> consecutive_digits(122)
        True
        >>> consecutive_digits(33)
        True
        >>> consecutive_digits(1002)
        True
        >>> consecutive_digits(1200)
        True
        >>> consecutive_digits(12000)
        True
        >>> consecutive_digits(12020202)
        False
    """
    if num < 10:      # Base case, and positive integers less than 10 cannot have consecutive digits
        return False
    elif num % 10 == (num // 10) % 10:  # Checks if last and second-to-last digits are the same
        return True
    else:
        return consecutive_digits(num // 10)


# This function returns only the even digits of a number. It returns 0 if the number only has odd digits.
def only_evens(num):
    """
        >>> only_evens(4386112)
        4862
        >>> only_evens(0)
        0
        >>> only_evens(357997555531)
        0
        >>> only_evens(13847896213354889741236)
        84862488426
        >>> only_evens(1202345678000)
        202468000
    """
    if num == 0:      # Base case
        return 0
    elif num % 2 == 0:
        return (only_evens(num // 10) * 10) + (num % 10)  # Keeps digit if even
    else:
        return only_evens(num // 10)  # Chops off last digit if it's odd
    


# ========= PART 2 ================

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    """
        >>> my_tree = BinarySearchTree() 
        >>> my_tree.isEmpty()
        True
        >>> my_tree.isBalanced
        True
        >>> my_tree.insert(9) 
        >>> my_tree.insert(5) 
        >>> my_tree.insert(14) 
        >>> my_tree.insert(4)  
        >>> my_tree.insert(6) 
        >>> my_tree.insert(5.5) 
        >>> my_tree.insert(7)   
        >>> my_tree.insert(25) 
        >>> my_tree.insert(23) 
        >>> my_tree.getMin
        4
        >>> my_tree.getMax
        25
        >>> 67 in my_tree
        False
        >>> 5.5 in my_tree
        True
        >>> my_tree.isEmpty()
        False
        >>> my_tree.getHeight(my_tree.root)   # Height of the tree
        3
        >>> my_tree.getHeight(my_tree.root.left.right)
        1
        >>> my_tree.getHeight(my_tree.root.right)
        2
        >>> my_tree.getHeight(my_tree.root.right.right)
        1
        >>> my_tree.isBalanced
        False
        >>> my_tree.insert(10)
        >>> my_tree.isBalanced
        True
        >>> newtree = BinarySearchTree()
        >>> newtree.insert(5)
        >>> newtree.insert(4)
        >>> newtree.getHeight(newtree.root)
        1
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def isEmpty(self):
        if self.root is None:   # If the tree is empty, the root will be None
            return True
        else:
            return False


    @property
    def getMin(self): 
        if self.isEmpty():
            return None
        else:
            current = self.root
            while current.left != None: # If we continue to go left in the tree, we will always reach the min
                current = current.left
            return current.value


    @property
    def getMax(self): 
        if self.isEmpty():
            return None
        else:
            current = self.root
            while current.right != None: # If we continue to go right in the tree, we will always reach the max
                current = current.right
            return current.value


    def __contains__(self,value):
        if self.isEmpty():
            return False
        else:
            current = self.root
            while current != None:
                if current.value == value:   # We know we've found the value
                    return True
                elif current.value < value:  # We know we need to go higher, so we look to the right
                    current = current.right
                else:                        # We know we need to go lower, so we look to the left
                    current = current.left

            return False    # Once we reach None instead of our value, we know the value is not in the tree


    def getHeight(self, node):
        if node == None:    # Base case for when the path does not exist
            return 0
        if node.right == None and node.left == None: # Base case for when we've reached a leaf node
            return 0
        else:
            return 1 + max(self.getHeight(node.left),self.getHeight(node.right))  # Adds 1 for every edge, makes recursive calls
                                                                                  # to find max height on either side of the node


        

    @property
    def isBalanced(self):  # Do not modify this method
        return self.isBalanced_helper(self.root)
    
    
    def isBalanced_helper(self, node):

        if node == None or (node.left == None and node.right == None): # Base case for once we've reached the end of a path or leaf nodes
            return True
        
        difference = abs(self.getHeight(node.left) - self.getHeight(node.right))

        if node.left == None or node.right == None:
            difference += 1        #  Account for possibility when only one of the subtrees does not exist
        
        if difference > 1:         #  If the abs value of difference in height between any of the
            return False           #  two children is more than 1, then the tree is unbalanced
        else:
            return self.isBalanced_helper(node.left) and self.isBalanced_helper(node.right)  # All of the children and their children will be balanced if the tree is balanced





def run_tests():
    import doctest

    # Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace is_power_of with the name of the function/class you want to test
    #doctest.run_docstring_examples(is_power_of, globals(), name='RecursionPractice',verbose=True)   

# Uncomment to run tests
#if __name__ == "__main__":
    #run_tests()