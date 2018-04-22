

class GamePlay:

    board = None

    def __init__(self, board):
        self.board = board

    def find_tile(self, event):
        return self.board.tile_intersect(event.x, event.y)

    def got_event(self, event):
        tile = self.find_tile(event)
        if tile is not None:
            if tile.piece is not None:
                print(tile.piece.piece_id)
                return tile.piece
