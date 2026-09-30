# Wayne Hayes Research Challenge - Graph Theory

Solution to the connected-components + degree-histogram challenge for
Professor Wayne Hayes's applied graph theory / biological network
analysis project.

## How to run
- Requirements: Python 3, matplotlib
- Run `challenge.ipynb`
- Reads each file at the root of `sample_input/`, prints its component count,
  and saves a degree histogram to `plots/`.
- The program will check the components algorithm on test graph files to make
  sure it has the correct output, and also assert that the x and y axes data
  is correct before writing a plot.

## Approach
- **Graph storage:** adjacency list using a `set` per node — so duplicate
  edges are ignored and degrees stay correct. Treated as undirected
  (each edge added both ways).
- **Connected components:** use iterative DFS and a stack to traverse
  from an unvisited node to every node that can be reached from it.
  Loop from 0 to N-1 (inclusive) so isolated nodes are also counted.
- **Degree histogram:** tally how many nodes have each degree, from 0
  up to the max degree. Any degree that doesn't have nodes gets filled
  in with zero.

## Results
| Graph | Nodes (N) | Connected components |
|-------|-----------|----------------------|
| n10    | 10     | 1  |
| n100   | 100    | 12 |
| n1000  | 1000   | 17 |
| n10000 | 10000  | 12 |
| s1     | 573    | 6  |

### Degree distributions
![n10](plots/n10.png)
![n100](plots/n100.png)
![n1000](plots/n1000.png)
![n10000](plots/n10000.png)
![s1](plots/s1.png)

## Verification
The script asserts that the degree counts sum to N on every graph, and I
validated the component logic against small hand-built test graphs with
known answers, including one with an isolated node and one with no edges.

## Notes / what I learned
My first version of the algorithm used recursive DFS, but that hit Python's
recursion limit on the 10,000-node graph. I rewrote it using an iterative stack
approach instead.