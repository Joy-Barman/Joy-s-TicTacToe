

import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
       
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def get_random_first_player(self):
       
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        
        self.board[row][col] = player

    def has_player_won(self, player):
        
        n = len(self.board)
        for i in range(n):
            
            if all(self.board[i][j] == player for j in range(n)):
                return True

            if all(self.board[j][i] == player for j in range(n)):
                return True

        
        if all(self.board[i][i] == player for i in range(n)):
            return True
        if all(self.board[i][n - i - 1] == player for i in range(n)):
            return True

        return False

    def is_board_filled(self):
        
        return all(self.board[i][j] != '-' for i in range(3) for j in range(3))

    def swap_player_turn(self, player):
        
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        
        for row in self.board:
            print(' '.join(row))
        print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'Player {player} turn')

                
                row, col = list(map(int, input('Enter row & column numbers to fix spot: ').split()))
                print()

                
                row -= 1
                col -= 1

                
                if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == '-':
                    self.fix_spot(row, col, player)

                    
                    if self.has_player_won(player):
                        print(f'Player {player} wins the game!')
                        game_over = True
                    elif self.is_board_filled():
                        print('Match Draw!')
                        game_over = True
                    else:
                        player = self.swap_player_turn(player)
                else:
                    print('Invalid spot. Try again!')

            except ValueError as err:
                print(err)

        print()
        self.show_board()


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()