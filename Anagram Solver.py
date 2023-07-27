# HW4
# Due Date: 11/05/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.
#       You might add additional methods to encapsulate and simplify the operations, but they must be
#       thoroughly documented


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.insert('mom')  
        >>> x.insert('omm') 
        >>> x.insert('mmo') 
        >>> x.root          
        Node({'mmo': ['mom', 'omm', 'mmo']})
        >>> x.insert('sat')
        >>> x.insert('kind')
        >>> x.insert('ats') 
        >>> x.root.left
        Node({'ast': ['sat', 'ats']})
        >>> x.root.right is None
        True
        >>> x.root.left.right
        Node({'dikn': ['kind']})
    '''

    def __init__(self):
        self.root = None


    # Modify the insert and _insert methods to allow the operations given in the PDF
    def insert(self, value):
        
        if self.root is None:
            newDict = {}
            sortedValue = "".join(sorted(value))
            newDict[ sortedValue] = [value]
            self.root=Node(newDict)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        sortedValue = "".join(sorted(value))
        key = list(node.value)[0]
        if(sortedValue<key):
            if(node.left==None):
                newDict = {}
                newDict[sortedValue] = [value]
                node.left = Node(newDict)
            else:
                self._insert(node.left, value)
        elif sortedValue==key:
            node.value[sortedValue].append(value)
        else:
            if(node.right==None):
                newDict = {}
                newDict[sortedValue] = [value]
                node.right = Node(newDict)
            else:
                self._insert(node.right, value)


    def isEmpty(self):
        return self.root == None

    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)   

    



class Anagrams:
    '''
        # Verify class has _bst attribute  
        >>> x = Anagrams(5)
        >>> '_bst' in x.__dict__    
        True
        >>> isinstance(x.__dict__.get('_bst'), BinarySearchTree)
        True
        >>> x = Anagrams(5)
        >>> x.create('words_small.txt')
        >>> x.getAnagrams('tap')
        'No match'
        >>> x.getAnagrams('arm')
        'No match'
        >>> x.getAnagrams('rat')
        ['art', 'tar', 'rat']
        >>> x._bst.printInorder
        {'a': ['a']} : {'adns': ['ands', 'sand']} : {'ahms': ['sham', 'hams']} : {'amt': ['tam', 'mat']} : {'arst': ['arts', 'rats', 'star']} : {'arsty': ['artsy']} : {'art': ['art', 'tar', 'rat']} : 
    '''



    def __init__(self, word_size):
        self.word_size = word_size
        self._bst = BinarySearchTree()

        pass




    def create(self, file_name):
        with open(file_name) as f: # ensures the file closes after the file operation finishes 
            contents = f.read() # reads the entire file, saving data in contents as string 
            allWords = contents.split()
            for word in allWords:
                if len(word) <= self.word_size:
                    self._bst.insert(word)


    def getAnagrams(self, word):

        wordSorted = "".join(sorted(word))
        current = self._bst.root
        while current:
            key = list(current.value)[0]

            if wordSorted< key :
                current = current.left
            elif wordSorted == key:
                return current.value[key]
            else:
                current = current.right
        
        return 'No match'



