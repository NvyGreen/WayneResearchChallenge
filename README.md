# Wayne Hayes Research Challenge - Graph Theory

Solution to the connected-components + degree-histogram challenge for
Professor Wayne Hayes's applied graph theory / biological network
analysis project.

## How to run
- Requirements: Python 3, matplotlib
- Run `challenge.ipynb`
- Reads each file at the root of `sample_input/` (not the test subfolder),
  prints its component count, and saves a degree histogram to `plots/`.
- The program will check the components algorithm on test graph files to make
  sure it has the correct output, and also assert that the x and y axes data
  is correct before writing a plot.

## Challenge
I was given a set of files that I stored at the root of `sample_input/`.
The first line of each file represents `N`, the number of nodes, and
subsequent lines represent edges. Each node is numbered from 0 to `N-1`.
The goal was to calculate the number of connected components in each
graph. Additionally, I also had to create a histogram of the distribution
of degrees in each graph. Duplicate edges should be ignored, and isolated
nodes count as components.

## Approach
1. I stored all of the given input files in a directory so I could easily
   loop through them and analyze each file.
2. For each file, after reading the first line representing `N`, the
   number of nodes, I store the edges represented by the rest of the lines
   in a `defaultdict[int, set]`, with the key being the node, and the value
   being all the connected nodes. I used a `set` so duplicate edges aren't
   counted, and a `defaultdict` to make it easier to append nodes and so I
   don't get a `KeyError` on isolated nodes when I'm looping later. I treated
   the graph as undirected, since the undergrad requirement only covers the
   undirected case. I skip any line that is empty after `.strip()`, since every
   sample file ends with a blank line.
3. To count the number of connected components, I used an iterative DFS
   approach with a stack. For each unvisited node, I'd traverse to every
   other node I could reach from it, marking them visited on the way. I 
   looped from 0 to `N-1` inclusive so isolated nodes were also counted.
   1. I originally tried using a recursive DFS approach, but I hit the
      recursion limit on `n10000.txt`.
4. I also counted how many nodes had each degree in that same loop. The loop
   I do it in checks each node once, so I avoid double-counting. When I went
   to build the plot, I looped from 0 up to the max degree to get the values.
   Any degrees without nodes were given a value of zero. Self loops (`u == v`)
   would affect the degree count, but I checked and there are none in the
   sample files, so this case doesn't occur here. `N == 0` also doesn't occur
   here, but if that does ever happen, the program skips drawing a plot.

### Validation
1. To make sure my logic was correct, I created 3 sample text files in
   `sample_input/test_input`: one with an isolated node, one with all
   nodes connected, and one with no nodes connected. Because I knew the
   results for these graphs, I could assert on them before I ran my code
   on the real files. `assert sum(degrees.values()) == n` (where `degrees` is
   the data for the histogram) checks that every node was accounted for when I
   looped for degree/component counting, and I also assert that the component
   count is what I expected.
2. Additionally, when I'm building the `x` and `y` values for the real files'
   graphs, I assert that the lists are the same length, that `x` goes up to
   the max degree, and that all the values in `y` sum up to `n`.

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

## Commentary & Analysis

### Degree Distribution
- `n10.txt`: Left-skewed, meaning all the nodes are nearly all connected
to each other.  
- `n100.txt`: A fairly sparse graph, since most of the nodes only have
degree 1 or 2 and no node has tons of connections (the max degree is 5).  
- `n1000.txt`, `n10000.txt`: Close to a bell curve, but slightly
right-skewed. Most nodes are connected to a low-to-moderate amount of
other nodes, and there are a few higher-degree nodes that are connected to
more.  
- `s1.txt`: Possibly a hub-and-spoke: One node has a degree of 31, and
the peak is at 2 degrees.  

### Component Count
I expected that larger graphs would have more components, but that didn't
end up being the case. This is probably because larger graphs instead have
more connections: the peak moved from degree 2 in `n100.txt`, to degree 3
in `n1000.txt`, to degree 6 in `n10000.txt`. More connections means that more
nodes are linked together, which is why component count didn't get drastically
higher. The remaining components are mostly just isolated nodes (8 in `n100.txt`,
14 in `n1000.txt`, 10 in `n10000.txt`). `s1.txt` and `n10.txt` have no isolated
nodes: `n10.txt` is one connected component, and `s1.txt` has 6 separate clusters.