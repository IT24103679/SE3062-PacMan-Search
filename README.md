# SE3062-PacMan-Search
Search Algorithms in Pac-Man - SE3062 Group Assignment


MEMBER 1 — Q1 (DFS) + Q2 (BFS)
 
 Q1 — DFS Terminal Commands

  python autograder.py -q q1

  python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
 
 Q2 — BFS Terminal Commands

  python autograder.py -q q2

  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs



MEMBER 2 — Q3 (UCS) + Q4 (A*)

 Q3 — UCS Terminal Commands

  python autograder.py -q q3

  python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

 Q4 — A* Terminal Commands
 
  python autograder.py -q q4

  python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=nullHeuristic
  python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic




MEMBER 3 — Q5 (CornersProblem) + Q6 (Corners Heuristic)

 Q5 — CornersProblem Terminal Commands

  python autograder.py -q q5

  python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

 Q6 — Corners Heuristic Terminal Commands

  python autograder.py -q q6

  python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5



MEMBER 4 — Q7 (Food Heuristic) + End Section
 
 Q7 — Food Heuristic Terminal Commands

  python autograder.py -q q7

  python pacman.py -l smallSearch -p AStarFoodSearchAgent

 



