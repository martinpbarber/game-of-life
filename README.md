# Game of Life

## Overview

A Conway Game of Life implementation in Python. This implementation tracks only live cells as opposed to tracking live and dead cells on a board as many implementations do. 

## Classes

### Game

The entry point for a Game of Life. A Game requires a Seed, which provides the starting live cells.
Executing the tick() function moves the game to the next generation. Live cells can be accessed via the live_cells() function. 

### Seed

The initial generation for the Game of Life. Live cells are added to the Seed before it is used to begin a Game using the add_live_cell() function.

### Cell

A simple class to track the position of a cell. A cell can provide it's neighbor cells using the get_neighbors() function.

### Generation

A private class that can compute a subsequent generation based on a previous generation. The logic of the game is captured in this class.
