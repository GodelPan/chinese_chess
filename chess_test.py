import unittest
from board_chess import board


class AdvisorTestCase(unittest.TestCase): # 士的測試

    def setUp(self):  # 前置作業
        self.board_chess = board()
        self.board_chess.init_chess()

    def test_advisor_01(self):  # 不要重複下到友軍位子
        expected = False
        self.board_chess.move_chess((5, 0), (4, 1))
        result = self.board_chess.move_chess((3, 0), (4, 1))
        self.assertEqual(expected, result)

    def test_advisor_02(self):  # 不要留在原點
        expected = False
        result = self.board_chess.move_chess((5, 0), (5, 0))
        self.assertEqual(expected, result)

    def test_advisor_03(self):  # 走斜的
        expected = True
        result = self.board_chess.move_chess((3, 0), (4, 1))
        self.assertEqual(expected, result)

    def test_advisor_04(self):  # 走直的
        expected = False
        result = self.board_chess.move_chess((3, 0), (3, 1))
        self.assertEqual(expected, result)

    def test_advisor_05(self):  # 走斜的(框外)
        expected = False
        result = self.board_chess.move_chess((3, 0), (2, 1))
        self.assertEqual(expected, result)

    def test_advisor_06(self):  # 走斜的 (黑)
        expected = True
        result = self.board_chess.move_chess((3, 9), (4, 8))
        self.assertEqual(expected, result)

    def test_advisor_07(self):  # 吃子
        expected = True
        result = self.board_chess.move_chess((7, 2), (5, 2))  # R炮
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((5, 9), (4, 8))  # B士
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((5, 2), (5, 7))  # R炮
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((4, 8), (5, 7))  # B士
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((5, 7), (4, 8))  # B士
        self.assertEqual(expected, result)

    def test_advisor_08(self):  # 走兩步
        expected = False
        result = self.board_chess.move_chess((3, 0), (3, 2))
        self.assertEqual(expected, result)


class ElephantTestCase(unittest.TestCase): # 象的測試

    def setUp(self):  # 前置作業
        self.board_chess = board()
        self.board_chess.init_chess()

    def test_elephant_01(self):  # 不要重複下到友軍位子
        expected = False
        self.board_chess.move_chess((6, 0), (4, 2))
        result = self.board_chess.move_chess((2, 0), (4, 2))
        self.assertEqual(expected, result)

    def test_elephant_02(self):  # 不要留在原點
        expected = False
        result = self.board_chess.move_chess((6, 0), (6, 0))
        self.assertEqual(expected, result)

    def test_elephant_03(self):  # 走斜的
        expected = True
        result = self.board_chess.move_chess((6, 0), (4, 2))
        self.assertEqual(expected, result)

    def test_elephanr_04(self):  # 走斜的 (黑)
        expected = True
        result = self.board_chess.move_chess((6, 9), (4, 7))
        self.assertEqual(expected, result)

    def test_elephant_05(self):  # 走斜的(過河X)
        expected = False
        self.board_chess.move_chess((6, 0), (4, 2))
        self.board_chess.move_chess((4, 2), (6, 4))
        result = self.board_chess.move_chess((6, 4), (4, 6))
        self.assertEqual(expected, result)

    def test_elephanr_06(self):  # 卡象腳
        expected = False
        self.board_chess.move_chess((7, 2), (5, 2))  # R炮
        self.board_chess.move_chess((6, 9), (4, 7))  # B象
        self.board_chess.move_chess((5, 2), (5, 8))  # R炮
        result = self.board_chess.move_chess((4, 7), (6, 9))  # B象
        self.assertEqual(expected, result)

    def test_elephant_07(self):  # 吃子
        expected = True
        result = self.board_chess.move_chess((7, 2), (5, 2))  # R炮
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((6, 9), (4, 7))  # B象
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((5, 2), (5, 7))  # R炮
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((4, 7), (6, 9))  # B象
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((5, 7), (4, 7))  # R炮
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((6, 9), (4, 7))  # B象
        self.assertEqual(expected, result)

    def test_elephant_08(self):  # 走兩步
        expected = False
        result = self.board_chess.move_chess((2, 0), (2, 4))
        self.assertEqual(expected, result)


class GeneralTestCase(unittest.TestCase): # 帥的測試

    def setUp(self):  # 前置作業
        self.board_chess = board()
        self.board_chess.init_chess()

    def test_general_01(self):  # 不要重複下到友軍位子
        expected = False
        self.board_chess.move_chess((5, 0), (4, 1))
        result = self.board_chess.move_chess((4, 0), (4, 1))
        self.assertEqual(expected, result)

    def test_general_02(self):  # 不要留在原點
        expected = False
        result = self.board_chess.move_chess((4, 0), (4, 0))
        self.assertEqual(expected, result)

    def test_general_03(self):  # 走斜的(紅)
        expected = False
        result = self.board_chess.move_chess((4, 0), (5, 1))
        self.assertEqual(expected, result)

    def test_general_04(self):  # 走直的
        expected = True
        result = self.board_chess.move_chess((4, 0), (4, 1))
        self.assertEqual(expected, result)

    def test_general_05(self):  # 走到框外(紅)
        expected = False
        self.board_chess.move_chess((4, 0), (4, 1))
        self.board_chess.move_chess((4, 1), (3, 1))
        result = self.board_chess.move_chess((3, 1), (2, 1))
        self.assertEqual(expected, result)

    def test_general_06(self):  # 走斜的 (黑)
        expected = False
        result = self.board_chess.move_chess((4, 9), (3, 8))
        self.assertEqual(expected, result)

    def test_general_07(self):  # 走到框外(黑)
        expected = False
        self.board_chess.move_chess((4, 9), (4, 8))
        self.board_chess.move_chess((4, 8), (3, 8))
        result = self.board_chess.move_chess((3, 8), (2, 8))
        self.assertEqual(expected, result)

    def test_general_08(self):  # 走兩步
        expected = False
        result = self.board_chess.move_chess((4, 0), (4, 2))
        self.assertEqual(expected, result)

    # 這邊只測試將軍移動，將對將測試而外拉出(專門處理將軍)

class HorseTestCase(unittest.TestCase): # 馬的測試

    def setUp(self):  # 前置作業
        self.board_chess = board()
        self.board_chess.init_chess()

    def test_horse_01(self):  # 不要重複下到友軍位子
        expected = False
        self.board_chess.move_chess((1, 0), (2, 2))
        result = self.board_chess.move_chess((2, 2), (3, 0))
        self.assertEqual(expected, result)

    def test_horse_02(self):  # 不要留在原點
        expected = False
        result = self.board_chess.move_chess((1, 0), (1, 0))
        self.assertEqual(expected, result)

    def test_horse_03(self):  # 走斜的(紅)
        expected = True
        result = self.board_chess.move_chess((1, 0), (0, 2))
        self.assertEqual(expected, result)

    def test_horse_04(self):  # 走直的
        expected = False
        result = self.board_chess.move_chess((1, 0), (1, 1))
        self.assertEqual(expected, result)

    def test_horse_05(self):  # 走斜的 (黑)
        expected = True
        result = self.board_chess.move_chess((1, 9), (2, 7))
        self.assertEqual(expected, result)

    def test_horse_06(self):  # 走兩步
        expected = False
        self.board_chess.move_chess((2, 3), (2, 4))
        result = self.board_chess.move_chess((1, 0), (3, 4))
        self.assertEqual(expected, result)
    
    def test_horse_07(self):  # 卡馬腳
        expected = False
        self.board_chess.move_chess((1, 0), (2, 2))  # R馬 ,卡(2,3)的兵
        result = self.board_chess.move_chess((2, 2), (3, 4))  # R馬
        self.assertEqual(expected, result)

    def test_horse_08(self):  # 走直的(紅)
        expected = False
        result = self.board_chess.move_chess((7, 0), (7, 3))
        self.assertEqual(expected, result)
    
    def test_horse_09(self):  # 跑出地圖
        expected = False
        self.board_chess.move_chess((2, 0), (0, 2))
        result = self.board_chess.move_chess((0, 2), (-2, 3))
        self.assertEqual(expected, result)

class  SoldierTestCase(unittest.TestCase): # 兵的測試

    def setUp(self):  # 前置作業
        self.board_chess = board()
        self.board_chess.init_chess()

    def test_soldier_01(self):  # 不要重複下到友軍位子
        expected = False
        self.board_chess.move_chess((1, 0), (2, 2))
        result = self.board_chess.move_chess((2, 2), (3, 0))
        self.assertEqual(expected, result)

    def test_soldier_02(self):  # 不要留在原點
        expected = False
        result = self.board_chess.move_chess((0, 3), (0, 3))
        self.assertEqual(expected, result)

    def test_soldier_03(self):  # 走斜的(紅)
        expected = False
        result = self.board_chess.move_chess((0, 3), (1, 4))
        self.assertEqual(expected, result)

    def test_soldier_04(self):  # 走直的
        expected = True
        result = self.board_chess.move_chess((0, 3), (0, 4))
        self.assertEqual(expected, result)

    def test_soldier_05(self):  # 走兩步
        expected = False
        result = self.board_chess.move_chess((0, 3), (0, 5))
        self.assertEqual(expected, result)
    
    def test_soldier_06(self):  # 不能後退
        expected = False
        result = self.board_chess.move_chess((0, 3), (0, 2))  
        self.assertEqual(expected, result)

    def test_soldier_07(self):  # 過河可以左右走
        expected = True
        self.board_chess.move_chess((0, 3), (0, 4))
        self.board_chess.move_chess((0, 4), (0, 5))
        result = self.board_chess.move_chess((0, 5), (1, 5))
        self.assertEqual(expected, result)
    
    def test_soldier_08(self):  # 跑出地圖
        expected = False
        self.board_chess.move_chess((0, 3), (0, 4))
        self.board_chess.move_chess((0, 4), (0, 5))
        result = self.board_chess.move_chess((0, 5), (-1, 5))
        self.assertEqual(expected, result)

    def test_soldier_09(self):  # 不能後退(黑)
        expected = False
        result = self.board_chess.move_chess((0, 6), (0, 7))  
        self.assertEqual(expected, result)

class  ChariotTestCase(unittest.TestCase): # 車的測試

    def setUp(self):  # 前置作業
        self.board_chess = board()
        self.board_chess.init_chess()

    def test_chariot_01(self):  # 不要重複下到友軍位子
        expected = False
        result = self.board_chess.move_chess((8, 0), (8, 3))
        self.assertEqual(expected, result)

    def test_chariot_02(self):  # 不要留在原點
        expected = False
        result = self.board_chess.move_chess((8, 0), (8, 0))
        self.assertEqual(expected, result)

    def test_chariot_03(self):  # 走斜的(紅)
        expected = False
        result = self.board_chess.move_chess((8, 0), (7, 1))
        self.assertEqual(expected, result)

    def test_chariot_04(self):  # 走直的
        expected = True
        result = self.board_chess.move_chess((8, 0), (8, 2))
        self.assertEqual(expected, result)
    
    def test_chariot_05(self):  # 跑出地圖
        expected = False
        result = self.board_chess.move_chess((8, 0), (9, 0))
        self.assertEqual(expected, result)

    def test_chariot_06(self):  # 走橫的
        expected = True
        self.board_chess.move_chess((0, 9), (0, 8))
        result = self.board_chess.move_chess((0, 8), (6, 8))
        self.assertEqual(expected, result)

    def test_chariot_07(self): # 中間卡棋子
        expected = False
        result = self.board_chess.move_chess((8, 0), (8, 6))
        self.assertEqual(expected, result)

    def test_chariot_08(self): # 吃子
        expected = True
        self.board_chess.move_chess((8, 0), (8, 1))
        self.board_chess.move_chess((8, 1), (5, 1))
        result = self.board_chess.move_chess((5, 1), (5, 9))
        self.assertEqual(expected, result)

    def test_chariot_10(self): # 中間卡棋子(2)
        expected = False
        self.board_chess.move_chess((8, 0), (8, 1)) # R車
        self.board_chess.move_chess((8, 1), (5, 1)) # R車
        self.board_chess.move_chess((5, 9), (4, 8)) # B士
        self.board_chess.move_chess((4, 8), (5, 7)) # B士
        result = self.board_chess.move_chess((5, 1), (5, 8)) # R車
        self.assertEqual(expected, result)

class  CannonTestCase(unittest.TestCase): # 炮的測試

    def setUp(self):  # 前置作業
        self.board_chess = board()
        self.board_chess.init_chess()

    def test_cannon_01(self):  # 不要重複下到友軍位子
        expected = False
        result = self.board_chess.move_chess((7, 2), (7, 0))
        self.assertEqual(expected, result)

    def test_cannon_02(self):  # 不要留在原點
        expected = False
        result = self.board_chess.move_chess((7, 2), (7, 2))
        self.assertEqual(expected, result)

    def test_cannon_03(self):  # 走斜的(紅)
        expected = False
        result = self.board_chess.move_chess((7, 2), (6, 1))
        self.assertEqual(expected, result)

    def test_cannon_04(self):  # 走直的
        expected = True
        result = self.board_chess.move_chess((7, 2), (7, 5))
        self.assertEqual(expected, result)
    
    def test_cannon_05(self):  # 跑出地圖
        expected = False
        result = self.board_chess.move_chess((7, 2), (9, 2))
        self.assertEqual(expected, result)

    def test_cannon_06(self):  # 走橫的
        expected = True
        result = self.board_chess.move_chess((7, 2), (4, 2))
        self.assertEqual(expected, result)

    def test_cannon_07(self): # 中間卡棋子
        expected = True
        result = self.board_chess.move_chess((7, 2), (7, 9))
        self.assertEqual(expected, result)

    def test_cannon_08(self): # 中間卡棋子(2)
        expected = False
        self.board_chess.move_chess((7, 2), (2, 2))
        result = self.board_chess.move_chess((2, 2), (2, 9))
        self.assertEqual(expected, result)

class  ChackKingTestCase(unittest.TestCase): # 炮的測試

    def setUp(self):  # 前置作業
        self.board_chess = board()
        self.board_chess.init_chess()

    def test_ChackKing_01(self):  # 王手(王v王) 紅x
        expected = False
        result = self.board_chess.move_chess((4, 9), (4, 8))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 8), (3, 8))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 1), (3, 1))
        self.assertEqual(expected, result)

    def test_ChackKing_02(self):  # 王手(王以外)(紅被將)
        expected = False
        result = self.board_chess.move_chess((5, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((7, 7), (7, 5))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((7, 5), (4, 5))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 1), (5, 0))
        self.assertEqual(expected, result)

    def test_ChackKing_03(self):  # 王手(王v王) 黑x
        expected = False
        result = self.board_chess.move_chess((4, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 1), (3, 1))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 9), (4, 8))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 8), (3, 8))
        self.assertEqual(expected, result)

    def test_ChackKing_04(self):  # 王手(王以外)(黑被將)
        expected = False
        result = self.board_chess.move_chess((5, 9), (4, 8))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((7, 2), (7, 5))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((7, 5), (4, 5))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 8), (5, 9))
        self.assertEqual(expected, result)

    def test_ChackKing_05(self):  # 王手 如果move_chess return F 盤面不能異動
        expected = False
        result = self.board_chess.move_chess((4, 9), (4, 8))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 8), (3, 8))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 0), (4, 1))
        self.assertEqual(True, result)
        result = self.board_chess.move_chess((4, 1), (3, 1))
        self.assertEqual(expected, result)
        result = self.board_chess.move_chess((4, 1), (5, 1))
        self.assertEqual(True, result)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(AdvisorTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(ElephantTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(GeneralTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(HorseTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(SoldierTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(ChariotTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(CannonTestCase)))
    suite.addTest(
        (unittest.TestLoader().loadTestsFromTestCase(ChackKingTestCase)))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
