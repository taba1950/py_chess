

class GamePlay:

    board = None

    moving = False
    moving_piece = None

    player_one_color = "green"
    player_two_color = "blue"

    def __init__(self, board):
        self.board = board

    def find_tile(self, event):
        return self.board.tile_intersect(event.x, event.y)

    def got_event(self, event):
        tile = self.find_tile(event)
        if not self.moving:
            if tile is not None:
                if tile.piece is not None:
                    self.moving_piece = tile.piece
                    self.moving_piece.color = "red"
                    self.board.redraw()
                    self.moving = True

        if self.moving:
            if tile.piece is None:
                if tile in self.moving_piece.legal_moves:
                    self.board.move_piece(self.moving_piece, tile)
                    if self.moving_piece.player == 1:
                        color = self.player_one_color
                    else:
                        color = self.player_two_color
                    self.moving_piece.color = color
                    self.board.redraw()
                    self.moving = False
                else:
                    self.moving = False
