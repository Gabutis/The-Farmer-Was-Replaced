def make_grass():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Turf:
		till()

def make_bush():
	if can_harvest():
		harvest()
	else:
		if num_items(Items.Fertilizer) < 2:
			trade(Items.Fertilizer, 2)
		use_item(Items.Fertilizer)
	if get_ground_type() != Grounds.Turf:
		till()
	plant(Entities.Bush)
	water()

def make_tree():
	if can_harvest():
		harvest()
	else:
		if num_items(Items.Fertilizer) < 2:
			trade(Items.Fertilizer, 2)
		use_item(Items.Fertilizer)
	plant(Entities.Tree)
	water()

def make_carrot():
	if can_harvest():
		harvest()
	else:
		if num_items(Items.Fertilizer) < 2:
			trade(Items.Fertilizer, 2)
		use_item(Items.Fertilizer)
	if num_items(Items.Carrot_Seed) < 2:
		trade(Items.Carrot_Seed, 2)
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrots)
	water()

def make_wood():
	if can_harvest():
		harvest()
	if (get_pos_x() + get_pos_y()) % 2 == 0:
		plant(Entities.Tree)
		judu()
	else:
		if get_ground_type() != Grounds.Turf:
			till()
		plant(Entities.Bush)