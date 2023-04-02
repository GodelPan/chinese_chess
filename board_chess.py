from chess_type.chess_general import general
from chess_type.chess_soidier import soldier
from chess_type.chess_elephant import elephant
from chess_type.chess_chariot import chariot
from chess_type.chess_horse import horse
from chess_type.chess_cannon import cannon
from chess_type.chess_advisor import advisor
import copy
from side import side


class board:

    def init_chess(self):
        self.chess_list = []
        # 將
        self.chess_list.append(general((4, 9), side.black))
        self.chess_list.append(general((4, 0), side.red))
        # 士
        self.chess_list.append(advisor((3, 9), side.black))
        self.chess_list.append(advisor((5, 9), side.black))
        self.chess_list.append(advisor((3, 0), side.red))
        self.chess_list.append(advisor((5, 0), side.red))
        # 象
        self.chess_list.append(elephant((2, 9), side.black))
        self.chess_list.append(elephant((6, 9), side.black))
        self.chess_list.append(elephant((2, 0), side.red))
        self.chess_list.append(elephant((6, 0), side.red))
        # 車
        self.chess_list.append(chariot((0, 9), side.black))
        self.chess_list.append(chariot((8, 9), side.black))
        self.chess_list.append(chariot((0, 0), side.red))
        self.chess_list.append(chariot((8, 0), side.red))
        # 馬
        self.chess_list.append(horse((1, 9), side.black))
        self.chess_list.append(horse((7, 9), side.black))
        self.chess_list.append(horse((1, 0), side.red))
        self.chess_list.append(horse((7, 0), side.red))
        # 炮
        self.chess_list.append(cannon((1, 7), side.black))
        self.chess_list.append(cannon((7, 7), side.black))
        self.chess_list.append(cannon((1, 2), side.red))
        self.chess_list.append(cannon((7, 2), side.red))
        # 兵
        self.chess_list.append(soldier((0, 6), side.black))
        self.chess_list.append(soldier((2, 6), side.black))
        self.chess_list.append(soldier((4, 6), side.black))
        self.chess_list.append(soldier((6, 6), side.black))
        self.chess_list.append(soldier((8, 6), side.black))
        self.chess_list.append(soldier((0, 3), side.red))
        self.chess_list.append(soldier((2, 3), side.red))
        self.chess_list.append(soldier((4, 3), side.red))
        self.chess_list.append(soldier((6, 3), side.red))
        self.chess_list.append(soldier((8, 3), side.red))

    def move_chess(self, from_point, to_point):
        if not self.find_chess(from_point):
            return False
        if self.point_chess_count(from_point) > 1: 
            return False
        if self.point_chess_count(to_point) > 1:
            return False

        chess_to_move = self.find_chess(from_point)  # 找到A
        if not chess_to_move.validateMovement(to_point, self):  # early return
            return False

        chess_list_temp = copy.deepcopy(self.chess_list)  # 複製self.chess_list的值,但存在不同的記憶體位址

        chess_to_delete = self.find_chess(to_point)  # 找到要去點的棋子了!
        if chess_to_delete:
            self.chess_list = [
                i for i in self.chess_list if to_point != i.point
            ]
        chess_to_move.point = to_point # 最後才4移動棋子

        #王手規則 (用validateMovement看可以不可以吃到將 如果吃的到會回傳True ,則可知道被將軍)
        
        # 王v王(一條線直線上(同x,不同y),只有兩顆棋子時(帥、王將),則return False)
        chess_count=0
        for i in self.chess_list:  # 找將
            if type(i) is general and i.side == side.black:         # python is 忘了去查
                general_black = i
          
        for i in self.chess_list:  # 找帥
            if type(i) is general and i.side == side.red:
                general_red = i

        if general_black.point[0] == general_red.point[0]: #王跟王中間有幾棋子
            for i in self.chess_list:
                if general_red.point[1] < i.point[1] and i.point[1] < general_black.point[1] and general_red.point[0] == i.point[0] :
                    chess_count+=1   
            if chess_count == 0: #王對王了
                self.chess_list = chess_list_temp
                return False

        # 自殺走法(我方下完後,如果敵方棋子的範圍可以走到帥的位子,回傳F)
        if chess_to_move.side == side.red: # 紅被將 (chess to move = red)
            find_red_general= self.find_chess(general_red.point)
            for i in self.chess_list: 
                black_chess = i
                if black_chess.side == side.black and black_chess.validateMovement(find_red_general.point, self):
                    self.chess_list = chess_list_temp
                    return False
    
        # 1 for迴圈 讓所有的黑棋的位置call vaildmovement  
        if chess_to_move.side == side.black: # 黑被將 (chess to move = black)
            find_black_general = self.find_chess(general_black.point)
            for i in self.chess_list: 
                red_chess = i
                if red_chess.side == side.red and red_chess.validateMovement(find_black_general.point, self):
                    self.chess_list = chess_list_temp
                    return False

        return True

    def check_gameover(self,current_player_side):

        chess_list_temp = copy.deepcopy(self.chess_list)
        
        for i in self.chess_list:  # 找將
            if type(i) is general and i.side == side.black:         
                general_black = i
          
        for i in self.chess_list:  # 找帥
            if type(i) is general and i.side == side.red:
                general_red = i
        
                
        # 下一手不看可不可以不被將
        find_black_general = self.find_chess(general_black.point)
        find_red_general= self.find_chess(general_red.point)
           
        # chess_point= [(i, j) for i in range(9) for j in range(10)]
              
        for i in chess_list_temp:
            chess = i
            for i in range(9):
                for j in range(10):
                    chess_point = (i,j)

                    if chess.side == side.black and chess.validateMovement(chess_point, self): 
                        for red_chess in chess_list_temp: #少王對王
                            if red_chess.side == side.red and red_chess.validateMovement(find_black_general.point, self):#黑被將
                                self.chess_list = chess_list_temp
                                return False
                            
                    elif chess.side == side.red and chess.validateMovement(chess_point, self):
                        for black_chess in chess_list_temp: #少王對王
                            if black_chess.side == side.black and black_chess.validateMovement(find_red_general.point, self):#紅被將
                                self.chess_list = chess_list_temp
                                return False                                    
        return True


    #   if chess_move.validateMovement() == True:
    #        chess_move.point = to_point
    #   else:
    #        return False

    def find_chess(self, point):
        for i in self.chess_list:
            if i.point == point:
                return i
        return None

    def point_chess_count(self, point):
        count = 0
        for i in self.chess_list:
            if i.point == point:
                count = count + 1
        return count
