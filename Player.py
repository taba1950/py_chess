from Piece import *


class Player:

    pieces_types = ["king", "queen", "knight", "castle", "rook", "pawn"]

    player_one_pieces_loc = {"king": ["E1"], "queen": ["D1"], "knight": ["B1", "G1"],
                             "castle": ["A1", "H1"],
                             "rook": ["C1", "F1"],
                             "pawn": ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"]}

    player_two_pieces_loc = {"king": ["D8"], "queen": ["E8"], "knight": ["B8", "G8"],
                             "castle": ["A8", "H8"],
                             "rook": ["C8", "F8"],
                             "pawn": ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"]}

    pieces = []
    player = None
    board = None
    color = None

    def __init__(self, player, color, board):
        self.player = player
        self.board = board
        self.color = color

    def generate_player_pieces(self):
        for piece_type in self.pieces_types:
            locations = self.player_one_pieces_loc.get(piece_type)
            for tile_id in locations:
                tile = self.board.tile_by_id(tile_id)
                piece_id = piece_type + "1"
                piece = Piece(piece_type, tile, self.color, piece_id, self.player)
                self.pieces.append(piece)
                tile.add_piece(piece)

    def draw(self):
        for piece in self.pieces:
            piece.draw_piece()

