from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {node.state:node} 
        
        # Add the node to the explored dictionary
        #explored[node.state] = True
        
        frontier = PriorityQueueFrontier()
        frontier.add(node,node.cost)

        while True:
            if frontier.is_empty():
               return NoSolution(explored)
            
            node = frontier.pop()

            if grid.end == node.state:
                return Solution(node,explored)
            
            neighbours = grid.get_neighbours(node.state)

            for accion in neighbours.keys():
                new_state = neighbours[accion]
                new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                new_node.parent = node
                new_node.action = accion
                
                if new_node.state not in explored.keys() or new_node.cost < explored[new_node.state].cost:
                    explored[new_node.state] = new_node
                    frontier.add(new_node,new_node.cost)





        return NoSolution(explored)
