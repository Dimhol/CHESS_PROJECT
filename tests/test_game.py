import unittest
from main import Game
from constants import *


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_board_setup(self):
        # Test initial setup of the board
        expected_white = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        expected_black = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        self.assertEqual(self.game.board[0], expected_black)
        self.assertEqual(self.game.board[1], ['pawn'] * 8)
        self.assertEqual(self.game.board[6], ['pawn'] * 8)
        self.assertEqual(self.game.board[7], expected_white)

    def test_move_piece(self):
        self.game.move_piece((6, 0), (5, 0))
        self.assertEqual(self.game.board[5][0], 'pawn')
        self.assertEqual(self.game.board[6][0], '')

    def test_invalid_move(self):
        with self.assertRaises(ValueError):
            self.game.move_piece((6, 0), (4, 0))

    def test_capture_piece(self):
        # Test capturing a piece
        self.game.move_piece((6, 0), (4, 0))
        self.game.move_piece((1, 1), (3, 1))
        self.game.move_piece((4, 0), (3, 1))
        self.assertEqual(self.game.board[3][1], 'pawn')
        self.assertEqual(self.game.board[4][0], '')

    def test_check(self):
        self.game.board[0][5] = ''
        self.game.board[4][1] = 'bishop'
        self.assertTrue(self.game.is_in_check('black'))

    def test_checkmate(self):

        self.game.board = [
            ['rook', 'knight', 'bishop', 'queen', 'king', '', 'knight', 'rook'],
            ['pawn'] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            ['pawn'] * 8,
            ['rook', 'knight', 'bishop', 'queen', '', 'bishop', 'knight', 'rook'],
        ]
        self.game.board[4][1] = 'queen'
        self.assertTrue(self.game.is_checkmate('black'))

    def test_stalemate(self):
        # Test stalemate condition
        self.game.board = [
            ['king', '', '', '', '', '', '', ''],
            [''] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            [''] * 8,
            ['king', '', '', '', '', '', '', ''],
        ]
        self.assertTrue(self.game.is_stalemate('black'))

    def test_castling(self):
        # Test castling move
        self.game.board[7][4] = 'king'
        self.game.board[7][0] = 'rook'
        self.game.board[7][7] = 'rook'
        self.game.turn = 'white'
        self.game.castling((7, 4), (7, 0))
        self.assertEqual(self.game.board[7][2], 'king')
        self.assertEqual(self.game.board[7][3], 'rook')

    def test_pawn_promotion(self):
        # Test pawn promotion
        self.game.board[1][0] = 'pawn'
        self.game.turn = 'white'
        self.game.pawn_promotion((0, 1), (0, 0), 'queen')
        self.assertEqual(self.game.board[0][0], 'queen')


if __name__ == '__main__':
    unittest.main()
