from chess import chess
from side import side


class general(chess):

    def general(self):
        pass

    def validateMovement(self, to_point, board):

        if self.point == to_point:  # 留原地
            return False

        chess_temp = board.find_chess(to_point)
        if chess_temp and chess_temp.side == self.side:  # 友軍位
            return False  # 如果 有這個棋子 and 棋子的顏色 == 我方旗子的顏色 => false

        #兩步
        general_count = (self.point[0] - to_point[0]), (self.point[1] -
                                                       to_point[1])
                                                       
        if abs(general_count[0]) + abs(general_count[1]) !=1 :           
            return False

        #過河x
        if self.side == side.red:
            if to_point != (3, 0) and to_point != (3, 1) and to_point != (
                    3, 2) and to_point != (4, 0) and to_point != (
                        4, 1) and to_point != (4, 2) and to_point != (
                            5, 0) and to_point != (5, 1) and to_point != (
                                5, 2):  # 9個點(red)
                return False
        else:
            if to_point != (3, 9) and to_point != (3, 8) and to_point != (
                    3, 7) and to_point != (4, 9) and to_point != (
                        4, 8) and to_point != (4, 7) and to_point != (
                            5, 9) and to_point != (5, 8) and to_point != (
                                5, 7):  # 9個點(red)
                return False
        return True
