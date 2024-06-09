def do_maze(target_gold):
    opp = {North: South, East: West, South: North, West: East}
    dx = {North: 0, East: 1, South: 0, West: -1}
    dy = {North: 1, East: 0, South: -1, West: 0}

    accumulated_gold = 0
    maze_size = get_world_size() * get_world_size()

    harvest()
    plant(Entities.Bush)
    while get_entity_type() == Entities.Bush:
        if num_items(Items.Pumpkin) < 3010:
            farm_pumpkin(3010)
        if num_items(Items.Fertilizer) < 301:
            trade(Items.Fertilizer, 301)
        use_item(Items.Fertilizer)

    x, y = get_pos_x(), get_pos_y()
    goalx, goaly = None, None

    while accumulated_gold + num_items(Items.Gold) < target_gold:
        while get_entity_type() == Entities.Treasure:
            if measure() == None:
                # We've hit the recycling limit.
                return accumulated_gold + num_items(Items.Gold)
            goalx, goaly = measure()
            # Recycle the maze
            while not use_item(Items.Fertilizer):
                pass

        stack = [([North, East, South, West], None)]
        visited = {(get_pos_x(), get_pos_y())}

        while get_entity_type() != Entities.Treasure:
            dirs, back = stack[-1]
            oldx, oldy = x, y
            dir = None
            while len(dirs) > 0:
                dir = dirs.pop()
                x = oldx + dx[dir]
                y = oldy + dy[dir]
                if (x, y) in visited or not move(dir):
                    dir = None
                    continue
                else:
                    break
            if dir == None:
                stack.pop()
                if back == None:
                    print("I give up!")
                    while True:
                        do_a_flip()
                move(back)
                x, y = oldx + dx[back], oldy + dy[back]
            else:
                visited.add((x, y))
                stack.append(
                    (get_ranked_dirs(x, y, goalx, goaly, opp[dir]), opp[dir]))

        accumulated_gold += maze_size
        if accumulated_gold + num_items(Items.Gold) < target_gold:
            while not use_item(Items.Fertilizer):
                pass

    harvest()
    return accumulated_gold + num_items(Items.Gold)


def get_ranked_dirs(pos_x, pos_y, goal_x, goal_y, exclude=None):
    if goal_x == None:
        all_dirs = [(1, North), (2, East), (3, South), (4, West)]
    else:
        all_dirs = [
            (goal_y - pos_y + 0.1, North),
            (goal_x - pos_x + 0.2, East),
            (pos_y - goal_y + 0.3, South),
            (pos_x - goal_x + 0.4, West)]

    ranked_dirs = []
    for i in range(len(all_dirs)):
        worst_dir = min(all_dirs)
        all_dirs.remove(worst_dir)
        if worst_dir[1] != exclude:
            ranked_dirs.append(worst_dir[1])

    return ranked_dirs