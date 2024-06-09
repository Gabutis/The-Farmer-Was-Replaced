def plant_cacti():
    if num_items(Items.Cactus_Seed) < 150:
        if num_items(Items.Gold) < 6000:
            do_maze(6000)
        trade(Items.Cactus_Seed, 150)


for i in range(get_world_size()):
    for j in range(get_world_size()):
        if get_ground_type() != Grounds.Soil:
            till()
        if get_entity_type() != Entities.Cactus:
            harvest()
            plant(Entities.Cactus)
        move(North)
    move(East)


def sort_cacti():
    move_to(0, 0)


cactus_map = []

for i in range(get_world_size()):
    for j in range(get_world_size()):
        x, y = get_pos_x(), get_pos_y()
        value = measure()
        cactus_map.append((x, y, value))
        move(North)
    move(East)

sorted = False

while not sorted:
    sorted = True
    for j in range(get_world_size() - 1):
        for i in range(get_world_size()):
            index = i * get_world_size() + j
            if cactus_map[index][2] > cactus_map[index + 1][2]:
                move_to(cactus_map[index][0], cactus_map[index][1])
                swap(North)
                cactus_map[index] = get_pos_x(), get_pos_y(), measure()
                move_to(cactus_map[index + 1][0], cactus_map[index + 1][1])
                cactus_map[index + 1] = get_pos_x(), get_pos_y(), measure()
                sorted = False

    for i in range(get_world_size() - 1):
        for j in range(get_world_size()):
            index = i * get_world_size() + j
            if cactus_map[index][2] > cactus_map[(i + 1) * get_world_size() + j][2]:
                move_to(cactus_map[index][0], cactus_map[index][1])
                swap(East)
                cactus_map[index] = get_pos_x(), get_pos_y(), measure()
                move_to(cactus_map[(i + 1) * get_world_size() + j][0], cactus_map[(i + 1) * get_world_size() + j][1])
                cactus_map[(i + 1) * get_world_size() + j] = get_pos_x(), get_pos_y(), measure()
                sorted = False

harvest()


def farm_cacti(n):
    while num_items(Items.Cactus) < n:
        plant_cacti()
        sort_cacti()