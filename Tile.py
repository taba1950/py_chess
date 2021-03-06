class Tile:

    def __init__(self, board, row, col, tile_size, color, tile_id):
        self.board = board
        self.row = row
        self.col = col
        self.tile_size = tile_size
        self.x = col*tile_size
        self.y = board.board_size - (row*tile_size)
        self.color = color
        self.tile_id = tile_id
        self.piece = None

    def draw_tile(self):
        canvas = self.board.canvas
        canvas.create_rectangle(self.x, self.y, self.x+self.tile_size, self.y-self.tile_size,
                                fill=self.color, outline="", activefill="red")
        canvas.create_text(self.x + 30, self.y - 10,
                           text=self.tile_id+" r:"+str(self.row)+" c:"+str(self.col))

    def add_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None
