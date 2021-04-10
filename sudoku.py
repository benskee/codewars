row1 = [5, 3, 4, 6, 7, 8, 9, 1, 2]
row2 = [1, 0, 0, 3, 4, 2, 5, 6, 0]

# def valid_row(row):
#     r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
#     if sorted(row) != r:
#         return False
#     else:
#         return True



def valid_solution(board):
    answer = True
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_dict = {
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[],
        9:[]
    }
    grid_dict = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }

    for row in board:
        if sorted(row) != r:
            answer = False
            break

    for row in board:
        for cell in range(9):
            my_dict[cell+1].append(row[cell])
    
    for row in my_dict.values():
        if sorted(row) != r:
            answer = False
            break
    
    for i in range(9):
        row = board[i]
        if i < 3:
            grid_dict[1] += row[0:3]
            grid_dict[2] += row[3:6]
            grid_dict[3] += row[6:]
        elif i < 6:
            grid_dict[4] += row[0:3]
            grid_dict[5] += row[3:6]
            grid_dict[6] += row[6:]
        else:
            grid_dict[7] += row[0:3]
            grid_dict[8] += row[3:6]
            grid_dict[9] += row[6:]

    for row in grid_dict.values():
        if sorted(row) != r:
            answer = False
            break

    return answer

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]))
