"""Search Problems Implementation
Four classical AI search problems:
1. Tic Tac Toe
2. Eight Queens
3. Milk and Water Jug
4. Missionaries and Cannibal
"""

from typing import List, Tuple, Set
import copy

class TicTacToe:
    """Tic Tac Toe problem using search"""
    
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.player = 'X'
        self.opponent = 'O'
    
    def get_successors(self, state):
        """Generate successor states"""
        successors = []
        for i in range(9):
            if state[i] == ' ':
                new_state = list(state)
                new_state[i] = self.player
                successors.append((''.join(new_state), f'Move at {i}'))
        return successors
    
    def is_goal(self, state):
        """Check if player has won"""
        lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in lines:
            if state[a] == state[b] == state[c] == self.player:
                return True
        return False

class EightQueens:
    """Eight Queens problem - place 8 queens on chessboard"""
    
    def __init__(self):
        self.n = 8
        self.solutions = []
    
    def is_safe(self, board: List[int], row: int, col: int) -> bool:
        """Check if placing queen is safe"""
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
            # Check diagonal
            if abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def get_successors(self, board: List[int], row: int) -> List[Tuple]:
        """Generate successor board configurations"""
        successors = []
        if row == self.n:
            return successors
        
        for col in range(self.n):
            if self.is_safe(board, row, col):
                new_board = board + [col]
                action = f'Queen at row {row}, col {col}'
                successors.append((new_board, action))
        return successors
    
    def is_goal(self, board: List[int]) -> bool:
        """Check if all queens are placed"""
        return len(board) == self.n
    
    def find_solutions(self, board=[]) -> List[List[int]]:
        """Find all solutions using backtracking"""
        if len(board) == self.n:
            self.solutions.append(board[:])
            return
        
        for col in range(self.n):
            if self.is_safe(board, len(board), col):
                self.find_solutions(board + [col])
        
        return self.solutions

class JugProblem:
    """Milk and Water Jug problem"""
    
    def __init__(self, jug1_capacity: int, jug2_capacity: int, target: int):
        self.jug1_cap = jug1_capacity
        self.jug2_cap = jug2_capacity
        self.target = target
        self.initial = (0, 0)
    
    def get_successors(self, state: Tuple[int, int]) -> List[Tuple]:
        """Generate successor states"""
        j1, j2 = state
        successors = []
        
        # Fill jug 1
        successors.append(((self.jug1_cap, j2), 'Fill jug 1'))
        # Fill jug 2
        successors.append(((j1, self.jug2_cap), 'Fill jug 2'))
        # Empty jug 1
        successors.append(((0, j2), 'Empty jug 1'))
        # Empty jug 2
        successors.append(((j1, 0), 'Empty jug 2'))
        # Pour jug 1 to jug 2
        amount = min(j1, self.jug2_cap - j2)
        successors.append(((j1 - amount, j2 + amount), 'Pour jug 1 to jug 2'))
        # Pour jug 2 to jug 1
        amount = min(j2, self.jug1_cap - j1)
        successors.append(((j1 + amount, j2 - amount), 'Pour jug 2 to jug 1'))
        
        return successors
    
    def is_goal(self, state: Tuple[int, int]) -> bool:
        """Check if target amount is in either jug"""
        return self.target in state

class MissionariesCannibals:
    """Missionaries and Cannibals problem"""
    
    def __init__(self):
        self.initial = (3, 3, 1)  # (missionaries left, cannibals left, boat left=1)
        self.goal = (0, 0, 0)
    
    def is_safe(self, state: Tuple[int, int, int]) -> bool:
        """Check if state is valid (missionaries >= cannibals on each side)"""
        m_left, c_left, boat = state
        m_right = 3 - m_left
        c_right = 3 - c_left
        
        # Check validity
        if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
            return False
        if m_left > 0 and m_left < c_left:
            return False
        if m_right > 0 and m_right < c_right:
            return False
        return True
    
    def get_successors(self, state: Tuple[int, int, int]) -> List[Tuple]:
        """Generate successor states"""
        m_left, c_left, boat = state
        successors = []
        
        if boat == 1:  # Boat on left, move right
            moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
            for m, c in moves:
                new_state = (m_left - m, c_left - c, 0)
                if self.is_safe(new_state):
                    successors.append((new_state, f'Move {m}M, {c}C right'))
        else:  # Boat on right, move left
            m_right = 3 - m_left
            c_right = 3 - c_left
            moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
            for m, c in moves:
                if m <= m_right and c <= c_right:
                    new_state = (m_left + m, c_left + c, 1)
                    if self.is_safe(new_state):
                        successors.append((new_state, f'Move {m}M, {c}C left'))
        
        return successors
    
    def is_goal(self, state: Tuple[int, int, int]) -> bool:
        """Check if all reached goal state"""
        return state == self.goal
