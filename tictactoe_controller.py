import tictactoe_view, tictactoe_grid
from PyQt5.QtWidgets import QPushButton
from functools import partial


class TictactoeController:
	def __init__(self):
		self.tictactoe_grid_object = tictactoe_grid.TictactoeGrid()
		self.tictactoe_view_object = tictactoe_view.TictactoeView()
		self.tictactoe_view_object.show()
		self.connect_widgets()


	def connect_widgets(self):
		for index_line in range(0, 5):  
			for index_column in range(0, 5):  
				button = self.tictactoe_view_object.findChild(QPushButton, f'push_button_{index_line}_{index_column}')
				if button:
					button.clicked.connect(partial(self.update_game, index_line, index_column))


	def update_game(self, index_line, index_column):
		#Humain
		self.tictactoe_grid_object.human_move(index_line, index_column)
		self.tictactoe_view_object.check_cell(index_line, index_column, 1)
		
		if not self.tictactoe_grid_object.game_in_progress:
			self.tictactoe_view_object.game_finished(self.tictactoe_grid_object.winner)
			return None



		#Machine
		robot_index_line, robot_index_column = self.tictactoe_grid_object.robot_move()
		self.tictactoe_view_object.check_cell(robot_index_line, robot_index_column, 2)
		
		if not self.tictactoe_grid_object.game_in_progress:
			self.tictactoe_view_object.game_finished(self.tictactoe_grid_object.winner)
			return None

