def move_to(target_x=None, target_y=None):
    if target_x == None and target_y == None:
        # If no coordinates provided, move North once.
        if get_pos_y() >= get_world_size() - 1:
            # If at the top of the map, move North and then East.
            move(North)
            move(East)
        else:
            move(North)
    else:
        while get_pos_x() != target_x or get_pos_y() != target_y:
            if get_pos_x() < target_x:
                move(East)
            elif get_pos_x() > target_x:
                move(West)

            if get_pos_y() < target_y:
                move(North)
            elif get_pos_y() > target_y:
                move(South)

def water():
	if num_items(Items.Water_Tank) < 2:
		trade(Items.Empty_Tank, 2)
	if get_water() < 0.75 and get_entity_type() != None:
		use_item(Items.Water_Tank)