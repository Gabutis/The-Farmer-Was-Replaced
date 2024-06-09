def polyculture():
	while True:
		if get_companion()[0] == Entities.Grass:
			move_to(get_companion()[1],get_companion()[2])
			make_grass()
		elif get_companion()[0] == Entities.Bush:
			move_to(get_companion()[1],get_companion()[2])
			make_bush()
		elif get_companion()[0] == Entities.Tree:
			move_to(get_companion()[1],get_companion()[2])
			make_tree()
		elif get_companion()[0] == Entities.Carrots:
			move_to(get_companion()[1],get_companion()[2])
			make_carrot()