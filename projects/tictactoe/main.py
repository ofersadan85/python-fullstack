import json


def display_board(board):
    board_format = """
    A | B | C
    -----------
      |   |
 1| {} | {} | {}
      |   |
    -----------
      |   |
 2| {} | {} | {}
      |   |
    -----------
      |   |
 3| {} | {} | {}"""
    print(
        board_format.format(
            board[0][0],
            board[0][1],
            board[0][2],
            board[1][0],
            board[1][1],
            board[1][2],
            board[2][0],
            board[2][1],
            board[2][2],
        )
    )


def check_win(board):
    x_wins = ["X", "X", "X"]
    o_wins = ["O", "O", "O"]

    for i in range(3):
        column = [board[0][i], board[1][i], board[2][i]]
        row = [board[i][0], board[i][1], board[i][2]]
        if column in [x_wins, o_wins] or row in [x_wins, o_wins]:
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    # win_combos = [  # These are the indexes of all the possible ways to win
    #     [0, 1, 2],  # Top row
    #     [3, 4, 5],  # Middle row
    #     [6, 7, 8],  # Bottom row
    #     [0, 3, 6],  # Left column
    #     [1, 4, 7],  # Middle column
    #     [2, 5, 8],  # Right column
    #     [0, 4, 8],  # Diagonal (top left to bottom right)
    #     [2, 4, 6],  # Diagonal (top right to bottom left)
    # ]
    # for combo in win_combos:
    #     if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
    #         return True
    # return False


def check_tie(board):
    if not check_win(board) and " " not in board:
        return True
    else:
        return False


def save_results(winner):
    try:
        results_file = open("results.json", "r+")
    except FileNotFoundError:
        results_file = open("results.json", "w")
        if winner == "Tie":
            results = {"X": 0, "O": 0, "Tie": 1}
        elif winner == "X":
            results = {"X": 1, "O": 0, "Tie": 0}
        elif winner == "O":
            results = {"X": 0, "O": 1, "Tie": 0}
        json.dump(results, results_file)
        results_file.close()
    else:
        results = json.load(results_file)
        if winner == "Tie":
            results["Tie"] = results["Tie"] + 1
        elif winner == "X":
            results["X"] = results["X"] + 1
        elif winner == "O":
            results["O"] = results["O"] + 1
        results_file.seek(0)
        json.dump(results, results_file)
        results_file.close()
    print(
        "The current results are: X: {}, O: {}, Tie: {}".format(
            results["X"], results["O"], results["Tie"]
        )
    )


winner = False
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


current_player = "X"
while not winner:
    display_board(board)
    print("It is {}'s turn.".format(current_player))
    move = input("Where would you like to move? ")
    move = move.lower()
    if move in ["exit", "quit", "q", "x"]:
        print("Stopping game... Goodbye!")
        exit()

    columns = {"a": 0, "b": 1, "c": 2}
    rows = {"1": 0, "2": 1, "3": 2}

    for letter in move:
        if letter in columns.keys():
            column = columns[letter]
    for letter in move:
        if letter in rows.keys():
            row = rows[letter]
    try:
        if board[row][column] != " ":
            # print("That is not a valid move.")
            # continue
            raise NameError
        board[row][column] = current_player
    except NameError:
        print("That is not a valid move.")
        continue

    if check_win(board):
        winner = current_player
    # elif check_tie(board):
    #     winner = "Tie"
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

display_board(board)
if winner == "Tie":
    print("It's a tie!")
else:
    print("Congratulations, {} wins!".format(winner))
save_results(winner)
