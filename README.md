# data_structures-portfolioproj
<br>Course: Data Structures
<br>Language: Python 3.8
<br>Tools: Microsoft Visual Studio Code

## Introduction
The course taught data structures and abstract data types including Dyanmic Arrays, Bags, Linked Lists, Stacks, Queues, Deques, Trees, Binary Trees, AVL Trees, Heaps, Hash Tables and introduced Graphs, Big-O complexity, and amortized analysis. The course culminated in this final project to tie in multiple data structures through implementation of a Hash Table and a Minimum Heap.

## Description
Implementing a Hash Table requires a Dynamic Array by itself or the addition of a LinkedList, depending on what is chosen to handle hash collisions. For this implementation, hash collisions were handled with chaining, and thus utilized Linked Lists alongside the Dynamic Array. The two hash functions are relatively simple, and create enough of a spread in resulting hashed indices to demonstrate functionality.

The Minimum Heap is implemented using a Dynamic Array functioning as a Priority Queue. Associated methods perform work via calculating indices of children or parent nodes.

Both the Linked List and Dynamic Array helper structures are imported from helper_structs.py. A small test suite is included at the bottom of hash_map.py/min_heap.py that demonstrate each of the methods.

## Instructions
All files necessary to run the project on Microsoft Visual Studio Code are included in this repository. Make sure that Python is your chosen interpreter (version 3 or higher).

### Running program tests
1) Open either hash_map.py or min_heap.py within the IDE of your choice.

2) Tests are by default commented out. Uncomment the test suite by removing the leading number signs (#) or by hitting Ctrl + /. 

3) Run the program by clicking Run -> Run Without Debugging or press Ctrl + F5.
