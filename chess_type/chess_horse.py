from chess import chess


class horse(chess):

    def horse(self):
        pass
    
    def validateMovement(self, to_point, board):
        if self.point == to_point:  # 留原地
            return False

        chess_temp = board.find_chess(to_point)
        if chess_temp and chess_temp.side == self.side:  # 友軍位
            return False  # 如果 有這個棋子 and 棋子的顏色 == 我方旗子的顏色 => false

        # 卡馬腳
        if abs(to_point[0]) > abs(to_point[1]):
            horse_eye = (self.point[0] +1) , (self.point[1])
            if board.find_chess(horse_eye):
                return False
        elif abs(to_point[0]) < abs(to_point[1]):
            horse_eye = (self.point[0] ) , (self.point[1]+1)                                                         
            if board.find_chess(horse_eye):
                return False

        # 走兩步
        horse_count = (self.point[0] - to_point[0]), (self.point[1] -
                                                         to_point[1])
        if abs((horse_count[0])) ==0 or abs((horse_count[1])) ==0 :
            return False

        if abs((horse_count[0])) + abs((horse_count[1])) !=3 :
            return False
        return True