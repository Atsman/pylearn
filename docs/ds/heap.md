# Priority Queue

## Operations

* insert (S, x): insert element x into set S.
* max(S): return element of S with the largest key.
* extract_max(S): and return it from S
* increase_key(s, x, k): increase the value of x's key to new value k.

# Heap

An array visualized an a nearly complete binary tree.

Example:

 1  2  3  4  5  6  7  8  9  10
|16|14|10| 8| 7| 9| 3| 2| 4| 1|

root of the tree: first element (i = 1)
parent(i) = i / 2
left(i) = 2i
right(i) = 2i+1
