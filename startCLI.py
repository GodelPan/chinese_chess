from chinese_chess import ChineseChess
import re
chess_game = ChineseChess()

while True:
    # try:
    #     from_point = tuple(input("請輸入from_chess:")) 
    #     if  len(from_point) != 2:
    #         print("請重新輸入正確的長度")
    #         continue
    #     from_point = (int(from_point[0]),int(from_point[1])) #最後移動
    # except ValueError:
    #     print("請重新輸入正確的數值")
    #     continue

    # try:
    #     to_point = tuple(input("請輸入to_chess:")) 
    #     if len(from_point) != 2:
    #         print("請稍後重新輸入正確的長度")
    #         continue
    #     to_point = (int(to_point[0]),int(to_point[1])) #最後移動
    # except ValueError:
    #     print("請重新輸入正確的數值")
    #     continue

    from_point = input("請輸入from_chess:") 
    if not re.match("^\d{2}$", from_point):
        print("請重新輸入正確的數值")
        continue
    from_point = (int(from_point[0]),int(from_point[1]))

    to_point = input("請輸入to_chess:") 
    if not re.match("^\d{2}$", to_point): #正則表達式
        print("請重新輸入正確的數值")
        continue
    to_point = (int(to_point[0]),int(to_point[1]))

    if not chess_game.movechess(from_point,to_point):
        print("請當前玩家重新輸入數值")
        continue

    # gameover
    if  not chess_game.check_gameover():
        print("遊戲結束")
        break

    if chess_game.current_player == chess_game.red_player:
        chess_game.current_player = chess_game.black_player
        print("輪到黑棋玩家")
    else:
        chess_game.current_player =chess_game.red_player
        print("輪到紅棋玩家")