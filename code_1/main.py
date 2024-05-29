
board =[
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
board_1 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
board_3 = [[".",".","5",".",".",".",".",".","."],
           ["1",".",".","2",".",".",".",".","."],
           [".",".","6",".",".","3",".",".","."],
           ["8",".",".",".",".",".",".",".","."],
           ["3",".","1","5","2",".",".",".","."],
           [".",".",".",".",".",".",".","4","."],
           [".",".","6",".",".",".",".",".","."],
           [".",".",".",".",".",".",".","9","."],
           [".",".",".",".",".",".",".",".","."]
        ]

def array_checker(array): 
    checker = []
    for i in array:        
        if i == ".":
            pass
        else:
            if i in checker:
                print(checker, i)
                return False
            else:
                checker.append(i)                      
    return True

def check_rows(board):    
    for row in board:
        if len(row) != 9:
            return False
        else:
            #print(row)
            if array_checker(row)  is False:
                return False   
    return True
            
def check_columns(board):    
    for i in range(9):  
        column = []   
        for j in range(9):
            column.append(board[j][i])
        #print(column)
        if array_checker(column) is False:
            return False
    return True

def check_blocks(board):
    a, b = 0 , 0
    block_element = []
    for i in range(a+3):      
        for j in range(b+3):
            block_element.append(board[i][j])  
    #print(block_element)
    checker = array_checker(block_element)
    if checker is False:
        return False
    
    block_element = []   
    for i in range(a+3):
        for j in range(b+3, b+6):
            block_element.append(board[i][j])
    #print(block_element) 
    checker = array_checker(block_element)
    if checker is False:
        return False  
    block_element = [] 
    for i in range(a+3):
        for j in range(b+6, b+9):
            block_element.append(board[i][j])   
    #print(block_element)
    checker = array_checker(block_element)
    if checker is False:
        return False
    
    block_element = []
    for i in range(a+3, a+6):
        for j in range(b+3):
            block_element.append(board[i][j])  
    #print(block_element)
    checker = array_checker(block_element)
    if checker is False:
        return False
    
    block_element = [] 
    for i in range(a+3, a+6):
        for j in range(b+3, b+6):
            block_element.append(board[i][j])  
    #print(block_element)
    checker = array_checker(block_element)
    if checker is False:
        return False
    
    block_element = [] 
    for i in range(a+3, a+6):
        for j in range(b+6, b+9):
            block_element.append(board[i][j])  
    #print(block_element)
    checker = array_checker(block_element)
    if checker is False:
        return False
    
    block_element = [] 
    for i in range(a+6, a+9):
        for j in range(b+3):
            block_element.append(board[i][j])  
    #print(block_element)
    checker = array_checker(block_element)
    if checker is False:
        return False
    
    block_element = [] 
    for i in range(a+6, a+9):
        for j in range(b+3, b+6):
            block_element.append(board[i][j])  
    #print(block_element)
    checker = array_checker(block_element)
    if checker is False:
        return False
    
    block_element = [] 
    for i in range(a+6, a+9):
        for j in range(b+6, b+9):
            block_element.append(board[i][j])  
    #print(block_element)
    checker = array_checker(block_element)
    if checker is False:
        return False

    return True

def sudoku_validator(board):
    row = check_rows(board)
    if row is False:
        return False
    elif check_columns(board) is False:
        return False
    else:
        if check_blocks(board) is False:
            return False        
    return True

# print(array_checker(['5', '3', '.', '.', '.', '.', '.', '7', '.']))
print(check_blocks(board_3))