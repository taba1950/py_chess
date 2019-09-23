
from Tile import *
from Player import *


class Board:

    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def __init__(self, canvas, board_size):
        self.board_size = board_size
        self.tile_size = board_size/8
        self.canvas = canvas

        self.tiles = []

        self.generate_tiles()
        self.draw_board()

        self.player_one = None
        self.player_two = None

        self.player_one_pieces = []
        self.player_two_pieces = []

        self.create_player_one()

        self.create_player_two()

    def generate_tiles(self):
        for x in range(8):
            for y in range(8):
                if(x+y) % 2 == 0:
                    color = "grey"
                else:
                    color = "white"

                tile_id = self.cols[y]+self.rows[x]

                self.tiles.append(
                    Tile(self, x, y, self.tile_size, color, tile_id))

    def draw_board(self):
        for tile in self.tiles:
            tile.draw_tile()

    def tile_by_id(self, tile_id):
        for tile in self.tiles:
            if tile_id == tile.tile_id:
                return tile

    def create_player_one(self):
        color = "green"
        player = 1
        self.player_one = Player(player, color, self)
        self.draw_player_one_pieces()

    def create_player_two(self):
        color = "blue"
        player = 2
        self.player_two = Player(player, color, self)
        self.draw_player_two_pieces()

    def draw_player_one_pieces(self):
        self.player_one.draw()

    def draw_player_two_pieces(self):
        self.player_two.draw()

    def tile_intersect(self, x, y):
        for tile in self.tiles:
            if (x > tile.x) & (x < (tile.x+tile.tile_size)) & (y < tile.y) & (y > (tile.y - tile.tile_size)):
                return tile

    def move_piece(self, piece, target):
        source = piece.tile
        piece.tile = target
        target.piece = piece
        source.piece = None
        piece.moved = True

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
