import numpy as np

# Sudoku solver project

def find_empty_spot(our_sudoku):
    
    for row in range(9):
        for col in range(9):  
            if our_sudoku[row][col] == -1:
                return row, col

    return None, None  # if no empty spaces were spotted return null


def is_valid(our_sudoku, our_guess, current_row, current_col):
    
    # let's start with the row
    list_of_this_row = our_sudoku[current_row]   
    if our_guess in list_of_this_row:
        return False  

    # now the column
    # copy this specific entire column in a new list called list_of_this_col
    list_of_this_col = [our_sudoku[i][current_col] for i in range(9)]
    if our_guess in list_of_this_col:
        return False  

    square_first_row = (current_row // 3) * 3
    
    square_first_col = (current_col // 3) * 3

    # move from square's first row up to last row in that square
    for row in range(square_first_row, square_first_row + 3):
        # move from square's first column up to last column in that square
        for col in range(square_first_col, square_first_col + 3):
            if our_sudoku[row][col] == our_guess:
                # if our guess was spotted in it's square return false because we have violated sudoku rules
                return False

    return True  # our guess is valid option


def solver(our_sudoku):
   

    # step 1: find a empty space on the Sudoku to mutate it
    current_row, current_col = find_empty_spot(our_sudoku)

    # step 1.1: if there's no empty spaces left in our Sudoku which means we're done return True (Sudoku is solved)
    if current_row is None:  # this is true if our find_empty_spot function returns (None, None)
        return True

    # step 2: if there is an empty place on our Sudoku, guess a number between 1 .. 9
    for our_guess in range(1, 10):  
        # step 3: check if our guess is valid using sudoku rules (row, col, block are valid)
        if is_valid(our_sudoku, our_guess, current_row, current_col):
            # step 3.1: if our guess is a valid answer put it on that spot in our Sudoku
            our_sudoku[current_row][current_col] = our_guess
            # step 4: then we call our solver function recursively with our updated Sudoku
            if solver(our_sudoku):
                return True        # once our Sudoku is fully solved return True

        # step 5: if our guess isn't valid or Sudoku couldn't be solved, Backtrack and revert spot on the Sudoku to -1
        our_sudoku[current_row][current_col] = -1

    # step 6: if none of our guesses worked, it indicates that this Sudoku can't be solved
    return False


if __name__ == '__main__':

    sudoku = [
        [5, 3, -1,     -1, 7, -1,     -1, -1, -1],
        [6, -1, -1,      1, 9, 5,     -1, -1, -1],
        [-1, 9, 8,    -1, -1, -1,      -1, 6, -1],

        [8, -1, -1,     -1, 6, -1,     -1, -1, 3],
        [4, -1, -1,      8, -1, 3,     -1, -1, 1],
        [7, -1, -1,     -1, 2, -1,     -1, -1, 6],

        [-1, 6, -1,     -1, -1, -1,      2, 8, -1],
        [-1, -1, -1,       4, 1, 9,     -1, -1, 5],
        [-1, -1, -1,      -1, 8, -1,      -1, 7, 9]
    ]

print(solver(sudoku))  # solve our Sudoku then print the result which if it was successful or not
print(np.matrix(sudoku))
