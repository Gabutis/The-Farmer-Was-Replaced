def plant_pumpkin():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if num_items(Items.Pumpkin_Seed) < 150:
                if num_items(Items.Carrot) < 1500:
                    farm_carrot(1500)
                trade(Items.Pumpkin_Seed, 150)
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)
            move(North)
        move(East)

def coord_in_list(coord, coord_list):
    for c in coord_list:
        if coord == c:
            return True
    return False

def check_pumpkin():
    pumpkin_list = []
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            coord = (get_pos_x(), get_pos_y())
            if get_entity_type() != Entities.Pumpkin:
                if not coord_in_list(coord, pumpkin_list):
                    pumpkin_list.append(coord)
                if num_items(Items.Pumpkin_Seed) < 2:
                    trade(Items.Pumpkin_Seed, 2)
                plant(Entities.Pumpkin)
                water()
            move(North)
        move(East)

    while len(pumpkin_list) > 0:
        x, y = pumpkin_list.pop(0)
        move_to(x, y)
        if get_entity_type() != Entities.Pumpkin:
            plant(Entities.Pumpkin)
        if get_entity_type() == Entities.Pumpkin and not can_harvest():
            while not can_harvest():
                if get_entity_type() == Entities.Pumpkin:
                    if num_items(Items.Fertilizer) < 2:
                        trade(Items.Fertilizer, 2)
                    use_item(Items.Fertilizer)
                else:
                    plant(Entities.Pumpkin)
        if get_entity_type() == Entities.Pumpkin and can_harvest():
            continue

def farm_pumpkin(n):
    while num_items(Items.Pumpkin) < n:
        plant_pumpkin()
        check_pumpkin()
        harvest()
