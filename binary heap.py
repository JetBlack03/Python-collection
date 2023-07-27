#Lab #7
#Due Date: 11/12/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.

class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        return self._heap[0]
    
    
    def _parent(self,index):
        if index <= len(self) and index > 1:
            return self._heap[index//2 - 1]
        else:
            return None

    def _leftChild(self,index):
        if len(self) >= index*2:
            return self._heap[index*2 - 1]
        else:
            return None

    def _rightChild(self,index):
        if len(self) >= index*2+1:
            return self._heap[index * 2 ]
        else:
            return None


    def insert(self,item):
        self._heap.append(item)
        heapIndex = len(self)
        while self._parent(heapIndex) != None and item < self._parent(heapIndex):
            self._heap[heapIndex -1 ] = self._parent(heapIndex)
            heapIndex = heapIndex//2
            self._heap[heapIndex - 1] = item

            

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted=self._heap[0]
            self._heap=[]
            return deleted
        else:
            min = self._heap[0]
            self._heap[0] = self._heap[-1]
            heapIndex = 1
            newValue = self._heap[0]
            while (self._leftChild(heapIndex) != None and newValue > self._leftChild(heapIndex)) or ( self._rightChild(heapIndex) != None and newValue > self._rightChild(heapIndex)):
                if self._leftChild(heapIndex) > self._rightChild(heapIndex):
                    self._heap[heapIndex - 1] = self._rightChild(heapIndex)
                    heapIndex = heapIndex*2 + 1
                    self._heap[heapIndex - 1] = newValue
                else:
                    self._heap[heapIndex - 1] = self._leftChild(heapIndex)
                    heapIndex = heapIndex*2 
                    self._heap[heapIndex - 1] = newValue

            self._heap.pop()
            return min



def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    heap = MinBinaryHeap()
    for i in numList:
        heap.insert(i)
    
    sortedList = []
    for i in range(len(numList)):
        sortedList.append(heap.deleteMin())
        
    return sortedList
    