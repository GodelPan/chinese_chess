from chess import chess
from side import side


class advisor(chess):

    def advisor(self):
        pass

    def validateMovement(self, to_point, board):
        if self.point == to_point:  # 留原地
            return False

        chess_temp = board.find_chess(to_point)
        if chess_temp and chess_temp.side == self.side:  # 友軍位
            return False  # 如果 有這個棋子 and 棋子的顏色 == 我方旗子的顏色 => false

        # 走兩步
        advisor_count = (self.point[0] - to_point[0]), (self.point[1] -
                                                        to_point[1])

        if abs((advisor_count[0])) !=1 or abs((advisor_count[1])) !=1 :
            return False

        # if (int(advisor_count[0])) < 0:
        #     if (int(advisor_count[0])) < -1:
        #         return False
        # elif (int(advisor_count[0])) > 0:
        #     if (int(advisor_count[0])) > 1:
        #         return False
        # else:
        #     pass

        # if (int(advisor_count[1])) < 0:
        #     if (int(advisor_count[1])) < -1:
        #         return False
        # elif (int(advisor_count[1])) > 0:
        #     if (int(advisor_count[1])) > 1:
        #         return False
        # else:
        #     pass

        if self.side == side.red:
            if to_point != (4, 1) and to_point != (3, 2) and to_point != (
                    5, 2) and to_point != (5, 0) and to_point != (
                        3, 0):  # 5個點(red)
                return False
        else:
            if to_point != (3, 7) and to_point != (5, 7) and to_point != (
                    4, 8) and to_point != (5, 9) and to_point != (
                        3, 9):  # 5個點(black)
                return False
        return True
