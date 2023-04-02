from chess import chess
from side import side

class chariot(chess):

    def chariot(self):
        pass

    def validateMovement(self, to_point, board):
        if self.point == to_point:  # 留原地
            return False

        chess_temp = board.find_chess(to_point)
        if chess_temp and chess_temp.side == self.side:  # 友軍位
            return False  # 如果 有這個棋子 and 棋子的顏色 == 我方旗子的顏色 => false

        # 超出地圖:
        if to_point[0] <= -1 or to_point[0] > 8  :
            return False
        
        if to_point[1] <= -1 or to_point[0] > 9:
            return False
        
        # 中間卡旗子
        for i in range(self.point[1],to_point[1]):
            for j in board.chess_list:
                if j.point == self.point:
                    continue
                elif j.point == (self.point[0],i):
                    return False

        for i in range(self.point[0],to_point[0]):
            for j in board.chess_list:
                if j.point ==self.point or j==to_point:
                    continue
                elif j.point == (i,self.point[1]):
                    return False
        # 走斜的
        chariot_count = (self.point[0] - to_point[0]), (self.point[1] - to_point[1])
                              
        if abs((chariot_count[0]))  > abs((chariot_count[1])): # 橫
            if abs((chariot_count[1])) != 0:
                return False

        elif abs((chariot_count[0]))  < abs((chariot_count[1])): # 直
            if abs((chariot_count[0])) != 0:
                return False  
            
        else:
            return False

        return True
