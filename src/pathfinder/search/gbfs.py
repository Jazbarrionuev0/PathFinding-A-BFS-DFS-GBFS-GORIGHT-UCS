from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node



def manjaran(node, objetivo):
    discol = abs(node.state[0] - objetivo[0])
    disfil = abs(node.state[1] - objetivo[1])
    dist = discol**2 + disfil**2
    return dist**(1/2)




class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = node

        if node.state == grid.end:
            return Solution(node, explored)

        frontier =  PriorityQueueFrontier()
        frontier.add(node, manjaran(node,grid.end))
        
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

                if new_node.state not in explored or new_node.cost < explored[new_node.state].cost:
                    explored[new_node.state] = new_node
                    frontier.add(new_node, manjaran(new_node, grid.end))