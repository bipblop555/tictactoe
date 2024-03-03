from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic

import os


class TictactoeView(QMainWindow):

	def __init__(self):
		super(TictactoeView, self).__init__()
		uic.loadUi(os.path.join(os.path.split(__file__)[0], "tictactoe2.ui"), self)

		self.dict_of_pixmaps = {f"player_{index_player}": QIcon(QPixmap(f"./player_{index_player}.png")) for index_player in range(1, 3)}


	def check_cell(self, index_line, index_column, turn):
		self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setIcon(self.dict_of_pixmaps[f"player_{turn}"])
		self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setEnabled(False)



	def game_finished(self, winner):
		for index_line in range(0, 5):
			for index_column in range(0, 5):
				self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setEnabled(False)

		if winner == 0 :
			self.game_status.setText(f"Draw")
		else:
			self.game_status.setText(f"The winner is the player {winner}")






































	# def update_grid_view(self, game_state):

	# 	if game_state["game_in_progress"]:
	# 		self.info_label.setText(f"C'est au tour du joueur {game_state['turn']}")

	# 	else:
	# 		for index_line in range(0, 3):
	# 			for index_column in range(0, 3):
	# 				self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setEnabled(False)
			
	# 		if game_state["there_is_winner"]:
	# 			self.info_label.setText(f"Le joueur {game_state['turn']} a gagné la partie")
	# 		else :
	# 			self.info_label.setText("Match nul !")



	# def reset_view(self):
	# 	for index_line in range(0, 3):
	# 		for index_column in range(0, 3):
	# 			self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setIcon(QIcon())
	# 			self.findChild(QPushButton, f'push_button_{index_line}_{index_column}').setEnabled(True)
	# 			self.info_label.setText(f"C'est au tour du joueur {1}")


