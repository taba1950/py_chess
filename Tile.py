class Tile:

    board = None
    row = None
    col = None
    x = None
    y = None
    tile_size = None
    color = None
    tile_id = None

    def __init__(self, board, row, col, tile_size, color, tile_id):
        self.board = board
        self.row = row
        self.col = col
        self.tile_size = tile_size
        self.x = col*tile_size
        self.y = board.board_size - (row*tile_size)
        self.color = color
        self.tile_id = tile_id

    def draw_tile(self):
        canvas = self.board.canvas
        canvas.create_rectangle(self.x, self.y, self.x+self.tile_size, self.y-self.tile_size,
                                fill=self.color, outline="", activefill="red")
        canvas.create_text(self.x + 10, self.y - 10, text=self.tile_id)
