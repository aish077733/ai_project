"""Search Algorithms: BFS, DFS and their variants
Implementation of Uninformed Search Strategies
"""

from collections import deque
import time
from typing import List, Set, Tuple, Optional, Any, Dict

class SearchState:
    """Base class for search states"""
    def __init__(self, state_repr: Any, parent=None, action=None):
        self.state = state_repr
        self.parent = parent
        self.action = action
        self.depth = 0 if parent is None else parent.depth + 1
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
    
    def __repr__(self):
        return f"State({self.state})"

class SearchMetrics:
    """Track search performance metrics"""
    def __init__(self):
        self.nodes_expanded = 0
        self.nodes_explored = 0
        self.path_length = 0
        self.execution_time = 0
        self.max_memory = 0

class SearchAlgorithms:
    """Collection of uninformed search algorithms"""
    
    def __init__(self, initial_state: Any, goal_state: Any, successors_fn):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.successors_fn = successors_fn  # Function to generate successor states
    
    def bfs(self) -> Tuple[Optional[List], SearchMetrics]:
        """Breadth-First Search - explores nodes level by level"""
        metrics = SearchMetrics()
        start_time = time.time()
        
        initial = SearchState(self.initial_state)
        if self.initial_state == self.goal_state:
            metrics.path_length = 0
            metrics.execution_time = time.time() - start_time
            return [], metrics
        
        queue = deque([initial])
        visited = {self.initial_state}
        
        while queue:
            current = queue.popleft()
            metrics.nodes_expanded += 1
            
            successors = self.successors_fn(current.state)
            for successor, action in successors:
                if successor == self.goal_state:
                    metrics.path_length = current.depth + 1
                    metrics.execution_time = time.time() - start_time
                    metrics.nodes_explored = len(visited)
                    return self._construct_path(SearchState(successor, current, action)), metrics
                
                if successor not in visited:
                    visited.add(successor)
                    queue.append(SearchState(successor, current, action))
        
        metrics.execution_time = time.time() - start_time
        metrics.nodes_explored = len(visited)
        return None, metrics
    
    def dfs(self) -> Tuple[Optional[List], SearchMetrics]:
        """Depth-First Search - explores deeply before backtracking"""
        metrics = SearchMetrics()
        start_time = time.time()
        
        if self.initial_state == self.goal_state:
            metrics.execution_time = time.time() - start_time
            return [], metrics
        
        visited = set()
        stack = [(SearchState(self.initial_state), visited.copy())]
        
        def dfs_recursive(state, visited, depth=0):
            if state.state == self.goal_state:
                return state
            
            if state.state in visited:
                return None
            
            visited.add(state.state)
            metrics.nodes_expanded += 1
            
            successors = self.successors_fn(state.state)
            for successor, action in successors:
                result = dfs_recursive(SearchState(successor, state, action), visited, depth + 1)
                if result:
                    return result
            
            return None
        
        result = dfs_recursive(SearchState(self.initial_state), visited)
        metrics.execution_time = time.time() - start_time
        metrics.nodes_explored = len(visited)
        
        if result:
            metrics.path_length = result.depth
            return self._construct_path(result), metrics
        return None, metrics
    
    def dfs_iterative(self, depth_limit: Optional[int] = None) -> Tuple[Optional[List], SearchMetrics]:
        """Iterative DFS with optional depth limit"""
        metrics = SearchMetrics()
        start_time = time.time()
        
        if self.initial_state == self.goal_state:
            metrics.execution_time = time.time() - start_time
            return [], metrics
        
        stack = [SearchState(self.initial_state)]
        visited = set()
        
        while stack:
            current = stack.pop()
            metrics.nodes_expanded += 1
            
            if current.state == self.goal_state:
                metrics.path_length = current.depth
                metrics.execution_time = time.time() - start_time
                metrics.nodes_explored = len(visited)
                return self._construct_path(current), metrics
            
            if current.state not in visited:
                visited.add(current.state)
                
                if depth_limit is None or current.depth < depth_limit:
                    successors = self.successors_fn(current.state)
                    for successor, action in successors:
                        if successor not in visited:
                            stack.append(SearchState(successor, current, action))
        
        metrics.execution_time = time.time() - start_time
        metrics.nodes_explored = len(visited)
        return None, metrics
    
    def iddfs(self, max_depth: int = 10) -> Tuple[Optional[List], SearchMetrics]:
        """Iterative Deepening DFS - combines BFS and DFS benefits"""
        metrics = SearchMetrics()
        start_time = time.time()
        
        for depth_limit in range(max_depth + 1):
            visited = set()
            result = self._dfs_limited(depth_limit, visited)
            metrics.nodes_expanded += sum(1 for _ in visited)
            metrics.nodes_explored = len(visited)
            
            if result:
                metrics.path_length = result.depth
                metrics.execution_time = time.time() - start_time
                return self._construct_path(result), metrics
        
        metrics.execution_time = time.time() - start_time
        return None, metrics
    
    def _dfs_limited(self, depth_limit: int, visited: Set) -> Optional[SearchState]:
        """Helper for IDDFS - DFS with depth limit"""
        def dfs_recursive(state, remaining_depth):
            if state.state == self.goal_state:
                return state
            
            if remaining_depth == 0:
                return None
            
            if state.state in visited:
                return None
            
            visited.add(state.state)
            
            successors = self.successors_fn(state.state)
            for successor, action in successors:
                result = dfs_recursive(SearchState(successor, state, action), remaining_depth - 1)
                if result:
                    return result
            
            return None
        
        return dfs_recursive(SearchState(self.initial_state), depth_limit)
    
    def _construct_path(self, goal_state: SearchState) -> List:
        """Reconstruct path from goal state to initial state"""
        path = []
        current = goal_state
        while current.parent is not None:
            if current.action:
                path.append(current.action)
            current = current.parent
        path.reverse()
        return path
    
    def compare_algorithms(self) -> Dict[str, SearchMetrics]:
        """Compare performance of all algorithms"""
        results = {}
        
        path, metrics = self.bfs()
        results['BFS'] = metrics
        
        path, metrics = self.dfs()
        results['DFS'] = metrics
        
        path, metrics = self.dfs_iterative()
        results['DFS_Iterative'] = metrics
        
        path, metrics = self.iddfs()
        results['IDDFS'] = metrics
        
        return results
