# links
    https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/
    https://en.wikipedia.org/wiki/List_of_data_structures

# surrounding
##access
    sequential
        can only access elems in order stored
    random/direct access
        access an arbitrary element of a sequence in equal time or any datum from a population of addressable elements roughly as easily and efficiently as any other

## specification
    map
        dictionary problem solutons
            hash table
            search tree //tree ds, locate different keys within a set
                binary search tree
                self balancing - any st can be, as opposed to a unbalanced

# language specific
    string (char arr)
        manipulation

# types

## linear //elems form a seq
### array //collection of elemns each identified by index or key
    fixed/general array
    two dimensional arr/matrice/matrix
    cicular buffer //store data streams
### collection literals (lists)
    dynamic arr / arr list //random access variable-size list
    linked list
        singly linked list
        doubly linked list
        circular linked list

## tree
    binary tree
        binary search tree
            self balancing / height balanced
                AVL Trees
                red-black trees
        fenwick tree / binary indexed tree 
    n-ary tree
    self balancing
        search tree
            //auto balance to stop overloading on one branch (losing O(log n))
            B-tree
                of order m
                    requirements
                        every node at most m children
                        non-leaf node with k children contains k-1 keys
                        root at least 2 children if not leaf node
                        non-leaf nodes (except root) has >= m/2 children
                        all leaves appear in same lv
                    inserting val
                        compare to vals in tree put inbetween less and more than vals
                        if new val makes num vals in node > m
                            node split into two nodes, left has vals < median val and right >
                                median val is promoted to parent node
                        if root node too many nodes then new root node created with med val
                B+-tree
    2-3 tree
    binary heaps
    prefix trees (trie)
    segment/statistic tree

## map
    hash list //list of hashes of data blocks in a file
    hash map/table //map key to value, implements dict

## queue
    double-ended priority queue (DEPQ) //priority queue and deque
    heap //priority queue
        binary heap

## priority queue
    heap - tree based
    unordered array

## graphs
    Adjacency list
        Vertices stored as records or objects, every vertex stores a list of adjacent vertices 
        allows the storage of additional data on the vertices. 
        Additional data can be stored if edges are also stored as objects, in which case each vertex stores its incident edges and each edge stores its incident vertices.
    Adjacency matrix
        two-dimensional matrix, rows rep source vertices & cols rep destination vertices
        Data on edges and vertices must be stored externally. Only the cost for one edge can be stored between each pair of vertices.
        square |V| × |V| matrix A such that its element Aij is one when there is an edge from vertex i to vertex j, and zero when there is no edge
    Incidence matrix
        A two-dimensional Boolean matrix, in which the rows represent the vertices and columns represent the edges. The entries indicate whether the vertex at a row is incident to the edge at a column.

# abstract data types 
//model for data type, defined by the behaviour from users point of view
    container/collection
        list/seq //countable num of ordered values
            set //can only store unique values
                multiset //set generalisation with no dups
            queues //fifo
                prioriry queue
                deque / double ended queue
            stacks //lifo
            tuple //finite ordered list of elements
                n-tuple //list of n (>0) elements
        trees //generalised digraph
        map/dict/associativearray //collection of key value pairs, each key different
            multimap //map generalisation where >1 val may be associated with and returned for a given key
        graph // math undirected/directed graph, set of vertices/nodes & set of unordered/ordered pairs for them
        //pairs known as edges/links/lines (undirected) or arrows (directed)
        //vertices part of graph structure or external entities with int indicies or refs

    bag //dynamic array you can only add too
