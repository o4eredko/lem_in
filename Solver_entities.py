class Room:
	def __init__(self, name, x, y):
		self.name = name
		self.x = int(x)
		self.y = int(y)
		self.halls = []
		self.added_by = None
		self.route_link = None
		self.ants_in_room = 0
