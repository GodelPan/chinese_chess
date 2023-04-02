from board_chess import board
from player import player
from side import side


class ChineseChess:

    def __init__(self):
        self.board_chess = board()
        self.board_chess.init_chess()
        self.red_player = player(side.red)
        self.black_player = player(side.black)
        self.current_player = self.red_player   #現在的player 要嘛紅或要嘛黑
    
    def movechess(self,from_point,to_point):

        chess_to_move = self.board_chess.find_chess(from_point)
        if not chess_to_move : #確認有沒有可以移動棋子
            return False
        if chess_to_move.side !=  self.current_player.side:
            return False
        if not self.board_chess.move_chess(from_point,to_point):
            return False
        return True

    def check_gameover(self):
        return self.board_chess.check_gameover(self.current_player.side)
        