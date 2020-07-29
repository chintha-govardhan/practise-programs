import datetime

test_data = '''
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0
'''

def is_duplicate_exist(entry_list):

    empty_count = entry_list.count(0)
    values = [ x for x in entry_list if x != 0 ]

    if min(values) < 1 or max(values) > 9:
        print("ERROR: incorrect values in list ", entry_list)
        exit(1)

    if (len(set(values)) + empty_count) != 9:
          return True
    return False

def is_valid(grid):

    # row and column validation
    for i in range(9):
        for j in range(9):
          if not is_valid_entry(grid, i, j):
              return False
    return True

def is_valid_entry(grid, row_index, col_index):

    # row and column validation
    row_data = grid[row_index]
    column_data = [grid[j][col_index] for j in range(9)]

    # grid data
    grid_row_index = row_index - (row_index % 3)
    grid_col_index = col_index - (col_index % 3)

    grid_data = [ grid[i][j] for i in range(grid_row_index, grid_row_index+3)
                  for j in range(grid_col_index, grid_col_index+3)]

#    print "row_data", row_data
#    print "col data", column_data
#    print grid_data

    if is_duplicate_exist(row_data) or is_duplicate_exist(column_data) or \
        is_duplicate_exist(grid_data):
        return False
    return True

def find_empty_location(grid):

    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                 return (row, col)
    return None

recurrsions = 0

def solve_sudoku(grid):

    global recurrsions
    recurrsions += 1
    empty_location = find_empty_location(grid)

    if not empty_location:
        return True

    row, col = empty_location
    for i in range(1,10):

        grid[row][col] = i
        if is_valid_entry(grid, row, col):
            if solve_sudoku(grid):
                return True
        grid[row][col] = 0

    return False


def print_sudoku(grid):

    for i in range(9):
        data = '\t'.join(list(map(str, grid[i])))
        print(data)

def log_time(fun):

    def wrap_fun(*args, **kwargs):
        start_time = datetime.datetime.now()
        fun(*args, **kwargs)
        end_time = datetime.datetime.now()
        print("Time taken: ", (end_time - start_time))
    return wrap_fun

@log_time
def test_prog():

    data = test_data.strip().splitlines()
    grid = []
    for entry in data:
        grid.append(list(map(int, entry.split())))

    print("Input Sudoku:")
    print_sudoku(grid)
    print("#" * 30)
    if solve_sudoku(grid):
        print("Sudoku Solution")
        print_sudoku(grid)
    else:
        print("Solution not found")

    print("recurrsions", recurrsions)

def main():

    print("*" * 80)
    print("Welcome to Sudoku solver")
    print("Instructions for the input")
    print("Enter each row in a line and each cell separated by a space")
    print("Use 0 in place of empty cell")
    print("*" * 80)

    print("Enter sudoku puzzle")
    print("")

    data = []
    for i in range(9):
        row = raw_input()
        row = [ int(x) for x in row.strip().split() ]
        if len(row) != 9:
            print("Error input: Row should contain exactly 9 entries only")
            print(row)
            exit(1)
        data.append(row)

    if not is_valid(data):
        print("Error: Input puzzle is not valid")
        exit(1)

    if solve_sudoku(data):
        print("Sudoku Solution")
        print_sudoku(data)
    else:
        print("Solution not found")

if __name__ == '__main__':
    test_prog()
    #main()
