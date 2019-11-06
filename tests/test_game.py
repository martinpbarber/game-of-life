from game_of_life import Game, Seed, Cell

import pytest

@pytest.fixture
def seed():
    return Seed()

def test_no_live_cells(seed):
    game = Game(seed)

    game.tick()
    assert len(game.live_cells()) == 0

def test_cell_with_no_neighbor_dies(seed):
    seed.add_live_cell(Cell(0,0))
    game = Game(seed)

    game.tick()
    assert len(game.live_cells()) == 0
    
def test_two_neighbor_cells_both_die(seed):
    seed.add_live_cell(Cell(0,0))
    seed.add_live_cell(Cell(1,0))
    game = Game(seed)

    game.tick()
    assert len(game.live_cells()) == 0

def test_cell_with_two_neighbors_lives(seed):
    seed.add_live_cell(Cell(0,0))
    seed.add_live_cell(Cell(1,1))
    seed.add_live_cell(Cell(1,-1))
    game = Game(seed)

    game.tick()
    assert Cell(0,0) in game.live_cells()

def test_dead_cell_with_three_live_neighbors_revive(seed):
    seed.add_live_cell(Cell(0,0))
    seed.add_live_cell(Cell(1,0))
    seed.add_live_cell(Cell(0,1))
    game = Game(seed)

    game.tick()
    assert Cell(1,1) in game.live_cells()

def test_cell_with_four_neighbors_die(seed):
    seed.add_live_cell(Cell(0,0))
    seed.add_live_cell(Cell(1,1))
    seed.add_live_cell(Cell(1,-1))
    seed.add_live_cell(Cell(-1,1))
    seed.add_live_cell(Cell(-1,-1))
    game = Game(seed)

    game.tick()
    assert Cell(0,0) not in game.live_cells()

def test_blinker(seed):
    seed.add_live_cell(Cell(0,0))
    seed.add_live_cell(Cell(1,0))
    seed.add_live_cell(Cell(2,0))
    game = Game(seed)

    game.tick()
    assert Cell(1,1) in game.live_cells()
    assert Cell(1,0) in game.live_cells()
    assert Cell(1,-1) in game.live_cells()
    game.tick()
    assert Cell(0,0) in game.live_cells()
    assert Cell(1,0) in game.live_cells()
    assert Cell(2,0) in game.live_cells()

def test_block(seed):
    seed.add_live_cell(Cell(0,0))
    seed.add_live_cell(Cell(1,0))
    seed.add_live_cell(Cell(0,-1))
    seed.add_live_cell(Cell(1,-1))
    game = Game(seed)

    game.tick()
    assert Cell(0,0) in game.live_cells()
    assert Cell(1,0) in game.live_cells()
    assert Cell(0,-1) in game.live_cells()
    assert Cell(1,-1) in game.live_cells()

def test_tub(seed):
    seed.add_live_cell(Cell(0,0))
    seed.add_live_cell(Cell(-1,-1))
    seed.add_live_cell(Cell(1,-1))
    seed.add_live_cell(Cell(0,-2))

    game = Game(seed)
    assert Cell(0,0) in game.live_cells()
    assert Cell(-1,-1) in game.live_cells()
    assert Cell(1,-1) in game.live_cells()
    assert Cell(0,-2) in game.live_cells()
