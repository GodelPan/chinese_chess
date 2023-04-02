from chess import chess
from side import side


class elephant(chess):

    def elephant(self):
        pass

    def validateMovement(self, to_point, board):
        if self.point == to_point:  # 留原地
            return False

        chess_temp = board.find_chess(to_point)
        if chess_temp and chess_temp.side == self.side:  # 友軍位
            return False  # 如果 有這個棋子 and 棋子的顏色 == 我方旗子的顏色 => false

        # 卡象腳
        elephant_eye = (self.point[0] + to_point[0]) // 2, (self.point[1] +
                                                            to_point[1]) // 2
        if board.find_chess(elephant_eye):
            return False

        # 走兩步
        elephant_count = (self.point[0] - to_point[0]), (self.point[1] -
                                                         to_point[1])

        if abs((elephant_count[0])) !=2 or abs((elephant_count[1])) !=2 :
            return False

        # if (int(elephant_count[0])) < 0:
            # if (int(elephant_count[0])) < -2:
                # return False
        # elif (int(elephant_count[0])) > 0:
            # if (int(elephant_count[0])) > 2:
                # return False
        # else:
        #     pass

        # if (int(elephant_count[1])) < 0:
            # if (int(elephant_count[1])) < -2:
                # return False
        # elif (int(elephant_count[1])) > 0:
            # if (int(elephant_count[1])) > 2:
                # return False
        # else:
            # pass

        # 過河
        if self.side == side.red:
            if to_point != (0, 2) and to_point != (2, 0) and to_point != (
                    2, 4) and to_point != (4, 2) and to_point != (
                        6, 0) and to_point != (6, 4) and to_point != (
                            8, 2):  # 7個點(red)
                return False
        else:
            if to_point != (0, 7) and to_point != (2, 5) and to_point != (
                    2, 9) and to_point != (4, 7) and to_point != (
                        6, 5) and to_point != (6, 9) and to_point != (
                            8, 4):  # 7個點(black)
                return False
        return True
