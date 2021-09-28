For the sum of the absolute values of differences between its adjacent elements to be minimal, I used the fact that array must be sorted, So in order to find minimum no. of swaps required to make array beautiful I just find minimum no. of swaps in order to sort an array.

Concept used:
This can be easily done by visualizing the problem as a graph. We will have n nodes and an edge directed from node i to node j if the element at i’th index must be present at j’th index in the sorted array.

The graph will now contain many non-intersecting cycles. Now a cycle with 2 nodes will only require 1 swap to reach the correct ordering, similarly a cycle with 3 nodes will only require 2 swap to do so.

Time Complexity: O(n*log(n))

