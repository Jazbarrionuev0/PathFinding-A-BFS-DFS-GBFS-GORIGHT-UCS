from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def manjaran(node, objetivo):
    discol = abs(node.state[0] - objetivo[0])
    disfil = abs(node.state[1] - objetivo[1])
    return discol + disfil

class AStarSearch:

    @staticmethod
    def search(grid: Grid) -> Solution:
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {node.state: node}

        # Add the node to the explored dictionary
        # explored[node.state] = True

        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost + manjaran(node, grid.end))

        while True:
            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.pop()

            if grid.end == node.state:
                return Solution(node, explored)

            neighbours = grid.get_neighbours(node.state)

            for action in neighbours.keys():
                new_state = neighbours[action]
                new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                new_node.parent = node
                new_node.action = action

                if new_node.state not in explored.keys() or new_node.cost < explored[new_node.state].cost:
                    estimated_distance = new_node.cost + manjaran(new_node, grid.end)
                    explored[new_node.state] = new_node
                    frontier.add(new_node, estimated_distance)