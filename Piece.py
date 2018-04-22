class Piece:

    piece_type = None
    tile = None

    def __init__(self, piece_type, tile):
        self.piece_type = piece_type
        self.tile = tile

    def draw_piece(self):
        canvas = self.tile.board.canvas
        x = self.tile.x
        y = self.tile.y
        size = self.tile.tile_size
        canvas.create_oval(x, y, x+size, y-size, fill="green", activefill="yellow")
        canvas.create_text(x+size/4, y-size/2, text=self.piece_type)
