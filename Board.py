
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

    board_size = None
    tile_size = None
    canvas = None

    tiles = []
    pieces = []

    def __init__(self, canvas, board_size):
        self.board_size = board_size
        self.tile_size = board_size/8
        self.canvas = canvas

        self.generate_tiles()
        self.draw_board()

        self.generate_player_one_pieces()
        self.draw_pieces()

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
        for piece_type in self.pieces_types:
            locations = self.player_one_pieces_loc.get(piece_type)
            for tile_id in locations:
                tile = self.tile_by_id(tile_id)
                self.pieces.append(Piece(piece_type, tile))

    def draw_pieces(self):
        for piece in self.pieces:
            piece.draw_piece()
