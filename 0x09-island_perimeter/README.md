# Island Perimeter

This directory contains a Python script to solve the **"Island Perimeter"** problem.

## Description

The task is to create a function `def island_perimeter(grid):` that calculates the perimeter of an island represented as a grid. The grid is a rectangular list of lists where:

- `0` represents water.
- `1` represents land.

### Rules:

- Each cell in the grid is square with a side length of 1.
- Cells are connected horizontally or vertically (not diagonally).
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island does not have any internal lakes.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- The code is interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All files must end with a new line.
- The first line of all Python files must be exactly `#!/usr/bin/python3`.
- A `README.md` file is mandatory in the root of the project.
- Your code must follow PEP 8 style guidelines (version 1.7).
- No module imports are allowed.
- All functions must be documented.
- All files must be executable.

## File Structure

- **`0-island_perimeter.py`**: Contains the implementation of the `island_perimeter` function.
- **`0-main.py`**: A test file to verify the functionality of `island_perimeter`.

## Example

Input grid:

```python
[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```
Expected Output:

12
