
from Tile import *
from Piece import *


class Board:

    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]

    pieces_types = ["king", "queen", "knight", "castle", "rook", "pawn"]

    player_one_pieces_loc = {"king": ["E1"], "queen": ["D1"], "knight": ["B1", "G1"],
                             "castle": ["A1", "H1"],
                             "rook": ["C1", "F1"],
                             "pawn": ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"]}

    player_two_pieces_loc = {"king": ["D8"], "queen": ["E8"], "knight": ["B8", "G8"],
                             "castle": ["A8", "H8"],
                             "rook": ["C8", "F8"],
                             "pawn": ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"]}

    board_size = None
    tile_size = None
    canvas = None

    tiles = []
    player_one_pieces = []
    player_two_pieces = []

    def __init__(self, canvas, board_size):
        self.board_size = board_size
        self.tile_size = board_size/8
        self.canvas = canvas

        self.generate_tiles()
        self.draw_board()

        self.generate_player_one_pieces()
        self.draw_player_one_pieces()

        self.generate_player_two_pieces()
        self.draw_player_two_pieces()

    def generate_tiles(self):
        for x in range(8):
            for y in range(8):
                if(x+y) % 2 == 0:
                    color = "grey"
                else:
                    color = "white"

                tile_id = self.cols[y]+self.rows[x]

                self.tiles.append(Tile(self, x, y, self.tile_size, color, tile_id))

    def draw_board(self):
        for tile in self.tiles:
            tile.draw_tile()

    def tile_by_id(self, tile_id):
        for tile in self.tiles:
            if tile_id == tile.tile_id:
                return tile

    def generate_player_one_pieces(self):
        color = "green"
        player = 1
        for piece_type in self.pieces_types:
            locations = self.player_one_pieces_loc.get(piece_type)
            for tile_id in locations:
                tile = self.tile_by_id(tile_id)
                piece_id = piece_type+"1"
                piece = Piece(piece_type, tile, color, piece_id, player)
                self.player_one_pieces.append(piece)
                tile.add_piece(piece)

    def generate_player_two_pieces(self):
        color = "blue"
        player = 2
        for piece_type in self.pieces_types:
            locations = self.player_two_pieces_loc.get(piece_type)
            for tile_id in locations:
                tile = self.tile_by_id(tile_id)
                piece_id = piece_type + "2"
                piece = Piece(piece_type, tile, color, piece_id, 2)
                self.player_two_pieces.append(piece)
                tile.add_piece(piece)

    def draw_player_one_pieces(self):
        for piece in self.player_one_pieces:
            piece.draw_piece()

    def draw_player_two_pieces(self):
        for piece in self.player_two_pieces:
            piece.draw_piece()

    def tile_intersect(self, x, y):
        for tile in self.tiles:
            if (x > tile.x) & (x < (tile.x+tile.tile_size)) & (y < tile.y) & (y > (tile.y - tile.tile_size)):
                return tile

    def move_piece(self, piece, target):
        source = piece.tile
        piece.tile = target
        target.piece = piece
        source.piece = None

    def tile_by_row_col(self, row, col):
        for tile in self.tiles:
            if tile.row == row & tile.col == col:
                return tile
            else:
                return None

    def redraw(self):
        self.draw_board()
        self.draw_player_one_pieces()
        self.draw_player_two_pieces()
