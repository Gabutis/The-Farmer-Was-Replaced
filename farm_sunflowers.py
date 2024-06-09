def plant_sunflowers():
    if num_items(Items.Sunflower_Seed) < 1:
        if num_items(Items.Carrot) < 900:
            farm_carrot(900)
        trade(Items.Sunflower_Seed, 150)
    if get_ground_type() != Grounds.Soil:
        till()
    if get_entity_type != Entities.Sunflower:
        plant(Entities.Sunflower)


def farm_sunflowers(n):
    sunflower_map = []

    for i in range(get_world_size()):
        for i in range(get_world_size()):
            plant_sunflowers()
            x, y = get_pos_x(), get_pos_y()
            value = measure()
            sunflower_map.append((x, y, value))
            move(North)
        move(East)


while num_items(Items.Power) < n:
    # Find the top value coordinates
    max_value = -1
    top_item = None
    for item in sunflower_map:
        if item[2] > max_value:
            max_value = item[2]
            top_item = item

    if top_item == None:
        break

    move_to(top_item[0], top_item[1])

    while not can_harvest():
        if num_items(Items.Fertilizer) < 2 and num_items(Items.Pumpkin) > 20:
            trade(Items.Fertilizer, 2)
        elif num_items(Items.Fertilizer) > 1:
            use_item(Items.Fertilizer)
        else:
            water()

    harvest()
    plant_sunflowers()
    new_value = measure()
    sunflower_map.remove(top_item)
    sunflower_map.append((top_item[0], top_item[1], new_value))