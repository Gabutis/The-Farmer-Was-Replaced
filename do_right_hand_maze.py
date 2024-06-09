def do_right_hand_maze(target_gold):
	while num_items(Items.Gold) < target_gold:
        harvest()
        plant(Entities.Bush)
        while get_entity_type() == Entities.Bush:
            if num_items(Items.Fertilizer) < 2:
                trade(Items.Fertilizer, 2)
            use_item(Items.Fertilizer)

        heading = North
        while get_entity_type() != Entities.Treasure:
            right = right_from(heading)
            if move(right):
                heading = right
            elif not move(heading):
                heading = left_from(heading)
        harvest()

def right_from(dir):
    dirs = [North, East, South, West, North]
    return find_next(dirs, dir)

def left_from(dir):
    dirs = [North, West, South, East, North]
    return find_next(dirs, dir)

def find_next(list, elem):
    for i in range(len(list) - 1):
        if list[i] == elem:
            return list[i + 1]
    return None