import numpy

class TictactoeGrid:
	def __init__(self):
		self.grid = numpy.zeros((5, 5))
		self.game_in_progress = True
		self.winner = 0


	def winning_check(self):
		for i in range(5):
			if numpy.all(self.grid[i,:] == self.grid[i,0]) and self.grid[i,0] != 0:
				return True

		for j in range(5):
			if numpy.all(self.grid[:,j] == self.grid[0,j]) and self.grid[0,j] != 0:
				return True

		if numpy.all(numpy.diag(self.grid) == self.grid[0,0]) and self.grid[0,0] != 0:
			return True

		if numpy.all(numpy.diag(numpy.fliplr(self.grid)) == self.grid[0,4]) and self.grid[0,4] != 0:
			return True

		return False


	def get_game_state(self):
		return numpy.any(self.grid == 0)



	def human_move(self, index_line, index_column):
		self.grid[index_line, index_column] = 1
		
		self.game_in_progress = self.get_game_state()
		self.there_is_winner = self.winning_check()

		if self.there_is_winner:
			self.game_in_progress = False
			self.winner = 1
		

	def robot_move(self):
		index_line, index_column = self.get_optimal_cell()
		self.grid[index_line, index_column] = 2
		
		self.game_in_progress = self.get_game_state()
		self.there_is_winner = self.winning_check()

		if self.there_is_winner:
			self.game_in_progress = False
			self.winner = 2
			
		return index_line, index_column


	def get_optimal_cell(self):

		best_score = -float('inf')
		best_index_line, best_index_column = None, None

		for index_line in range(0, 5):
			for index_column in range(0, 5):
				if self.grid[index_line, index_column] == 0:
					self.grid[index_line, index_column] = 2
					score = self.minmax(robot_turn=False)
					if score > best_score:
						best_score = score
						best_index_line = index_line
						best_index_column = index_column
					self.grid[index_line, index_column] = 0	

		return best_index_line, best_index_column


	def minmax(self, robot_turn, alpha=-float('inf'), beta=float('inf'), depth=0, max_depth=3):
		if depth == max_depth or self.winning_check() or not self.get_game_state():
			return self.evaluate_state(robot_turn, depth)

		if robot_turn:
			best_score = -float('inf')
			for index_line in range(5):
				for index_column in range(5):
					if self.grid[index_line, index_column] == 0:
						self.grid[index_line, index_column] = 2 
						score = self.minmax(False, alpha, beta, depth + 1, max_depth)
						self.grid[index_line, index_column] = 0
						best_score = max(best_score, score)
						alpha = max(alpha, best_score)
						if beta <= alpha:
							break
			return best_score
		else:
			best_score = float('inf')
			for index_line in range(5):
				for index_column in range(5):
					if self.grid[index_line, index_column] == 0:
						self.grid[index_line, index_column] = 1 
						score = self.minmax(True, alpha, beta, depth + 1, max_depth)
						self.grid[index_line, index_column] = 0
						best_score = min(best_score, score)
						beta = min(beta, best_score)
						if beta <= alpha:
							break
			return best_score

	def evaluate_state(self, robot_turn, depth):
		if self.winning_check():
			return -10 + depth if robot_turn else 10 - depth
		elif not self.get_game_state():
			return 0
		else:
			return 0
