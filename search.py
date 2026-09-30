# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# DFS
def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

 # Create a Stack for the fringe (LIFO - Last In First Out)
    fringe = util.Stack()
    
    # Push the start state as a tuple: (state, actions, cost)
    startState = problem.getStartState()
    fringe.push((startState, [], 0))
    
    # Track expanded states to avoid revisiting (graph search)
    expanded = set()
    
    while not fringe.isEmpty():
        # Pop the most recently added node from the stack
        state, actions, cost = fringe.pop()
        
        # Check if this state is the goal
        if problem.isGoalState(state):
            return actions
        
        # Only expand the state if it hasn't been expanded before
        if state not in expanded:
            expanded.add(state)
            
            # Get all successors of the current state
            for successor, action, stepCost in problem.getSuccessors(state):
                newActions = actions + [action]
                newCost = cost + stepCost
                fringe.push((successor, newActions, newCost))
    
    # Return empty list if no goal was found (failure)
    return []



# BFS
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

# Create a Queue for the fringe (FIFO - First In First Out)
    fringe = util.Queue()
    
    # Push the start state as a tuple: (state, actions, cost)
    startState = problem.getStartState()
    fringe.push((startState, [], 0))
    
    # Track expanded states to avoid revisiting (graph search)
    expanded = set()
    
    while not fringe.isEmpty():
        # Pop the oldest node from the queue
        state, actions, cost = fringe.pop()
        
        # Check if this state is the goal
        if problem.isGoalState(state):
            return actions
        
        # Only expand the state if it hasn't been expanded before
        if state not in expanded:
            expanded.add(state)
            
            # Get all successors of the current state
            for successor, action, stepCost in problem.getSuccessors(state):
                newActions = actions + [action]
                newCost = cost + stepCost
                fringe.push((successor, newActions, newCost))
    
    # Return empty list if no goal was found (failure)
    return []


    

# uniformCostSearch

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

# Create a PriorityQueue for the fringe (ordered by accumulated cost)
    fringe = util.PriorityQueue()
    
    # Push the start state with priority 0 (no cost yet)
    startState = problem.getStartState()
    fringe.push((startState, [], 0), 0)
    
    # Track expanded states to avoid revisiting (graph search)
    expanded = set()
    
    while not fringe.isEmpty():
        # Pop the node with the lowest accumulated cost
        state, actions, cost = fringe.pop()
        
        # Check if this state is the goal
        if problem.isGoalState(state):
            return actions
        
        # Only expand the state if it hasn't been expanded before
        if state not in expanded:
            expanded.add(state)
            
            # Get all successors of the current state
            for successor, action, stepCost in problem.getSuccessors(state):
                newActions = actions + [action]
                newCost = cost + stepCost
                # Priority = accumulated cost (g)
                fringe.push((successor, newActions, newCost), newCost)
    
    # Return empty list if no goal was found (failure)
    return []

    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


# A* Logic

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
# Create a PriorityQueue for the fringe (ordered by f = g + h)
    fringe = util.PriorityQueue()
    
    # Push the start state with priority = heuristic(start)
    startState = problem.getStartState()
    fringe.push((startState, [], 0), heuristic(startState, problem))
    
    # Track expanded states to avoid revisiting (graph search)
    expanded = set()
    
    while not fringe.isEmpty():
        # Pop the node with the lowest f = g + h
        state, actions, cost = fringe.pop()
        
        # Check if this state is the goal
        if problem.isGoalState(state):
            return actions
        
        # Only expand the state if it hasn't been expanded before
        if state not in expanded:
            expanded.add(state)
            
            # Get all successors of the current state
            for successor, action, stepCost in problem.getSuccessors(state):
                newActions = actions + [action]
                newCost = cost + stepCost
                # Priority = g + h (accumulated cost + heuristic)
                priority = newCost + heuristic(successor, problem)
                fringe.push((successor, newActions, newCost), priority)
    
    # Return empty list if no goal was found (failure)
    return []


    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
