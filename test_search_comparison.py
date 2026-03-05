"""Test and Performance Comparison of Search Algorithms
Comparing BFS, DFS and variants performance across problems
"""

from search_algorithms import SearchAlgorithms, SearchMetrics
from search_problems import (
    TicTacToe, EightQueens, JugProblem, MissionariesCannibals
)
import time
from typing import Dict, List
import json

def test_tic_tac_toe():
    """Test Tic Tac Toe problem"""
    print("\n=== Testing Tic Tac Toe Problem ===")
    
    ttt = TicTacToe()
    initial_state = ' ' * 9  # Empty board
    goal_state = 'X' * 3 + ' ' * 6  # X wins on top row (simplified)
    
    search = SearchAlgorithms(initial_state, goal_state, ttt.get_successors)
    
    print("BFS Search:")
    path, metrics = search.bfs()
    print(f"  Nodes Expanded: {metrics.nodes_expanded}")
    print(f"  Nodes Explored: {metrics.nodes_explored}")
    print(f"  Path Length: {metrics.path_length}")
    print(f"  Time: {metrics.execution_time:.6f}s")
    
    print("DFS Search:")
    path, metrics = search.dfs()
    print(f"  Nodes Expanded: {metrics.nodes_expanded}")
    print(f"  Nodes Explored: {metrics.nodes_explored}")
    print(f"  Path Length: {metrics.path_length}")
    print(f"  Time: {metrics.execution_time:.6f}s")

def test_eight_queens():
    """Test Eight Queens problem"""
    print("\n=== Testing Eight Queens Problem ===")
    
    eq = EightQueens()
    print(f"Finding all solutions...")
    solutions = eq.find_solutions()
    print(f"Total Solutions Found: {len(solutions)}")
    if solutions:
        print(f"First Solution: {solutions[0]}")
        print(f"  (Row indices represent column positions)")

def test_jug_problem():
    """Test Milk and Water Jug problem"""
    print("\n=== Testing Milk and Water Jug Problem ===")
    
    # Problem: Get 4 liters in a 3L and 5L jug
    jug = JugProblem(3, 5, 4)
    initial = (0, 0)
    
    def jug_successors(state):
        return jug.get_successors(state)
    
    search = SearchAlgorithms(initial, initial, jug_successors)
    
    print("BFS Search for target 4L:")
    path, metrics = search.bfs()
    if path:
        print(f"  Solution Found: {path}")
        print(f"  Path Length: {len(path)}")
    else:
        print("  Solution not found")
    print(f"  Nodes Explored: {metrics.nodes_explored}")
    print(f"  Time: {metrics.execution_time:.6f}s")

def test_missionaries_cannibals():
    """Test Missionaries and Cannibals problem"""
    print("\n=== Testing Missionaries and Cannibals Problem ===")
    
    mc = MissionariesCannibals()
    initial = mc.initial
    goal = mc.goal
    
    def mc_successors(state):
        return mc.get_successors(state)
    
    search = SearchAlgorithms(initial, goal, mc_successors)
    
    print(f"Initial State: {initial}")
    print(f"Goal State: {goal}")
    print("\nBFS Search:")
    path, metrics = search.bfs()
    if path:
        print(f"  Solution Found with {len(path)} moves")
        for i, move in enumerate(path, 1):
            print(f"    Move {i}: {move}")
    else:
        print("  Solution not found")
    print(f"  Nodes Expanded: {metrics.nodes_expanded}")
    print(f"  Time: {metrics.execution_time:.6f}s")
    
    print("\nIDDFS Search:")
    search2 = SearchAlgorithms(initial, goal, mc_successors)
    path, metrics = search2.iddfs(max_depth=15)
    if path:
        print(f"  Solution Found with {len(path)} moves")
    print(f"  Nodes Expanded: {metrics.nodes_expanded}")
    print(f"  Time: {metrics.execution_time:.6f}s")

def performance_comparison():
    """Compare performance of algorithms"""
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON SUMMARY")
    print("="*60)
    
    results = {
        'Tic Tac Toe': {},
        'Eight Queens': {},
        'Jug Problem': {},
        'Missionaries & Cannibals': {}
    }
    
    print("\nKey Observations:")
    print("1. BFS finds shortest path but explores more nodes")
    print("2. DFS uses less memory but may take longer paths")
    print("3. IDDFS combines benefits: optimal path + lower memory")
    print("4. Problem complexity affects algorithm performance")
    
    print("\nAlgorithm Characteristics:")
    print("-" * 60)
    print("BFS (Breadth-First Search):")
    print("  - Optimal: Yes (finds shortest path)")
    print("  - Complete: Yes")
    print("  - Space: O(b^d) - exponential")
    print("  - Time: O(b^d) - exponential")
    
    print("\nDFS (Depth-First Search):")
    print("  - Optimal: No (may find longer paths)")
    print("  - Complete: No (in infinite graphs)")
    print("  - Space: O(b*d) - linear")
    print("  - Time: O(b^d) - exponential")
    
    print("\nIDDFS (Iterative Deepening DFS):")
    print("  - Optimal: Yes")
    print("  - Complete: Yes")
    print("  - Space: O(b*d) - linear")
    print("  - Time: O(b^d) - exponential")

if __name__ == '__main__':
    print("\n" + "="*60)
    print("SEARCH ALGORITHMS - TEST AND COMPARISON")
    print("="*60)
    
    test_tic_tac_toe()
    test_eight_queens()
    test_jug_problem()
    test_missionaries_cannibals()
    performance_comparison()
    
    print("\n" + "="*60)
    print("Testing Complete")
    print("="*60)
