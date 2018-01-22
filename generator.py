from graphics import *
from random import randint
from time import sleep

class Cell(object):
	
	def __init__(self, x, y, s):
		self.x = x
		self.y = y
		self.s = s
		self.visited = False
		self.current = False
		self.wall = {'up': True,
					 'down': True,
					 'left': True,
					 'right': True}
		
	def draw_rect(self, window):
		p1 = Point(self.x * self.s, self.y * self.s)
		p2 = Point(self.x * self.s + self.s, self.y * self.s + self.s)
		rect = Rectangle(p1, p2)
		rect.draw(window)
		
	def print_info(self):
		print "x: %r, y: %r, s: %r, visited: %r, current: %r, wall: %r" % (self.x, self.y, self.s, self.visited, self.current, self.wall)
	
class Engine(object):
	
	def __init__(self, cells, window, rows, cols):
		self.cells = cells
		self.window = window
		self.rows = rows
		self.cols = cols
		
	def draw_inner_square(self, cell, colour):
		p1 = Point(cell.x * cell.s + 1, cell.y * cell.s + 1)
		p2 = Point(cell.x * cell.s + cell.s - 1, cell.y * cell.s + cell.s - 1)
		fill = Rectangle(p1,p2)
		fill.setFill(colour)
		fill.setOutline(colour)
		fill.draw(self.window)
		
	def clear_window(self):
		p1 = Point(0, 0)
		p2 = Point(500, 500)
		blank = Rectangle(p1, p2)
		blank.setFill('white')
		blank.setOutline('white')
		blank.draw(self.window)
		
	def update(self):
	
		for row in self.cells:
			for cell in row:
			
				# define points that make up lines
				top_left = Point(cell.x * cell.s, cell.y * cell.s)
				top_right = Point(cell.x * cell.s + cell.s, cell.y * cell.s)
				bottom_left = Point(cell.x * cell.s, cell.y * cell.s + cell.s)
				bottom_right = Point(cell.x * cell.s + cell.s, cell.y * cell.s + cell.s)
				
				# define lines
				line_up = Line(top_left, top_right)
				line_down = Line(bottom_left, bottom_right)
				line_left = Line(top_left, bottom_left)
				line_right = Line(top_right, bottom_right)
				
				# define cell fill-in area
				
				
				# if the cell wall is not there, make it grey
				if cell.wall['up'] == False:
					line_up.setFill('grey')
				if cell.wall['down'] == False:
					line_down.setFill('grey')
				if cell.wall['left'] == False:
					line_left.setFill('grey')
				if cell.wall['right'] == False:
					line_right.setFill('grey')
					
				# draw cell walls
				line_up.draw(self.window)
				line_down.draw(self.window)
				line_left.draw(self.window)
				line_right.draw(self.window)
				
				# fill cell in pink if current
				if cell.current == True:
					self.draw_inner_square(cell, 'pink')
					
				# fill cell in grey if visited
				if cell.visited == True:
					self.draw_inner_square(cell, 'grey')
					
	def check_if_finished(self):
		total = 0
		for row in self.cells:
			for cell in row:
				if cell.visited == False:
					return False
		return True
		
	def game_over(self, message):
		print message
		while True:
			pass
			
	def move_up(self, current_cell, recent):
		current_cell.visited = True
		top_left = Point(current_cell.x * current_cell.s, current_cell.y * current_cell.s)
		top_right = Point(current_cell.x * current_cell.s + current_cell.s, current_cell.y * current_cell.s)
		line_up = Line(top_left, top_right)
		line_up.setFill('grey')
		line_up.draw(self.window)
		self.draw_inner_square(current_cell, 'grey')
		current_cell.wall['up'] = False
		recent.append(current_cell)
		current_cell = self.cells[current_cell.x][current_cell.y-1]
		current_cell.wall['down'] = False
		
		return current_cell, recent
		
	def move_down(self, current_cell, recent):
		current_cell.visited = True
		bottom_left = Point(current_cell.x * current_cell.s, current_cell.y * current_cell.s + current_cell.s)
		bottom_right = Point(current_cell.x * current_cell.s + current_cell.s, current_cell.y * current_cell.s + current_cell.s)
		line_down = Line(bottom_left, bottom_right)
		line_down.setFill('grey')
		line_down.draw(self.window)
		self.draw_inner_square(current_cell, 'grey')
		current_cell.wall['down'] = False
		recent.append(current_cell)
		current_cell = self.cells[current_cell.x][current_cell.y+1]
		current_cell.wall['up'] = False
		
		return current_cell, recent
		
	def move_left(self, current_cell, recent):
		current_cell.visited = True
					
		top_left = Point(current_cell.x * current_cell.s, current_cell.y * current_cell.s)
		bottom_left = Point(current_cell.x * current_cell.s, current_cell.y * current_cell.s + current_cell.s)
		line_left = Line(top_left, bottom_left)
		line_left.setFill('grey')
		line_left.draw(self.window)
					
		self.draw_inner_square(current_cell, 'grey')
		current_cell.wall['left'] = False
		recent.append(current_cell)
		current_cell = self.cells[current_cell.x-1][current_cell.y]
		current_cell.wall['right'] = False
		
		return current_cell, recent
		
	def move_right(self, current_cell, recent):
		current_cell.visited = True
					
		top_right = Point(current_cell.x * current_cell.s + current_cell.s, current_cell.y * current_cell.s)
		bottom_right = Point(current_cell.x * current_cell.s + current_cell.s, current_cell.y * current_cell.s + current_cell.s)
		line_right = Line(top_right, bottom_right)
		line_right.setFill('grey')
		line_right.draw(self.window)
					
		self.draw_inner_square(current_cell, 'grey')
		current_cell.wall['right'] = False
		recent.append(current_cell)
		current_cell = self.cells[current_cell.x+1][current_cell.y]
		current_cell.wall['left'] = False
		
		return current_cell, recent
				
	def run(self, current_cell, recent):
	
		sleep(7)
	
		while True:
			#print "X: %r, Y: %r" % (current_cell.x, current_cell.y)
			if self.check_if_finished():
				self.game_over('Maze has been generated')
		
			current_cell.current = True
			self.draw_inner_square(current_cell, 'pink')
			"""
			if next_move == 0 and current_cell.y > 0:
				if self.cells[current_cell.x][current_cell.y-1].visited == False:
					current_cell, recent = self.move_up(current_cell, recent)
			elif next_move == 1 and current_cell.y < self.rows-1:
				if self.cells[current_cell.x][current_cell.y+1].visited == False:
					current_cell, recent = self.move_down(current_cell, recent)
			elif next_move == 2 and current_cell.x > 0:
				if self.cells[current_cell.x-1][current_cell.y].visited == False:
					current_cell, recent = self.move_left(current_cell, recent)
			elif next_move == 3 and current_cell.x < self.cols-1:
				if self.cells[current_cell.x+1][current_cell.y].visited == False:
					current_cell, recent = self.move_right(current_cell, recent)
				
			elif:
				#self.draw_inner_square(current_cell,'grey')
				#current_cell = recent[-1]
				#print recent
				#recent.pop(-1)
			else:
				pass
			"""
			
			can_move = [False, False, False, False]
			if current_cell.y > 0:
				if self.cells[current_cell.x][current_cell.y-1].visited == False:
					can_move[0] = True
			if current_cell.y < self.rows-1:
				if self.cells[current_cell.x][current_cell.y+1].visited == False:
					can_move[1] = True
			if current_cell.x > 0:
				if self.cells[current_cell.x-1][current_cell.y].visited == False:
					can_move[2] = True
			if current_cell.x < self.cols-1:
				if self.cells[current_cell.x+1][current_cell.y].visited == False:
					can_move[3] = True
					
			if True in can_move:
				while True:
					next_move = randint(0,3)
					if can_move[next_move] == True:
						if next_move == 0:
							current_cell, recent = self.move_up(current_cell, recent)
							break
						if next_move == 1:
							current_cell, recent = self.move_down(current_cell, recent)
							break
						if next_move == 2:
							current_cell, recent = self.move_left(current_cell, recent)
							break
						if next_move == 3:
							current_cell, recent = self.move_right(current_cell, recent)
							break
			else:
				self.draw_inner_square(current_cell,'grey')
				current_cell.visited = True
				current_cell = recent[-1]
				self.draw_inner_square(current_cell,'pink')
				recent.pop(-1)
				
	
def init_cells(side_length, rows, cols):
	cells = []
	for i in range(0,rows):
		row = []
		for j in range(0,cols):
			new_cell = Cell(i, j, side_length)
			row.append(new_cell)
		cells.append(row)
	return cells
	
def main():
	

	# setup canvas size variables
	canvas_width = 750
	canvas_height = 750
	
	# something that goes evenly in canvas_width and canvas_height works best
	rows = 50
	cols = 50
	side_length = canvas_width/cols
	
	# setup graphics window
	window = GraphWin("My Grid", canvas_height + 1, canvas_width + 1)
	window.setBackground('white')
	
	# setup cells
	cells = init_cells(side_length, rows, cols)
	game = Engine(cells, window, rows, cols)
	
	
	
	# run main loop
	# PUT THIS IS A LOOP
	current_cell = cells[0][0]
	recent = []
	game.update()
	game.run(current_cell, recent)
	
	window.getMouse()
	window.close()

main()