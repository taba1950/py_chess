class Piece:

    piece_type = None
    tile = None
    color = None

    player = None

    piece_id = None

    legal_moves = []

    def __init__(self, piece_type, tile, color, piece_id, player):
        self.piece_type = piece_type
        self.tile = tile
        self.color = color
        self.piece_id = piece_id
        self.player = player
        self.find_legal_moves()

    def draw_piece(self):
        canvas = self.tile.board.canvas
        x = self.tile.x
        y = self.tile.y
        size = self.tile.tile_size
        canvas.create_oval(x, y, x+size, y-size, fill=self.color, activefill="yellow")
        canvas.create_text(x+size/4, y-size/2, text=self.piece_type)

    def find_legal_moves(self):
        col = self.tile.col
        row = self.tile.row

        self.legal_moves = self.tile.board.tiles
