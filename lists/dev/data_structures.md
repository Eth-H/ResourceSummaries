# links
    https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/
    https://en.wikipedia.org/wiki/List_of_data_structures
# surrounding
    access
        sequential
            can only access elems in order stored
        random/direct access
            access an arbitrary element of a sequence in equal time or any datum from a population of addressable elements roughly as easily and efficiently as any other

# language specific
    string (char arr)
        manipulation




# linear //elems form a seq
    array //collection of elemns each identified by index or key
        fixed/general array
        two dimensional arr/matrice/matrix
        cicular buffer //store data streams
    collection literals (lists)
        dynamic arr / arr list //random access variable-size list
        linked list
            singly linked list
            doubly linkded list
# tree
    Binary search tree
    AVL Trees
    Red Black Trees
    Binary Heaps
# hash based
    hash list //list of hashes of data blocks in a file
    hash map/table //map key to value, implements dict

# heap
    binary heap

# graphs
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

# abstract data type //model for data type, defined by the behaviour from users point of view
    list/seq //countable num of ordered values
    set //can only store unique values
    Queues //FIFO
    Stacks //LIFO
    Tuple //finite ordered list of elements
    n-tuple //list of n (>0) elements
    Trees
    dict/associative array //collection of key value pairs, each key different
    graph // math undirected/directed graph, set of vertices/nodes & set of unordered/ordered pairs for them
        //pairs known as edges/links/lines (undirected) or arrows (directed)
        //vertices part of graph structure or external entities with int indicies or refs

    bag //dynamic array you can only add too


