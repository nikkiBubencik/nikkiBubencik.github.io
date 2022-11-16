class TicTacToe:
    """
    Class to play tic-tac-toe
    2 player game first to get 3 in a row wins
    """

    def __init__(self) -> None:
        """
        initializes board and start player
        """
        self.board: [[str]] = []
        self.player: str = 'X'

    def setup_board(self) -> None:
        """
        makes board all elements are equal to '.' which means spot is empty
        :return:
        """
        for i in range(3):
            row = []
            for j in range(3):
                row.append('.')
            self.board.append(row)

    def swap_player(self) -> None:
        """
        switches player from 'X' to 'O' or vice versa
        :return:
        """
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def change_spot(self, row: int, col: int) -> None:
        """
        changes board spot to the player whose turns it is
        :param row: row to change
        :param col: column to change
        :return:
        """
        self.board[row][col] = self.player

    def check_empty_spot(self, row: int, col: int) -> bool:
        """
        checks to see if a player has already chosen that spot
        :param row: user inputted row
        :param col: user inputted column
        :return: True if spot is empty False otherwise
        """
        if self.board[row - 1][col - 1] == '.':
            return True
        return False

    def check_board_filled(self) -> bool:
        """
        loops through the board and checks to see if any spot is empty
        :return: True if the board is filled False otherwise
        """
        for i in range(len(self.board)):
            if self.board[i].count('.') > 0:
                return False
        return True

    def check_win(self) -> bool:
        """
        checks all possible ways of winning; straight lines or diagonals
        :return:  True if a player has three in a row False otherwise
        """
        n = len(self.board)
        if self.check_row(n) or self.check_col(n) or self.check_diagonal1(n) or self.check_diagonal2(n):
            return True
        return False

    def check_row(self,  n: int) -> bool:
        """
        checks all rows in board to see if the player has 3 in a row
        :param n: length of board
        :return: True if player has 3 in a row False otherwise
        """
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != self.player:
                    win = False
                    break
            if win:
                return win
        return False

    def check_col(self, n: int) -> bool:
        """
        checks all columns in board to see if the player has 3 in a row
        :param n: length of board
        :return: True if player has 3 in a row False otherwise
        """
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != self.player:
                    win = False
                    break
            if win:
                return win
        return False

    def check_diagonal1(self, n: int) -> bool:
        """
        checks the diagonal ("\") in board to see if the player has 3 in a row
        :param n: length of board
        :return: True if player has 3 in a row False otherwise
        """
        win = True
        for i in range(n):
            if self.board[i][i] != self.player:
                win = False
                break
        if win:
            return win
        return False

    def check_diagonal2(self, n: int):
        """
        checks the diagonal ("/") in board to see if the player has 3 in a row
        :param n: length of board
        :return: True if player has 3 in a row False otherwise
        """
        win = True
        for i in range(n):
            if self.board[i][n - i - 1] != self.player:
                win = False
                break
        if win:
            return True
        return False

    def display_board(self) -> None:
        """
        prints out the game board
        :return:
        """
        for i in range(len(self.board)):
            for j in self.board[i]:
                print(j, end=" ")
            print()

    def get_user_input(self) -> None:
        """
        get user inputted row and column
        if not a valid row or column changes board[row][col] value
        :return:
        """
        while True:
            try:
                row = int(input("Enter a row "))
                col = int(input("Enter a column: "))
                if row < 1 or col < 1:
                    print("Please enter a valid row and colum; enter 1, 2, or 3")
                    continue
                if not self.check_empty_spot(row, col):
                    print("Pick an empty spot")
                    continue
                self.change_spot(row - 1, col - 1)
                break
            except ValueError:
                print("Please enter a valid number for row and colum; enter 1, 2, or 3")
            except IndexError:
                print("Please enter a valid row and colum; enter 1, 2, or 3")

    def play_game(self):
        """
        method to play the game
        sets up board, shows it, gets changes board value, checks if player won or board is filled, swap player and repeat
        :return: 
        """
        self.setup_board()
        self.display_board()
        while True:
            print("Player", self.player, "turn")
            self.get_user_input()
            # self.display_board()
            if self.check_win():
                print("Player", self.player, "Wins!")
                break
            if self.check_board_filled():
                print("Draw")
                break
            self.swap_player()
            print()
            self.display_board()
        self.display_board()


tic_tac = TicTacToe()
tic_tac.play_game()
