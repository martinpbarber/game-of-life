class Game:
    def __init__(self, seed):
        self._generation = seed

    def live_cells(self):
        return self._generation.live_cells()

    def tick(self):
        generation = Generation(self._generation)
        self._generation = generation
 
class Cell:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    def get_neighbors(self):
        x = self.x
        y = self.y
        neighbor_cells = (
           Cell(x-1, y-1), Cell(x-1, y), Cell(x-1, y+1), 
           Cell(x, y-1),                 Cell(x, y+1), 
           Cell(x+1, y-1), Cell(x+1, y), Cell(x+1, y+1), 
        )
        return neighbor_cells

    def __eq__(self, other):
        if isinstance(other, Cell):
            return (self.x == other.x) and (self.y == other.y)
        return False

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

class Seed:
    def __init__(self):
        self._live_cells = set()

    def add_live_cell(self, cell):
        self._live_cells.add(cell)

    def live_cells(self):
        return set(self._live_cells)

class Generation:
    def __init__(self, previous_generation):
        self._previous_generation = previous_generation
        self._live_cells = self._next_generation()

    def live_cells(self):
        return set(self._live_cells)

    def _next_generation(self):
        live_cells = set()
        for live_cell in self._previous_generation.live_cells():
            if self._live_cell_still_alive(live_cell):
                live_cells.add(live_cell)
            for revived_neighbor in self._find_revived_neighbors(live_cell):
                live_cells.add(revived_neighbor)
        return live_cells

    def _live_cell_still_alive(self, cell):
        num_live_neighbors = self._num_live_neighbors(cell)
        if num_live_neighbors == 2 or num_live_neighbors == 3:
            return True 
        return False

    def _num_live_neighbors(self, cell):
        num_live_neighbors = 0
        for neighbor in cell.get_neighbors():
            if neighbor in self._previous_generation.live_cells():
                num_live_neighbors += 1
        return num_live_neighbors

    def _find_revived_neighbors(self, cell):
        revived_neighbors = set()
        for dead_cell in self._dead_neighbors(cell):
            if self._is_dead_cell_revived(dead_cell):
                revived_neighbors.add(dead_cell)
        return revived_neighbors

    def _dead_neighbors(self, cell):
        dead_neighbors = []
        for neighbor in cell.get_neighbors():
            if neighbor not in self._previous_generation.live_cells():
                dead_neighbors.append(neighbor)
        return dead_neighbors

    def _is_dead_cell_revived(self, dead_cell):
        num_live_neighbors = self._num_live_neighbors(dead_cell)
        if num_live_neighbors == 3:
            return True
        return False
