def move_down(fall, keys, check_floor):
    if keys['s']:
        if check_floor():
            fall()
