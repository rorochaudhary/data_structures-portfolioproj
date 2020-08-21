# Course: CS261 - Data Structures
# Assignment: 5 - Min Heap Implementation
# Student: Rohit Chaudhary
# Description: Implementation of a Min Heap with methods of add, get_min, remove_min, and build_heap. Utilizes DynamicArray as underlying data structure.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        function adds a new value to the heap, maintaining heap property.
        """
        # add item to heap and percolate to correct spot
        self.heap.append(node)
        self.percolate_up()

        return

    def percolate_up(self) -> None:
        """
        function is a helper method to add() that will "percolate" the last heap item to its correct heap position with repeated swaps.
        """
        # starting node and parent values
        node_index = self.heap.length() - 1
        parent_index = (node_index - 1) // 2
        node = self.heap.get_at_index(node_index)
        parent = self.heap.get_at_index(parent_index)

        # while parent > node
        while parent > node:
            # if node is a the top (index 0), we are done
            if node_index == 0:
                break
            # swap node and parent
            else:
                self.heap.swap(node_index, parent_index)
                # recalculate node and parent
                node_index = parent_index
                parent_index = (node_index - 1) // 2
                node = self.heap.get_at_index(node_index)
                parent = self.heap.get_at_index(parent_index)
        
        return

    def get_min(self) -> object:
        """
        function returns the top value of the MinHeap. raises MinHeapException if heap is empty
        """
        if self.is_empty():
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        function removes the minimum key element from the heap, returning the value. removing from empty heap raises MinHeapException.
        """
        if self.is_empty():
            raise MinHeapException
        else:
            min_element = self.get_min()
            # swap last and first heap elements, removing the last
            self.heap.swap(0, self.heap.length() - 1)
            self.heap.pop()
            # check if removed the only element (empty heap)
            if not self.is_empty():
                # move element to proper position within heap
                self.percolate_down()
    
            return min_element

    def percolate_down(self) -> None:
        """
        function is a helper method to remove_min(), "percolating" the top heap element downwards via repeated swaps, maintaining min-heap property.
        """
        # indices
        i = 0
        i_left = (2 * i) + 1
        i_right = (2 * i) + 2
        i_small = 0

        # keep swapping while there are valid indices
        while i_left < self.heap.length() or i_right < self.heap.length():
            # current node and its children
            current = self.heap.get_at_index(i)

            # handle one or two children
            if i_left >= self.heap.length():
                right_child = self.heap.get_at_index(i_right)
                smaller_child = right_child
                i_small = i_right
            elif i_right >= self.heap.length():
                left_child = self.heap.get_at_index(i_left)
                smaller_child = left_child
                i_small = i_left
            else:   # compare children to find the smaller
                right_child = self.heap.get_at_index(i_right)
                left_child = self.heap.get_at_index(i_left)
                if left_child <= right_child:
                    smaller_child = left_child
                    i_small = i_left
                else:
                    smaller_child = right_child
                    i_small = i_right
            # found smaller child, compare with current
            if current > smaller_child:
                # swap
                self.heap.swap(i, i_small)

                # recalculate indices
                i = i_small
                i_left = (2 * i) + 1
                i_right = (2 * i) + 2
                i_small = 0

            else:
                break
        return

    def build_heap(self, da: DynamicArray) -> None:
        """
        function recieves a DynamicArray with objects in any order and builds a valid MinHeap
        """
        # copy heap into new_heap
        new_heap = DynamicArray()
        for j in range(da.length()):
            new_heap.append(da.get_at_index(j))

        # get the first non-leaf index
        i = (new_heap.length() // 2) - 1
        for k in range(i + 1, -1, -1):
            self.percolate_build(new_heap, k)

        # new_heap is sorted, make that the main heap
        self.heap = new_heap
        return

    def percolate_build(self, da, non_leaf_index) -> None:
        """
        function is a helper method to build_heap, which percolates down the DynArray (da) heap element at position non_leaf_index into proper position. similar to percolate_down helper method implemented for remove_min.
        """
        # indices
        i = non_leaf_index
        i_left = (2 * i) + 1
        i_right = (2 * i) + 2
        i_small = 0

        # keep swapping while there are valid indices
        while i_left < da.length() or i_right < da.length():
            # current node and its children
            current = da.get_at_index(i)

            # handle one or two children
            if i_left >= da.length():
                right_child = da.get_at_index(i_right)
                smaller_child = right_child
                i_small = i_right
            elif i_right >= da.length():
                left_child = da.get_at_index(i_left)
                smaller_child = left_child
                i_small = i_left
            else:   # compare children to find the smaller
                right_child = da.get_at_index(i_right)
                left_child = da.get_at_index(i_left)
                if left_child <= right_child:
                    smaller_child = left_child
                    i_small = i_left
                else:
                    smaller_child = right_child
                    i_small = i_right

            # found smaller child, compare with current
            if current > smaller_child:
                # swap
                da.swap(i, i_small)

                # recalculate indices
                i = i_small
                i_left = (2 * i) + 1
                i_right = (2 * i) + 2
                i_small = 0

            else:
                break
        
        return

# BASIC TESTING
# if __name__ == '__main__':

#     print("\nadd example 1")
#     print("-------------------")
#     h = MinHeap()
#     print(h, h.is_empty())
#     for value in range(300, 200, -15):
#         h.add(value)
#         print(h)

    # print("\nadd example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)


    # print("\nget_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())


    # print("\nremove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())


    # print("\nbuild_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
