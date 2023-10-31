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
    print(board_format.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))


def check_win(board):
    win_combos = [  # These are the indexes of all the possible ways to win
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal (top left to bottom right)
        [2, 4, 6],  # Diagonal (top right to bottom left)
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False


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
    print("The current results are: X: {}, O: {}, Tie: {}".format(results["X"], results["O"], results["Tie"]))


winner = False
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
current_player = "X"
while not winner:
    display_board(board)
    print("It is {}'s turn.".format(current_player))
    move = input("Where would you like to move? ")
    if move.lower() in ["exit", "quit", "q", "x"]:
        print("Stopping game... Goodbye!")
        exit()
    if move.lower() in ["a1", "1a"]:
        board[0] = current_player
    elif move.lower() in ["b1", "1b"]:
        board[1] = current_player
    elif move.lower() in ["c1", "1c"]:
        board[2] = current_player
    elif move.lower() in ["a2", "2a"]:
        board[3] = current_player
    elif move.lower() in ["b2", "2b"]:
        board[4] = current_player
    elif move.lower() in ["c2", "2c"]:
        board[5] = current_player
    elif move.lower() in ["a3", "3a"]:
        board[6] = current_player
    elif move.lower() in ["b3", "3b"]:
        board[7] = current_player
    elif move.lower() in ["c3", "3c"]:
        board[8] = current_player
    else:
        print("That is not a valid move.")
        continue
    if check_win(board):
        winner = current_player
    elif check_tie(board):
        winner = "Tie"
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
