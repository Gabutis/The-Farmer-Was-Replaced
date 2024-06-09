def plant_dino():
    world_size = get_world_size()

    for i in range(world_size):
        for j in range(world_size):
            if num_items(Items.Egg) < 150:
                if num_items(Items.Cactus) < 18000:
                    farm_cacti(18000)
                trade(Items.Egg, 150)
            if get_entity_type() != Entities.Dinosaur:
                use_item(Items.Egg)
            move(North)
        move(East)


def check_neighbors_and_harvest(x, y, dino_type):
    directions = [North, East, South, West]
    same_type_count = 0

    for direction in directions:
        move_to(x, y)
        measure(direction)
        if measure(direction) == dino_type:
            same_type_count += 1

    if same_type_count >= 3:
        move_to(x, y)
        harvest()


def farm_dino(n):
    plant_dino()
    world_size = get_world_size()
    while num_items(Items.Bones) < n:
        for i in range(world_size):
            for j in range(world_size):
                move_to(i, j)
                if get_entity_type != Entities.Dinosaur:
                    if num_items(Items.Egg) < 2:
                        trade(Items.Egg, 2)
                    use_item(Items.Egg)
                dino_type = measure()
                if dino_type == 0 or dino_type == 1:
                    harvest()
                elif dino_type == 2 or dino_type == 3:
                    check_neighbors_and_harvest(i, j, dino_type)