import time
from typing import Callable

from .search.astar import AStarSearch
from .search.gbfs import GreedyBestFirstSearch
from .search.bfs import BreadthFirstSearch
from .search.dfs import DepthFirstSearch
from .search.ucs import UniformCostSearch
from .search.goright import GoRight
from .models.grid import Grid
from .models.solution import Solution
from .models.search_types import Search
from .models.search_types import Search

SearchFunction = Callable[[Grid], Solution]

SEARCH: dict[Search, SearchFunction] = {
    Search.GO_RIGHT: GoRight.search,    
    Search.BREADTH_FIRST_SEARCH: BreadthFirstSearch.search,
    Search.UNIFORM_COST_SEARCH: UniformCostSearch.search,
    Search.DEPTH_FIRST_SEARCH: DepthFirstSearch.search, 
    Search.GREEDY_BEST_FIRST_SEARCH: GreedyBestFirstSearch.search,
    Search.ASTAR_SEARCH: AStarSearch.search,
}


class PathFinder:
    @staticmethod
    def find_path(
        grid: Grid,
        search: Search,
    ) -> Solution:
        start_time = time.perf_counter()
        solution = SEARCH[search](grid)
        time_taken = (time.perf_counter() - start_time) * 1000
        solution.time = time_taken

        return solution
