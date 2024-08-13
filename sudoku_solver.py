def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0], l[1] = row, col
                return True
    return False

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num):
    return num in [grid[row][col] for row in range(9)]

def used_in_box(grid, box_start_row, box_start_col, num):
    return num in [grid[i][j] for i in range(box_start_row, box_start_row + 3) for j in range(box_start_col, box_start_col + 3)]

def check_location_is_safe(grid, row, col, num):
    return (not used_in_row(grid, row, num) and
            not used_in_col(grid, col, num) and
            not used_in_box(grid, row - row % 3, col - col % 3, num))

def solve_sudoku(grid):
    l = [0, 0]

    if not find_empty_location(grid, l):
        return True

    row, col = l[0], l[1]

    for num in range(1, 10):
        if check_location_is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

if __name__ == "__main__":
    sudoku_grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    if solve_sudoku(sudoku_grid):
        print("Sudoku grid solved successfully:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")