# links
## learn
### algorithmic technique
    https://www.geeksforgeeks.org/algorithms-design-techniques/
    https://en.wikipedia.org/wiki/Algorithmic_technique
    https://www.geeksforgeeks.org/dynamic-programming/
    https://www.javatpoint.com/daa-algorithm-design-techniques
    https://en.wikipedia.org/wiki/Algorithm#Design
## challenges
## repos

https://www.geeksforgeeks.org/fundamentals-of-algorithms/
    algorithms
    Recursion
    Sorting
        bubble
        merge
        sort
    Searching
        binary
    Node/Tree Traversal
        Breadth First Search
        Depth First Search
    graph
        network theory
            page rank
        routing
            shortest path
                dijkstra
        search //may need to transverse same node > once
            a* algorithm
            Dijkstra's algorithm (a* with no heuristic func)
            Breadth-first search //traverses a graph level by level
            Depth-first search //traverses a graph branch by branch
    sequence
        search
            unsorted
                Linear search
            sorted
                Binary search algorithm
        merging //join two lists (eg used in merge sort)
            K-way merging
            Parallel merge
        sort
            exchange
                bubble
                quick sort
            timsort
            insertion sort
                shell sort
            Merge sort

# algorithmic technique
    approach for implementing a process/computation

    dynamic programming / bottom-up

# how to classify algorithms
    by implementation
        recursion
            invokes itself until termination condition
        logical
            controlled deductive reasoning 
            algorithm = logic + control
        serial, parallel or distributed
            serial: one isntruction at a time
            parallel: several processors
            distributed: several networked machines
        deterministic or non-deterministic
            deterministic: exact decision at every step of the algorithm
            non-deterministic: guessing with heuristics to improve accuracy
        exact or approximate
            target an approximate sol with deterministic or random stratergy
        quantum algorithm
            use quantum computing features
    by design
        brute force /exhaustive search
        divide and conquer
            repeatedly reduces an instance of a problem to one or more smaller instances of the same problem (usually recursively) until the instances are small enough to solve easily
        search and enumeration
            search alogithms
                retrieve info from data structure or calc in search space of problem domain
            graph exploration/search algorithm
            branch and bound enumeration
            backtracking
        randomized algorithm
            choices randomly (or pseudo-randomly)
            finding approximate solutions for problems where finding exact solutions can be impractical
        reduction of complexity / transform and conquer
            involves solving a difficult problem by transforming it into a better-known problem for which we have (hopefully) asymptotically optimal algorithms 
    by optimization problems 
        linear programming
        dynamic programming
            can use if
                problem shows optimal substructures (optimal solution to a problem can be constructed from optimal solutions to subproblems)
                overlapping subproblems (meaning the same subproblems are used to solve many different problem instances)
            fits with memoization
        greedy
            improve exisiting solution with modifications
        heuristic method
            find a solution close to the optimal solution in cases where finding the optimal solution is impractical
            local search, tabu search, simulated annealing, and genetic algorithms
            when a bound on the error of the non-optimal solution is known, the algorithm is further categorized as an approximation algorithm
    by field of study
        most are operations on a data structure
        search algorithms, sorting algorithms, merge algorithms, numerical algorithms, graph algorithms, string algorithms, computational geometric algorithms, combinatorial algorithms, medical algorithms, machine learning, cryptography, data compression algorithms and parsing techniques
    by complexity    
        time required for an alogithm
        constant time: is the same, regardless of the input size. e.g. an access to an array element.
        logarithmic time: logarithmic function of the input size. e.g. binary search algorithm.
        linear time: proportional to the input size. e.g. the traverse of a list.
        polynomial time: a power of the input size. e.g. the bubble sort algorithm has quadratic time complexity.
        exponential time: an exponential function of the input size. e.g. brute-force search.

# summary
procedure having well defined steps for solving a particular problem
finite set of logic or instructions, written in order for accomplish the certain predefined task
can repersent logic with flowchat / pseudo code

## categories
    sort: algorithm developed for sorting the items in certain order.
    search: algorithm developed for searching the items inside a data structure.
    delete: algorithm developed for deleting the existing element from the data structure.
    insert: algorithm developed for inserting an item inside a data structure.
    update: algorithm developed for updating the existing element inside a data structure.

## measure performance
    time complexity: way of representing the amount of time needed by a program to run to the completion
    space complexity: it is the amount of memory space required by an algorithm, during a course of its execution. space complexity is required in situations when limited memory is available and for the multi user system.

## algorithm components
    specification: description of the computational procedure.
    pre-conditions: the condition(s) on input.
    body of the algorithm: a sequence of clear and unambiguous instructions.
    post-conditions: the condition(s) on output.

## characteristics
must haves
    input: 0 or well defined inputs.
    output: 1 or well defined outputs, and should match with the desired output.
    feasibility: be terminated after the finite number of steps.
    independent: have step-by-step directions which is independent of any programming code.
    unambiguous: be unambiguous and clear. each of their steps and input/outputs must be clear and lead to only one meaning.
