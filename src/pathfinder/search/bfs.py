from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state = grid.start, cost = 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        explored[node.state] = True

        if grid.end == node.state:
            return Solution(node,explored)

        # Add the node to the explored dictionary
        frontier = QueueFrontier()
        frontier.add(node)
        
        while True:

            if frontier.is_empty():
               return NoSolution(explored)
            
            node = frontier.remove()

            explored[node.state] = True

            
            neighbours = grid.get_neighbours(node.state)

            for accion in neighbours.keys():
                new_state = neighbours[accion]
                new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                new_node.parent = node
                new_node.action = accion

                if grid.end == new_node.state:
                    return Solution(node,explored)
                
                if new_node.state not in explored.keys():
                    explored[new_node.state] = True
                    frontier.add(new_node)
