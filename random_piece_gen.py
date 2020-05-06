import copy
import random

x,y = 2, 2
width, height = 5, 5

arr = [copy.deepcopy([False for x in range(width)]) for y in range(height)]
forms = [
        [
            [0,1,1,0,0],
            [0,1,0,0,0],
            [0,1,0,0,0],
            [0,1,0,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,0,0],
            [0,1,1,0,0],
            [0,1,0,0,0],
            [0,1,0,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,0,0],
            [0,1,1,0,0],
            [0,1,1,0,0],
            [0,1,0,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,1,0],
            [0,1,1,0,0],
            [0,1,1,0,0],
            [0,1,0,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,1,0],
            [0,1,1,0,0],
            [0,1,1,0,0],
            [0,1,1,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,1,0],
            [0,1,1,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,1,0],
            [0,1,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,1,0],
            [0,1,0,0,0],
            [0,1,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ],[
            [0,1,1,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ],[
            [1,1,1,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        ]


def choose_form(forms):
    return forms[random.randint(0,len(forms)-1)]


def side_gen(side, arr, index):
    if random.randint(1,250) > 30:
        # 0=left
        # 1=right
        # 2=up
        # 3=down
        if side == 0 and index['x'] > 0:
            arr[index['y']][index['x'] - 1] = True
            index['x'] -= 1
            return arr, index
        if side == 1 and index['x'] < len(arr[index['y']]) - 1:
            arr[index['y']][index['x'] + 1] = True
            index['x'] += 1
            return arr, index
        if side == 2 and index['y'] > 0:
            arr[index['y'] - 1][index['x']] = True
            index['y'] -= 1
            return arr, index
        if side == 3 and index['y'] < len(arr) - 1:
            arr[index['y'] + 1][index['x']] = True
            index['y'] += 1
            return arr, index
    return arr, index

count = 0

def rec_side_gen(arr, index):
    global count
    for side in range(4):
        if random.randint(0,120) > 13:
            arr, index2 = side_gen(side, arr, index)
            if count < 8:
                count += 1
                arr2 = rec_side_gen(arr, index2)
                for y in range(len(arr2)):
                    for x in range(len(arr2[y])):
                        if arr2[y][x]:
                            arr[y][x] = True
    return arr

def test():
    global arr,x,y,forms
    '''
    arr = [copy.deepcopy([False for x in range(width)]) for y in range(height)]
    arr[y][x] = True
    arr = rec_side_gen(arr, {'x':x,'y':y})
    '''
    arr = copy.deepcopy(choose_form(forms))
    return arr
