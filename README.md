# AI Project: Uninformed Search Algorithms

A comprehensive implementation of uninformed search strategies with applications to classic AI problems.

## Project Overview

This project implements and compares various uninformed search algorithms:
- **BFS (Breadth-First Search)** - Level-by-level exploration
- **DFS (Depth-First Search)** - Deep exploration with backtracking
- **DFS Iterative** - Depth-limited DFS variant
- **IDDFS (Iterative Deepening DFS)** - Combines BFS optimality with DFS memory efficiency

## Project Structure

### Core Modules

#### 1. `search_algorithms.py`
Implements the fundamental search algorithms with performance tracking:
- **SearchState**: Represents nodes in the search tree
- **SearchMetrics**: Tracks performance metrics (time, nodes explored, path length)
- **SearchAlgorithms**: Main class implementing all search variants

Key Features:
- Configurable successor function
- Performance metrics collection
- Support for goal state checking

#### 2. `search_problems.py`
Implements four classic AI problems:

**Tic Tac Toe**
- Game playing scenario
- Successor generation for valid moves
- Win condition checking

**Eight Queens**
- Constraint satisfaction problem
- N-queens solver
- All solutions finding capability

**Milk and Water Jug Problem**
- State space search
- Jug filling, emptying, and pouring operations
- Target volume detection

**Missionaries and Cannibals**
- River crossing problem
- State validity constraints
- Recursive backtracking solution

#### 3. `test_search_comparison.py`
Comprehensive test suite and performance comparison:
- Tests for each problem
- Algorithm performance metrics
- Characteristics comparison table

#### 4. `architecture_design_turing_captcha.md`
Architecture design documentation for advanced concepts:
- Turing test implementation strategies
- CAPTCHA design principles

## Algorithm Characteristics

| Aspect | BFS | DFS | IDDFS |
|--------|-----|-----|-------|
| Optimal | Yes | No | Yes |
| Complete | Yes | No* | Yes |
| Space | O(b^d) | O(b*d) | O(b*d) |
| Time | O(b^d) | O(b^d) | O(b^d) |

*No in infinite graphs

## Performance Comparison

### Key Findings:
1. **BFS** finds shortest path but requires exponential memory
2. **DFS** uses linear memory but may find suboptimal paths
3. **IDDFS** combines benefits: optimal solution with linear memory
4. Problem complexity significantly affects algorithm performance

## Usage Examples

### Running Tests
```bash
python test_search_comparison.py
```

### Using Search Algorithms
```python
from search_algorithms import SearchAlgorithms
from search_problems import MissionariesCannibals

# Initialize problem
mc = MissionariesCannibals()
initial = mc.initial
goal = mc.goal

# Create search instance
search = SearchAlgorithms(initial, goal, mc.get_successors)

# Perform BFS
path, metrics = search.bfs()
print(f"Path: {path}")
print(f"Nodes Explored: {metrics.nodes_explored}")
print(f"Time: {metrics.execution_time}s")
```

## Problem Descriptions

### Tic Tac Toe
- Board representation: 9-character string
- Successor: All valid move positions
- Goal: Get three in a row

### Eight Queens
- State: List of column positions
- Constraint: No two queens on same row/column/diagonal
- Solutions: 92 valid configurations

### Milk & Water Jug (3L and 5L)
- State: (jug1_volume, jug2_volume)
- Operations: Fill, empty, pour between jugs
- Goal: Achieve target volume

### Missionaries and Cannibals
- State: (missionaries_left, cannibals_left, boat_position)
- Constraint: Cannibals can't outnumber missionaries on either bank
- Goal: Transport all across river safely

## Installation

No external dependencies required. Uses only Python standard library:
- collections (deque)
- time
- typing

## Implementation Details

### SearchState
Represents a node in the search tree:
- `state`: The actual state representation
- `parent`: Reference to parent node
- `action`: Action taken to reach this state
- `depth`: Level in search tree

### SearchMetrics
Tracks algorithm performance:
- `nodes_expanded`: Count of nodes explored
- `nodes_explored`: Total unique nodes visited
- `path_length`: Solution path length
- `execution_time`: Algorithm runtime

## Performance Observations

1. **Memory Usage**: IDDFS significantly more memory-efficient than BFS
2. **Solution Quality**: BFS guarantees optimal paths
3. **Execution Time**: Problem-dependent; IDDFS may revisit nodes
4. **Scalability**: All algorithms struggle with large search spaces

## Future Enhancements

- Implement informed search (A*, Best-First)
- Add heuristic functions for problems
- Performance visualization
- Parallel search exploration
- More complex problem variants

## References

- Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach
- Nilsson, N. J. (1998). Artificial Intelligence: A New Synthesis
- Classical AI Problems and their algorithms

## Author

Implemented as part of AI coursework - Assignment Task 3

## License

Educational use. Feel free to modify and distribute for learning purposes.
