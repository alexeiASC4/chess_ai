from Piece import *
import random
import sys

class ChessBoard:
    def __init__(self, x_size, y_size):
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.darkbrown = (101, 67, 33)
        self.lightbrown = (188, 158, 130)
        self.grey = (192, 192, 192)
        self.offset_x = 30
        self.offest_y = 30
        self.offset_piece = 10
        self.sqaure_size = 60
        self.is_check = False
        self.white_king_location = (0, 4)
        self.black_king_location = (7, 4)
        self.piece_that_gives_check_location = (-1, -1)
        self.piece_that_gives_pin_location = (-1, -1)
        self.block_check_location = (-1, -1)
        self.black_king_moved = False
        self.white_king_moved = False
        self.piece = None
        self.moves = []
        self.select_piece = True
        self.coords = (0, 0)
        self.current_color = "white"
        self.gameDisplay = pygame.display.set_mode((x_size, y_size))
        self.clock = pygame.time.Clock()
        self.gameExit = False
        self.outcomeDecided = False
        self.bot_king_location = (-1,-1)

        self.white_pawn = ChessPiece("images/white_pawn.png", "white", "pawn", 20)
        self.white_queen = ChessPiece("images/white_queen.png", "white", "queen", 100)
        self.white_knight = ChessPiece("images/white_knight.png", "white", "knight", 50)
        self.white_rook = ChessPiece("images/white_rook.png", "white", "rook", 60)
        self.white_bishop = ChessPiece("images/white_bishop.png", "white", "bishop", 60)
        self.white_king = ChessPiece("images/white_king.png", "white", "king", sys.maxsize)
        self.black_pawn = ChessPiece("images/black_pawn.png", "black", "pawn", 20)
        self.black_queen = ChessPiece("images/black_queen.png", "black", "queen", 100)
        self.black_rook = ChessPiece("images/black_rook.png", "black", "rook", 60)
        self.black_bishop = ChessPiece("images/black_bishop.png", "black", "bishop", 60)
        self.black_knight = ChessPiece("images/black_knight.png", "black", "knight", 50)
        self.black_king = ChessPiece("images/black_king.png", "black", "king", sys.maxsize)
        self.chessBoard = self.init_chess_board()

        pygame.init()
        # background color
        self.gameDisplay.fill(self.white)
        # caption
        pygame.display.set_caption("ChessBoard")

#generates pieces on board 
    def init_chess_board(self):
        chessBoard = [[i for i in range(0, 8)] for j in range(0, 8)]
        chessBoard[1][0] = self.black_pawn
        chessBoard[1][1] = self.black_pawn
        chessBoard[1][2] = self.black_pawn
        chessBoard[1][3] = self.black_pawn
        chessBoard[1][4] = self.black_pawn
        chessBoard[1][5] = self.black_pawn
        chessBoard[1][6] = self.black_pawn
        chessBoard[1][7] = self.black_pawn
        chessBoard[0][0] = self.black_rook
        chessBoard[0][1] = self.black_knight
        chessBoard[0][2] = self.black_bishop
        chessBoard[0][3] = self.black_queen
        chessBoard[0][4] = self.black_king
        chessBoard[0][5] = self.black_bishop
        chessBoard[0][6] = self.black_knight
        chessBoard[0][7] = self.black_rook
        chessBoard[6][0] = self.white_pawn
        chessBoard[6][1] = self.white_pawn
        chessBoard[6][2] = self.white_pawn
        chessBoard[6][3] = self.white_pawn
        chessBoard[6][4] = self.white_pawn
        chessBoard[6][5] = self.white_pawn
        chessBoard[6][6] = self.white_pawn
        chessBoard[6][7] = self.white_pawn
        chessBoard[7][0] = self.white_rook
        chessBoard[7][1] = self.white_knight
        chessBoard[7][2] = self.white_bishop
        chessBoard[7][3] = self.white_queen
        chessBoard[7][4] = self.white_king
        chessBoard[7][5] = self.white_bishop
        chessBoard[7][6] = self.white_knight
        chessBoard[7][7] = self.white_rook

        return chessBoard
# draws the chess board and sets the colors
    def draw_chess_board(self, board):

        color = self.darkbrown

        for i in range(0, 8):
            if (color == self.lightbrown):
                color = self.darkbrown
            else:
                color = self.lightbrown
            for j in range(0, 8):
                pygame.draw.rect(self.gameDisplay, color,
                                 [self.offset_x + self.sqaure_size * j, self.offest_y + self.sqaure_size * i,
                                  self.sqaure_size, self.sqaure_size])
                if (type(board[i][j]) != int):
                    self.gameDisplay.blit(board[i][j].image,
                                          [self.offset_piece + self.offset_x + self.sqaure_size * j,
                                           self.offset_piece + self.offest_y + self.sqaure_size * i])

                if (color == self.lightbrown):
                    color = self.darkbrown
                else:
                    color = self.lightbrown

                for move in self.moves:
                    if i == move[0] and j == move[1]:
                        pygame.draw.circle(self.gameDisplay, self.grey, [30 + self.offset_x + self.sqaure_size * j,
                                                                         30 + self.offest_y + self.sqaure_size * i], 10)
#removes piece by setting coordinate to (-1,-1)
    def remove_piece(self, i, j, board):

        board[i][j] = -1

#moves piece by placing it at a certain coordinate, does not remove piece from previous coordinate, likely must be used in conjunction with remove piece
    def move_piece(self, i, j, piece, board):

        board[i][j] = piece

#checks color returns string
    def check_color(self, i, j, board):
        if board[i][j] == self.black_king or board[i][j] == self.black_queen or board[i][
            j] == self.black_pawn \
                or board[i][j] == self.black_knight or board[i][j] == self.black_rook or \
                board[i][j] == self.black_bishop:
            return "black"
        else:
            return "white"

#returns the piece at a coordinate
    def get_piece(self, i, j, board):
        return board[i][j]

    def check_for_check(self, moves, color):
        king_loc = (-1, -1)
        if color == "black":
            king_loc = self.white_king_location
        else:
            king_loc = self.black_king_location
        for move in moves:
            if move[0] == king_loc[0] and move[1] == king_loc[1]:
                return True

        return False

#this uses rules about how pieces move to check to see if check c an be blocked for all pieces (in the same way for each piece) by checking the coordinates, the only exception is the knight
    def find_locations_that_block_check(self, attacking_piece_location, king_location, board):
        locations = []

        # if check is deliverd by knight, we cannot block check and thus you need to kill the knight
        if type(board[attacking_piece_location[0]][attacking_piece_location[1]]) == ChessPiece:
            if board[attacking_piece_location[0]][attacking_piece_location[1]].piece == "knight":
                return locations

        x = attacking_piece_location[0] - king_location[0]
        y = attacking_piece_location[1] - king_location[1]

        if x == 0 and y > 0:
            for k in range(1, abs(y)):
                locations.append((attacking_piece_location[0], attacking_piece_location[1] - k))
        elif x == 0 and y < 0:
            for k in range(1, abs(y)):
                locations.append((attacking_piece_location[0], attacking_piece_location[1] + k))
        elif x > 0 and y == 0:
            for k in range(1, abs(x)):
                locations.append((attacking_piece_location[0] - k, attacking_piece_location[1]))
        elif x < 0 and y == 0:
            for k in range(1, abs(x)):
                locations.append((attacking_piece_location[0] + k, attacking_piece_location[1]))
        elif x > 0 and y > 0:
            for k in range(1, abs(x)):
                locations.append((attacking_piece_location[0] - k, attacking_piece_location[1] - k))
        elif x < 0 and y > 0:
            for k in range(1, abs(x)):
                locations.append((attacking_piece_location[0] + k, attacking_piece_location[1] - k))
        elif y < 0 and x < 0:
            for k in range(1, abs(x)):
                locations.append((attacking_piece_location[0] + k, attacking_piece_location[1] + k))
        elif y < 0 and x > 0:
            for k in range(1, abs(x)):
                locations.append((attacking_piece_location[0] - k, attacking_piece_location[1] + k))

        return locations

# it checks to see if the attacking piece(s) can snipe the king if current_piece moves and seeminly alters self.piece_that_gives_pin_location, not sure why yet
    def pin(self, i, j, color, pieces, current_piece, king_location, sign, board):
        for k in range(1, 7):
            if self.check_if_opponent_piece(i + k * sign[0], j + k * sign[1], color, board):
                if i + k * sign[0] > 7: continue
                if j + k * sign[1] > 7: continue
                if i + k * sign[0] < 0: continue
                if j + k * sign[1] < 0: continue
                if board[i + k * sign[0]][j + k * sign[1]].piece == pieces[0] or \
                        board[i + k * sign[0]][j + k * sign[1]].piece == pieces[1]:
                    self.remove_piece(i, j, board)
                    possible_moves = self.possible_moves(i + k * sign[0], j + k * sign[1],
                                                         self.get_piece(i + k * sign[0], j + k * sign[1], board), board)
                    self.move_piece(i, j, current_piece, board)
                    for move in possible_moves:
                        if move[0] == king_location[0] and move[1] == king_location[1]:
                            self.piece_that_gives_pin_location = (i + k * sign[0], j + k * sign[1])
                            return True
        return False

    # checks tosee if piece is pinned by observing the rook  queen  and  bishops as  they are the only ones that can pin a piece
    def is_piece_pinned(self, i, j, color, board):
        king_location = (-1, -1)
        if color == "black":
            king_location = self.black_king_location
        else:
            king_location = self.white_king_location

        x = king_location[0] - i
        y = king_location[1] - j
        current_piece = board[i][j]

        if x == 0 and y > 0:
            pieces = ["rook", "queen"]
            sign = [0, -1]
            return self.pin(i, j, color, pieces, current_piece, king_location, sign, board)
        elif x == 0 and y < 0:
            pieces = ["rook", "queen"]
            sign = [0, 1]
            return self.pin(i, j, color, pieces, current_piece, king_location, sign, board)
        elif x > 0 and y == 0:
            pieces = ["rook", "queen"]
            sign = [-1, 0]
            return self.pin(i, j, color, pieces, current_piece, king_location, sign, board)
        elif x < 0 and y == 0:
            pieces = ["rook", "queen"]
            sign = [1, 0]
            return self.pin(i, j, color, pieces, current_piece, king_location, sign, board)
        elif x > 0 and y > 0:
            pieces = ["bishop", "queen"]
            sign = [-1, -1]
            return self.pin(i, j, color, pieces, current_piece, king_location, sign, board)
        elif x < 0 and y > 0:
            pieces = ["bishop", "queen"]
            sign = [1, -1]
            return self.pin(i, j, color, pieces, current_piece, king_location, sign, board)
        elif y < 0 and x < 0:
            pieces = ["bishop", "queen"]
            sign = [1, 1]
            return self.pin(i, j, color, pieces, current_piece, king_location, sign, board)
        elif y < 0 and x > 0:
            pieces = ["bishop", "queen"]
            sign = [-1, 1]
            return self.pin(i, j, color, pieces, current_piece, king_location, sign, board)
        else:
            return False

# for some reason this checks if there isan int at the coordinates given before checking if the piece is our color, might be because the int ios a placeholder when there are no pieces in the place
    def check_if_opponent_piece(self, i, j, my_color, board):
        if i > 7: i = 7
        if j > 7: j = 7
        if i < 0: i = 0
        if j < 0: j = 0
        if type(board[i][j]) != int and self.check_color(i, j, board) != my_color:
            return True
        else:
            return False
# similar situation as above 
    def check_if_team_piece(self, i, j, my_color, board):
        if i > 7: i = 7
        if j > 7: j = 7
        if i < 0: i = 0
        if j < 0: j = 0
        if type(board[i][j]) != int and self.check_color(i, j, board) == my_color:
            return True
        else:
            return False
# yes this confirms theory above, empty spaces have ints 
    def check_if_square_empty(self, i, j, board):
        if i > 7: i = 7
        if j > 7: j = 7
        if i < 0: i = 0
        if j < 0: j = 0
        if type(board[i][j]) == int:
            return True
        else:
            return False


#generates list of coordinates representing list  of possible movesfor bishoprook and king
    def move_bishop_rook_queen(self, i, j, color, sign, moves, board):
        directions = [True] * len(sign)

        for l in range(0, len(sign)):
            for k in range(1, 8):
                if i + k * sign[l][0] > 7: continue
                if i + k * sign[l][0] < 0: continue
                if j + k * sign[l][1] > 7: continue
                if j + k * sign[l][1] < 0: continue

                if (self.check_if_opponent_piece(i + k * sign[l][0], j + k * sign[l][1], color, board)):
                    moves.append((i + k * sign[l][0], j + k * sign[l][1]))
                    break

                if (self.check_if_square_empty(i + k * sign[l][0], j + k * sign[l][1], board) and directions[l]):
                    moves.append((i + k * sign[l][0], j + k * sign[l][1]))
                else:
                    directions[l] = False
                    break
#generates list of coordinates representing list  of possible moves for Knight
    def move_knight(self, i, j, color, sign, moves, board):

        for l in range(0, 8):
            if i + sign[l][0] > 7: continue
            if i + sign[l][0] < 0: continue
            if j + sign[l][1] > 7: continue
            if j + sign[l][1] < 0: continue
            if self.check_if_square_empty(i + sign[l][0], j + sign[l][1], board) or self.check_if_opponent_piece(
                    i + sign[l][0], j + sign[l][1], color, board):
                moves.append((i + sign[l][0], j + sign[l][1]))

#generates list of coordinates representing list  of possible moves for King
    def move_king(self, i, j, color, sign, moves, board):
        for l in range(0, 8):
            if i + sign[l][0] > 7: continue
            if i + sign[l][0] < 0: continue
            if j + sign[l][1] > 7: continue
            if j + sign[l][1] < 0: continue
            if self.check_if_square_empty(i + sign[l][0], j + sign[l][1], board) or self.check_if_opponent_piece(
                    i + sign[l][0], j + sign[l][1], color, board):
                moves.append((i + sign[l][0], j + sign[l][1]))

#generates list of coordinates representing list  of possible moves for pawn
    def move_pawn(self, i, j, color, moves, board):

        if color == "white":
            rank = 6
            sign = -1
        else:
            rank = 1
            sign = 1

        if i == rank and self.check_if_square_empty(i + 1 * sign, j, board) and self.check_if_square_empty(i + 2 * sign,
                                                                                                    j, board):
            moves.append((i + 1 * sign, j))
            moves.append((i + 2 * sign, j))
        if i == rank and self.check_if_square_empty(i + 1 * sign, j, board) and self.check_if_square_empty(i + 2 * sign,
                                                                                                    j, board) and self.check_if_opponent_piece(
            i + 1 * sign, j - 1 * sign, color, board):
            moves.append((i + 1 * sign, j))
            moves.append((i + 2 * sign, j))
            moves.append((i + 1 * sign, j - 1 * sign))
        if i == rank and self.check_if_square_empty(i + 1 * sign, j, board) and self.check_if_square_empty(i + 2 * sign,
                                                                                                    j, board) and self.check_if_opponent_piece(
            i + 1 * sign, j + 1 * sign, color, board):
            moves.append((i + 1 * sign, j))
            moves.append((i + 2 * sign, j))
            moves.append((i + 1 * sign, j + 1 * sign))
        if i == rank and self.check_if_square_empty(i + 1 * sign, j, board) and not self.check_if_square_empty(
                i + 2 * sign,
                j, board):
            moves.append((i + 1 * sign, j))
        if self.check_if_square_empty(i + 1 * sign, j, board):
            moves.append((i + 1 * sign, j))
        if self.check_if_opponent_piece(i + 1 * sign, j + 1 * sign, color, board):
            moves.append((i + 1 * sign, j + 1 * sign))
        if self.check_if_opponent_piece(i + 1 * sign, j - 1 * sign, color, board):
            moves.append((i + 1 * sign, j - 1 * sign))

#return list of possible moves for ChessPiece piece at coords (i,j)
    def possible_moves(self, i, j, piece, board):
        moves = []

        if piece == self.black_pawn:
            self.move_pawn(i, j, "black", moves, board)

        if piece == self.white_pawn:
            self.move_pawn(i, j, "white", moves, board)

        if piece == self.white_king:
            sign = [[1, 1], [0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, -1], [-1, -1]]
            self.move_king(i, j, "white", sign, moves, board)
            self.white_king_location = (i, j)

        if piece == self.black_king:
            sign = [[1, 1], [0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, -1], [-1, -1]]
            self.move_king(i, j, "black", sign, moves, board)
            self.black_king_location = (i, j)

        if piece == self.black_knight:
            sign = [[2, 1], [1, 2], [1, -2], [2, -1], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
            self.move_knight(i, j, "black", sign, moves, board)

        if piece == self.white_knight:
            sign = [[2, 1], [1, 2], [1, -2], [2, -1], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
            self.move_knight(i, j, "white", sign, moves, board)

        if piece == self.black_bishop:
            sign = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
            self.move_bishop_rook_queen(i, j, "black", sign, moves, board)

        if piece == self.white_bishop:
            sign = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
            self.move_bishop_rook_queen(i, j, "white", sign, moves, board)

        if piece == self.black_rook:
            sign = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            self.move_bishop_rook_queen(i, j, "black", sign, moves, board)

        if piece == self.white_rook:
            sign = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            self.move_bishop_rook_queen(i, j, "white", sign, moves, board)

        if piece == self.black_queen:
            sign = [[1, 1], [-1, 1], [1, -1], [-1, -1], [1, 0], [-1, 0], [0, -1], [0, 1]]
            self.move_bishop_rook_queen(i, j, "black", sign, moves, board)

        if piece == self.white_queen:
            sign = [[1, 1], [-1, 1], [1, -1], [-1, -1], [1, 0], [-1, 0], [0, -1], [0, 1]]
            self.move_bishop_rook_queen(i, j, "white", sign, moves, board)

        return moves


    def check_all_pieces_for_check(self, color, board):
        for i in range(0, 8):
            for j in range(0, 8):
                if (type(board[i][j]) == ChessPiece):
                    if board[i][j].color == color:
                        possible_moves = self.possible_moves(i, j, self.get_piece(i, j, board), board)
                        if self.check_for_check(possible_moves, color):
                            self.piece_that_gives_check_location = (i, j)
                            self.is_check = True
                            break

    def find_pawns_attacking_locations(self, color,board):
        attacking_locations = []

        if color == "white":
            sign = [[-1, -1], [-1, 1]]
        else:
            sign = [[1, -1], [1, 1]]
        for i in range(0, 8):
            for j in range(0, 8):
                if (type(board[i][j]) == ChessPiece):
                    if board[i][j].color == color:
                        if board[i][j].piece == "pawn":
                            attacking_locations.append((i + sign[0][0], j + sign[0][1]))
                            attacking_locations.append((i + sign[1][0], j + sign[1][1]))

        attacking_locations = [i for i in attacking_locations if i[0] > -1 and i[1] > -1 and i[0] < 8 and i[1] < 8]
        attacking_locations = list(dict.fromkeys(attacking_locations))

        return attacking_locations

    def generate_kings_moves(self, i, j, color, board):

        kings_move = self.possible_moves(i, j, board[i][j], board)

        if color == "black":
            new_color = "white"
        else:
            new_color = "black"

        pawn_moves = self.find_pawns_attacking_locations(new_color, board)

        other_moves = []

        for k in range(0, 8):
            for l in range(0, 8):
                if (type(board[k][l]) == ChessPiece):
                    if board[k][l].color == new_color:
                        if board[k][l].piece != "pawn":
                            other_moves.append(self.possible_moves(k, l, board[k][l], board))

        other_moves = [item for sublist in other_moves for item in sublist]
        all_moves = other_moves + pawn_moves
        all_moves = list(dict.fromkeys(all_moves))

        for move in all_moves:
            if move in kings_move:
                kings_move.remove(move)

        # remove king
        temp_king = board[i][j]
        board[i][j] = -1

        # need to eliminate possibilty for king to move into direction where attacking piece that is giving check can also move
        # this happens when attacking with rook, bishop or queen, since king is blocking that move possibility, 1 possible king move
        # under check was always forbiden. Figured this our only when I played the game.
        moves_from_checking_piece = self.possible_moves(self.piece_that_gives_check_location[0],
                                                        self.piece_that_gives_check_location[1],
                                                        board[self.piece_that_gives_check_location[0]][
                                                            self.piece_that_gives_check_location[1]], board)
        for move in moves_from_checking_piece:
            if move in kings_move:
                kings_move.remove(move)

        # put king back on the board
        board[i][j] = temp_king

        return kings_move

    def is_piece_that_gives_ckeck_protected(self, board):

        if not self.is_check:
            return False

        if self.current_color == "white":
            color = "black"
        else:
            color = "white"

        possible_moves = []
        temp_piece = board[self.piece_that_gives_check_location[0]][self.piece_that_gives_check_location[1]]
        board[self.piece_that_gives_check_location[0]][self.piece_that_gives_check_location[1]] = -1

        for k in range(0, 8):
            for l in range(0, 8):
                if (type(board[k][l]) == ChessPiece):
                    if board[k][l].color == color:
                        possible_moves.append(self.possible_moves(k,l,self.get_piece(k,l, board), board))


        possible_moves = [item for sublist in possible_moves for item in sublist]
        possible_moves = list(dict.fromkeys(possible_moves))

        self.move_piece(self.piece_that_gives_check_location[0],self.piece_that_gives_check_location[1],temp_piece, board)

        for move in possible_moves:
            if move[0] == self.piece_that_gives_check_location[0] and move[1] == self.piece_that_gives_check_location[1]:
                return True

        return False

    def find_moves_under_check(self, i, j, king_location):
        defending_moves = []
        blocking_moves = []
        king_moves = []
        remove_attacker_moves = []
        moves_under_check = []
        blocking_locations = self.find_locations_that_block_check(self.piece_that_gives_check_location, king_location, self.chessBoard)

        # find move that removes attacker of the king
        for move in self.moves:
            if move[0] == self.piece_that_gives_check_location[0] and move[1] == self.piece_that_gives_check_location[1]:
                remove_attacker_moves.append(move)

        # find moves that blocks check by moving defending piece into the blocking location
        for move in self.moves:
            for b_move in blocking_locations:
                if b_move[0] == move[0] and b_move[1] == move[1]:
                    blocking_moves.append(move)

        # find moves with moving king
        if (i, j) == king_location:

            defending_moves = self.generate_kings_moves(i, j, self.current_color, self.chessBoard)
        else:
            defending_moves = remove_attacker_moves + blocking_moves

        if len(defending_moves) == 0:
            moves_under_check = []
        else:
            moves_under_check = defending_moves
            #king cant take attacking piece, if attacking piece is protected
            if (self.is_piece_that_gives_ckeck_protected(self.chessBoard)):
                if self.piece_that_gives_check_location in defending_moves:
                    defending_moves.remove(self.piece_that_gives_check_location)

        if (self.is_piece_pinned(i, j, self.current_color, self.chessBoard)):
            moves_under_check = []

        return moves_under_check

    def promote_pawn(self,i,j, board):
        piece = self.get_piece(i,j, board)
        if type(piece) == ChessPiece:

            if piece.piece == "pawn":
                if (piece.color == self.current_color):

                    if self.current_color == "white" and i == 0:
                        board[i][j] = self.white_queen
                    elif self.current_color == "black" and i == 7:
                        board[i][j] = self.black_queen

    def is_checkmate(self, king_location):
        possible_moves = []
        for k in range(0, 8):
            for l in range(0, 8):
                if (type(self.chessBoard[k][l]) == ChessPiece):
                    if self.chessBoard[k][l].color == self.current_color:
                        possible_moves.append(self.find_moves_under_check(k, l, king_location))

        possible_moves = [item for sublist in possible_moves for item in sublist]

        if len(possible_moves) == 0:
            print("checkmate")
            return True
        else:

            return False

    def find_moves_under_pin(self, i, j, board):
        moves_under_pin = []
        current_piece = self.get_piece(i, j, board)
        for move in self.moves:
            # remove pinning piece, thats fine, player is allowed to do that
            if move[0] == self.piece_that_gives_pin_location[0] and move[1] == \
                    self.piece_that_gives_pin_location[1]:
                moves_under_pin.append((move[0], move[1]))
                continue

            # we remove moving piece from current position
            self.remove_piece(i, j, board)
            # we save taken opponent move by our piece, so that we can later restore its position
            temp_piece = self.get_piece(move[0], move[1], board)

            # we move our piece on that location
            self.move_piece(move[0], move[1], current_piece, board)
            moves_that_might_deliver_check = self.possible_moves(self.piece_that_gives_pin_location[0],
                                                                 self.piece_that_gives_pin_location[1],
                                                                 self.get_piece(
                                                                     self.piece_that_gives_pin_location[0],
                                                                     self.piece_that_gives_pin_location[1],board), board)
            # we remove our piece from temporary location
            self.remove_piece(move[0], move[1], board)
            # we move temporary taken piece into its original position
            self.move_piece(move[0], move[1], temp_piece, board)

            if self.current_color == "black":
                color = "white"
            else:
                color = "black"

            if (not self.check_for_check(moves_that_might_deliver_check, color)):
                moves_under_pin.append((move[0], move[1]))

            # we move our piece into original position
            self.move_piece(i, j, current_piece, board)
        return moves_under_pin

    # TODO
    def rook_can_see_king(self):
        return False

    # TODO
    def castling_squares_under_attack(self):
        return False

    # TODO
    def castling(self):
        if self.current_color == "white" and self.white_king_moved and not self.rook_can_see_king() and not self.castling_squares_under_attack():
            return "cannot castle white king"

        if self.current_color == "black" and self.black_king_moved and not self.rook_can_see_king() and not self.castling_squares_under_attack():
            return "cannot castle black king"

    # TODO
    def en_passant(self):
        pass

    def game(self, i, j, board):
        # check if you can select piece on coordinate i,j (I think)
        if i < 0 or i > 7 or j < 0 or j > 7:
            return "that move is out of bounds"
        if self.select_piece:
            #
            if (type(self.get_piece(i, j, board)) != ChessPiece):
                return "Invalid move"
            
            piece_color = self.check_color(i, j, board)
            #controls whose turn it is (can't move other players pieces)
            if (piece_color != self.current_color):
                return "Invalid move: Not your piece"
            
            self.piece = self.get_piece(i, j, board)
            self.coords = (i, j) #may break
            self.moves = self.possible_moves(i, j, self.piece, board)
            self.select_piece = False

            if self.piece.piece == "king":
                self.moves = self.generate_kings_moves(i, j, self.current_color, board)

            # check for pins, accordingly reduces move possibilities
            if (self.is_piece_pinned(i, j, self.current_color, board) and not self.is_check):
                self.moves = self.find_moves_under_pin(i, j, board)
                print("pin" + str(self.moves))
            king_location = (-1, -1)
            if self.current_color == "black":
                king_location = self.black_king_location
            else:
                king_location = self.white_king_location

            if (self.is_check):
                self.moves = self.find_moves_under_check(i, j, king_location)

        else:
            #block of code executes when you click on a non-movable piece or unselecting a movable piece after you've selected one
            player_move = (i, j)
            if player_move not in self.moves:
                self.moves = []
                self.select_piece = True
                return "Invalid move: You've unselected your piece or that piece isn't currently moveable"
            
            self.remove_piece(self.coords[0], self.coords[1], board)#may break
            self.move_piece(i, j, self.piece, board)
            self.is_check = False
            self.select_piece = True
            self.moves = []

            self.promote_pawn(i,j, board)

            # after player makes a move, we check if player deliverd a check to opponents king, we need for discovery checks
            self.check_all_pieces_for_check(self.current_color, board)

            if self.current_color == "white":
                self.current_color = "black"
                king_location = self.black_king_location
            else:
                self.current_color = "white"
                king_location = self.white_king_location

            if self.is_check:
                if self.is_checkmate(king_location):
                    k = self.find_king(self.current_color, self.chessBoard)
                    #print("k moves"+str(self.possible_moves(k[0], k[1], self.chessBoard[k[0]] [k[1]], self.chessBoard)))
                    # GAME FINISHED
                    self.moves = []
                    self.select_piece = False
                    if self.current_color == "black":
                        print("White won!")
                    else:
                        print("Black won!")
                    print("theirs")
                    self.outcomeDecided = True
            
            # if too few pieces left game ends in draw
            piecesLeft = self.count_pieces_on_board(board)
            if piecesLeft < 3:
                print("Game ends in draw, only " + str(piecesLeft) + 
                    " pieces left on board")
                self.outcomeDecided = True
                #return "Game ends in draw, too few pieces left on board"
    
    #count number of pieces left on board
    def count_pieces_on_board(self, board):
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if type(board[i][j]) == ChessPiece:
                    count += 1
        return count
                    
    # continually runs while game is in play
    def run_game(self):
        while not (self.gameExit or self.outcomeDecided):

            mx, my = pygame.mouse.get_pos()
            mj, mi = (int((mx - self.offset_x) / self.sqaure_size), int((my - self.offest_y) / self.sqaure_size))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                   print(self.game(mi, mj, self.chessBoard))

            if self.current_color == "black":

                botmove = self.bot(self.current_color, 1)
                
                print(self.game(botmove[1][0],botmove[1][1],self.chessBoard))
                self.select_piece = False
                print(self.game(botmove[0][0],botmove[0][1],self.chessBoard))
            
            # we uncomment the following code block when running the bot against itself
            # else:
            #     botmove = self.bot(self.current_color, 1)
                
            #     print(self.game(botmove[1][0],botmove[1][1],self.chessBoard))
            #     self.select_piece = False
            #     print(self.game(botmove[0][0],botmove[0][1],self.chessBoard))
                
                # uncomment for random moves
                # var = self.random_move(self.all_moves(self.current_color, self.chessBoard))
                # cor1 = var[0][1]
                # cor2 = var[1]
                # print(self.game(cor1[0],cor1[1],self.chessBoard))
                # self.select_piece = False
                # print(self.game(cor2[0],cor2[1],self.chessBoard))
                
                
            self.draw_chess_board(self.chessBoard)

            pygame.display.update()
        while not self.gameExit:
            self.draw_chess_board(self.chessBoard)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
    
    def find_king(self, color, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if type(board[i][j]) == ChessPiece:
                    if board[i][j].piece == "king" and board[i][j].color == color:
                        return (i,j)
                  
    # selects move for bot
    def bot(self,color,depth):
        movei = self.max_move(self.all_moves(color,self.chessBoard), self.chessBoard, color, depth)

        print("Chosen move: " + str(movei))
        if type(movei[0][0]) == ChessPiece:
            print(movei[0][0].piece)
        
        # [move ival, move jval, [selection ival, selection jval]]
        return [movei[1][0], movei[1][1]], [movei[0][1][0], movei[0][1][1]]
  
#first part creates a list of lists consisting of a piece and its coordinate [i,j]
#second creates a list of lists of a (list of piece and coordinates [i,j]) and a move (i,j) 
    def all_moves(self,color,board):
        pieces = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if type(board) == ChessBoard:
                    if self.check_if_square_empty(i, j, board) != True:
                        if (board[i][j]).color == color:
                            
                            
                                
                            pieces.append([board[i][j],[i,j]])
                else:
                    if type(board[i][j]) != int:
                        if (board[i][j]).color == color:
                            
                                
                            pieces.append([board[i][j],[i,j]])
                            
        
        all_moves=[]
        for piece in pieces:
            if not self.is_piece_pinned( piece[1][0], piece[1][1], color, board):
                for move in set(self.possible_moves(piece[1][0],piece[1][1],piece[0], board)):
                    if move[0] <= 7 and move[0] >= 0 and move[1] <= 7 and move[1] >= 0:
                        all_moves.append([piece,move])
            
            else:
                for move in set(self.find_moves_under_pin(piece[1][0],piece[1][1], board)):
                    if move[0] <= 7 and move[0] >= 0 and move[1] <= 7 and move[1] >= 0:
                        all_moves.append([piece,move])
        
        
        all_moves2 = []

        self.is_check = False
        random.shuffle(all_moves)
        return all_moves
                    
    def random_move(self,all_moves):
        return random.choice(all_moves)

    def max_kill(self, all_moves, board, color, depth):

        depth -= 1

        if depth <= 0:
            if type(board[all_moves[0][1][0]][all_moves[0][1][1]]) == ChessPiece:
                maxvalue = board[all_moves[0][1][0]][all_moves[0][1][1]].value
                enemyvalue = 0 
            else:
                maxvalue = 0
                enemyvalue = 0 
        else:
            if type(board[all_moves[0][1][0]][all_moves[0][1][1]]) == ChessPiece:
                enemyvalue = self.max_move(all_moves, board, color, depth)[2]
                maxvalue = board[all_moves[0][1][0]][all_moves[0][1][1]].value - enemyvalue
            else:
                enemyvalue = self.max_move(all_moves, board, color, depth)[2]
                maxvalue = 0 - enemyvalue
            
        maxmoves = []
        maxmoves.append(all_moves[0])
        for move in all_moves:
            if len(move) < 2:
                print("Error " +str(move))
            else:

                if type(board[move[1][0]][move[1][1]]) == ChessPiece:

                    if board[move[1][0]][move[1][1]].value - enemyvalue == maxvalue:
                        maxmoves.append(move)

                    elif board[move[1][0]][move[1][1]].value - enemyvalue > maxvalue:
                        maxmoves = []
                        maxmoves.append(move)
                        

                        maxvalue = board[move[1][0]][move[1][1]].value - enemyvalue
                        
                elif maxvalue == 0 - enemyvalue:
                    maxmoves.append(move)
        
        self.is_check = False               
        output = random.choice(maxmoves)
        output.append(maxvalue)
        return output
    
    def max_move(self, all_moves, board, color, depth):
        maxvalue = float('-inf')
        
        if len(all_moves[0]) > 2 and type(board[all_moves[0][1][0]][all_moves[0][1][1]]) == ChessPiece:
            maxvalue = board[all_moves[0][1][0]][all_moves[0][1][1]].value  - self.look_ahead_fun(all_moves[0],color,board, depth)[2]
        maxmoves = []
        maxmoves.append(all_moves[0])
        for move in all_moves:
            if len(move) < 2:
                print("Error" + move)
            else:
                lookAhead = self.look_ahead_fun(move,color,board, depth)[2]
                if type(board[move[1][0]][move[1][1]]) == ChessPiece:
                    if board[move[1][0]][move[1][1]].value - lookAhead == maxvalue:
                        maxmoves.append(move)
                    elif board[move[1][0]][move[1][1]].value - lookAhead > maxvalue:
                        maxmoves = []
                        maxmoves.append(move)
                        maxvalue = board[move[1][0]][move[1][1]].value - lookAhead

                else:
                
                    if 0 - lookAhead == maxvalue:
                        maxmoves.append(move)
                    elif 0 - lookAhead > maxvalue:

                        maxmoves = []
                        maxmoves.append(move)
                        maxvalue = 0 - lookAhead
             
        output = random.choice(maxmoves)
        output.append(maxvalue)
        return output

    def look_ahead_fun(self, move, color, board, depth):
        currcolor = color    
        copyOfChessBoard = self.generate_board_after_move(board, move)          
        if currcolor == "black":
            currcolor = "white"
        elif currcolor == "white":
            currcolor = "black"

        return self.max_kill(self.all_moves(currcolor, copyOfChessBoard),copyOfChessBoard, color, depth)

    def generate_board_after_move(self, board, move):
        copyOfChessBoard = [[i for i in range(0, 8)] for j in range(0, 8)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                copyOfChessBoard[i][j] = board[i][j]
        
        if type(move) != int:
            copyOfChessBoard[move[0][1][0]][move[0][1][1]] = 0
            copyOfChessBoard[move[1][0]][move[1][1]] = move[0][0]
        
        return copyOfChessBoard
          
    
chessBoard = ChessBoard(800, 600)
chessBoard.run_game()
