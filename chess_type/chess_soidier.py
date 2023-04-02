from chess import chess
from side import side

class soldier(chess):

    def soldier():
        pass

    def validateMovement(self, to_point, board):
        if self.point == to_point:  # 留原地
            return False

        chess_temp = board.find_chess(to_point)
        if chess_temp and chess_temp.side == self.side:  # 友軍位
            return False  # 如果 有這個棋子 and 棋子的顏色 == 我方旗子的顏色 => false
        
        # 走兩步
        soldier_count = (self.point[0] - to_point[0]), (to_point[1] - self.point[1])
                              

        if abs((soldier_count[0])) + abs((soldier_count[1])) !=1 :
            return False

        if self.side == side.red:
            if soldier_count[1] == -1 : # 不能退後 
                return False

        if self.side == side.black:
            if soldier_count[1] == 1 : # 不能退後 (黑)
                return False
        
        # 超出地圖:
        if to_point[0] <= -1 or to_point[0] > 8  :
            return False
        
        if to_point[1] <= -1 or to_point[0] > 9:
            return False

        # 過河可以左右跑  
        if self.point[1] == 3:
            if self.side == side.red:
                if to_point != (0, 4) and to_point != (2, 4) and to_point != (
                        4, 4) and to_point != (6, 4) and to_point != (
                            8, 4):  # 5個點(red)
                    return False
                
            if self.side == side.black:
                if to_point != (0, 5) and to_point != (2, 5) and to_point != (
                        4, 5) and to_point != (6, 5) and to_point != (
                            8, 5):  # 5個點(black)
                    return False
        elif self.point[1] == 4:
            if not to_point[1]  >= 5:
                return False
        return True

        
        
