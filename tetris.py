#!/bin/python3
import pygame
import sys
import copy
import math
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

def random_piece_gen():
    global arr,x,y,forms
    '''
    arr = [copy.deepcopy([False for x in range(width)]) for y in range(height)]
    arr[y][x] = True
    arr = rec_side_gen(arr, {'x':x,'y':y})
    '''
    arr = copy.deepcopy(choose_form(forms))
    return arr

def move_down(fall, keys, check_floor):
    if keys['s']:
        if check_floor():
            fall()

width = 400
height = 600
block_size = 20
fps = 25

colors = {
        'lightblue':[100,200,200],
        'white':[255,255,255],
        'blue':[0,30,200],
        'red':[200,30,20],
        'green':[5,190,20],
        'black':[0,0,0],
        'random':[255,255,255],
        'bluegreen':[0,255,255],
        'redblue':[255,0,255],
        }

def random_255(minimum, maximum):
    return random.randint(minimum, maximum)

def gen_random_color(color):
    global colors
    colors[color] = []
    if 'red' in color or color == random:
        colors[color].append(random_255(180, 255))
    else:
        colors[color].append(random_255(0,120))
    if 'green' in color or color == random:
        colors[color].append(random_255(180, 255))
    else:
        colors[color].append(random_255(0,120))
    if 'blue' in color or color == random:
        colors[color].append(random_255(180, 255))
    else:
        colors[color].append(random_255(0,120))


def gen_random_color_all():
    gen_random_color('blue')
    gen_random_color('red')
    gen_random_color('green')
    gen_random_color('redblue')
    gen_random_color('bluegreen')
    gen_random_color('random')


gen_random_color_all()

def array2d_init(width, height, val):
    return [copy.deepcopy([copy.deepcopy(val) for x in range(width)]) for y in range(height)]


def index_wh(screen_width, screen_height, rect_width, rect_height):
    index_width = int(screen_width / rect_width)
    index_height = int(screen_height / rect_height)
    return index_width, index_height


class array2d:
    def init(self, screen_width, screen_height, rect_width, rect_height):
        self.index_width, self.index_height = index_wh(screen_width, screen_height, rect_width, rect_height)
    def make(self, inner):
        self.array2d = array2d_init(self.index_width, self.index_height, inner)


class rect_array2d(array2d):
    def __init__(self, screen_width, screen_height, rect_width, rect_height):
        self.init(screen_width, screen_height, rect_width, rect_height)
        inner = [0 for x in range(4)]
        self.make(inner)
        for y in range(self.index_height):
            for x in range(self.index_width):
                self.array2d[y][x][0] = rect_width * x# x
                self.array2d[y][x][1] = rect_height * y# y
                self.array2d[y][x][2] = rect_width# width
                self.array2d[y][x][3] = rect_height# height


class data_array2d(array2d):
    def __init__(self, screen_width, screen_height, rect_width, rect_height):
        self.init(screen_width, screen_height, rect_width, rect_height)
        inner = 'black'
        self.make(inner)

pygame.init()

size = width, height

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

keys = {'up':False,'down':False,'left':False,'right':False,'a':False,'d':False, 'e':False, 'q':False, 's':False}

rect2d = rect_array2d(width, height, block_size, block_size)
data2d = data_array2d(width, height, block_size, block_size)


fallenX = []
fallenY = []

piece_spawn = True

xLim = 0
xMov = False
floor = []
color = 'white'
colorArr = []
colorNumArr = [x for x in range(5)]

def rand_color():
    global color, colorNumArr
    gen_random_color_all()
    numIndex = random.randint(0,len(colorNumArr) - 1)
    num = colorNumArr[numIndex]
    del colorNumArr[numIndex]
    if len(colorNumArr) > 0:
        pass
    else:
        colorNumArr = []
        for x in range(5):
            if x == num:
                continue
            else:
                colorNumArr.append(x)
    if num == 0:
        color = 'blue'
    if num == 1:
        color = 'red'
    if num == 2:
        color = 'bluegreen'
    if num == 3:
        color = 'green'
    if num == 4:
        color = 'redblue'


def check_walls(xArr):
    global rect2d
    for x in xArr:
        if x >= rect2d.index_width or x < 0:
            return False
    return True


def init_floor():
    global floor
    floor = []
    for x in range(int(width / block_size)):
        floor.append(int(height / block_size) - 1)

init_floor()

def check_xArr(xArr):
    global floor, xLim
    if xLim == 1:
        xLim = 0
    answer = True
    for indexX in xArr:
        if indexX >= len(floor):
            answer = False
        if indexX == len(floor) - 1:
            xLim = 1
    return answer

def check_floor(xArr1, yArr1):
    global floor
    touch_floor = False
    for indexY, indexX in zip(yArr1, xArr1):
        if floor[indexX] + 1 <= indexY:
            touch_floor = True
            return False
    return True

def check_comlex_floor(xArr1, yArr1, xArr2, yArr2, yAdd):
    for x1, y1 in zip(xArr1, yArr1):
        for x2, y2 in zip(xArr2, yArr2):
            if x1 == x2 and y1 + yAdd == y2:
                return False
    return True

def check_comlex_floorArr(xArr1, yArr1, fallenX, fallenY, yAdd):
    for xArr2,yArr2 in zip(fallenX,fallenY):
        if not check_comlex_floor(xArr1, yArr1, xArr2, yArr2, yAdd):
            return False
    return True

def fall(xArr1, yArr1):
    yArrAnswer = []
    for indexY in copy.deepcopy(yArr1):
        yArrAnswer.append(indexY + 1)
    return yArrAnswer


def moveX(keys, data2d, indexX):
    global xLim, xMov
    if keys['a']:
        indexX -= 1
        if indexX > 0 and xLim >= 0:
            xLim = 0
            xMov = True
        elif indexX == 0:
            xLim = -1
    if keys['d']:
        indexX += 1
        if indexX < len(data2d.array2d[0]) - 1 and xLim <= 0:
            xLim = 0
            xMov = True
        elif indexX == len(data2d.array2d[0]) - 1:
            xLim = 1
    return indexX

def moveXArr(keys, data2d, indexXArr):
    global xMov, piece_spawn, xLim
    localindexX = copy.deepcopy(indexXArr)
    if not xLim == 0:
        #xLim = 0
        for x in range(len(indexXArr)):
            moveX(keys,data2d,indexXArr[x])
        return indexXArr
    for x in range(len(indexXArr)):
        localindexX[x] = moveX(keys,data2d,indexXArr[x])
    if xMov and not piece_spawn:
        indexXArr = copy.deepcopy(localindexX)
    return indexXArr


xArr = []
yArr = []


def findMiddleIndexArr(iArr):
    answer = 0
    maximum = 0
    minimum = iArr[0]
    allEqual = True
    allI = iArr[0]
    for i in iArr:
        if not allI == i:
            allEqual = False
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return int(math.floor((maximum + minimum) / 2)), maximum, minimum, allEqual, ((maximum + minimum) / 2) - math.floor((maximum + minimum) / 2)

def rotate_upleft(fallenX, fallenY):
    global xArr, yArr, keys
    right=False
    if keys['e']:
        right=True
        keys['e'] = False
    elif not keys['q']:
        return
    else:
        keys['q'] = False
    middlex, maximumx, minimumx, allEqualx, halfx = findMiddleIndexArr(xArr)
    middley, maximumy, minimumy, allEqualy, halfy = findMiddleIndexArr(yArr)
    localXArr = copy.deepcopy(xArr)
    localYArr = copy.deepcopy(yArr)
    count = 0
    ay = 1
    ax = 1
    adderx = 0
    addery = 0
    if right:
        ay = -1
        ax = 1
        adderx = maximumy - minimumy
    else:
        ay = 1
        ax = -1
        addery = maximumx - minimumx
    for y in yArr:
        xArr[count] = ((y - minimumy)*ay) + minimumx + adderx
        count += 1
    count = 0
    for x in localXArr:
        yArr[count] = ((x - minimumx)*ax) + minimumy + addery
        count += 1
    if not check_xArr(xArr):
        xArr = localXArr
        yArr = localYArr
        return
    if not check_floor(xArr, yArr) or not check_comlex_floorArr(xArr, yArr, fallenX, fallenY, 1):
        xArr = localXArr
        yArr = localYArr

def flip_xArr():
    global xArr, yArr, fallenX, fallenY, keys
    localXArr = []
    middle, maximum, minimum, allEqual, half = findMiddleIndexArr(xArr)
    one = 0
    if half == 0.5:
        one = 1
    if allEqual:
        return
    if keys['left'] or keys['right']:
        if keys['left']:
            keys['left'] = False
        if keys['right']:
            keys['right'] = False
        for x in xArr:
            if x - minimum <= middle:
                localXArr.append(((middle - (x)) + middle) + one)
            else:
                localXArr.append((middle - ((x) - middle)) + one)
        if check_floor(xArr, yArr) and check_comlex_floorArr(xArr, yArr, fallenX, fallenY, 1):
            xArr = copy.deepcopy(localXArr)

def flip_yArr():
    global xArr, yArr, fallenX, fallenY, keys
    localYArr = []
    middle, maximum, minimum, allEqual, half = findMiddleIndexArr(yArr)
    one = 0
    if half == 0.5:
        one = 1
    if allEqual:
        return
    if keys['down'] or keys['up']:
        if keys['down']:
            keys['down'] = False
        if keys['up']:
            keys['up'] = False
        for y in yArr:
            if y - minimum <= middle:
                localYArr.append(((middle - (y)) + middle) + one)
            else:
                localYArr.append((middle - ((y) - middle)) + one)
        if check_floor(xArr, yArr) and check_comlex_floorArr(xArr, yArr, fallenX, fallenY, 1):
            yArr = copy.deepcopy(localYArr)

def from_array2dBool(array2dBool):
    global xArr, yArr, width
    xArr = []
    yArr = []
    xPos = random.randint(0, (width / block_size) - len(array2dBool[0]))
    for y in range(len(array2dBool)):
        for x in range(len(array2dBool[y])):
            if array2dBool[y][x] == True:
                xArr.append(x + xPos)
                yArr.append(y)

def blacken_data():
    global data2d
    x = 0
    y = 0
    while y < len(data2d.array2d):
        while x < len(data2d.array2d[y]):
            data2d.array2d[y][x] = [0,0,0]
            x += 1
        y += 1
        x = 0

def make_data(xArr, yArr, color):
    global data2d
    for xIndex,yIndex in zip(xArr,yArr):
        data2d.array2d[yIndex][xIndex] = color

def make_datas(fallenX, fallenY, colorArr):
    for xArr, yArr, color in zip(fallenX, fallenY, colorArr):
        make_data(xArr, yArr, color)

def draw_from_data():
    global screen, rect2d, data2d
    indexy = 0
    indexx = 0
    for y in data2d.array2d:
        for x in y:
            if not x == [0,0,0]:
                screen.fill(x, rect2d.array2d[indexy][indexx])
            indexx += 1
        indexy += 1
        indexx = 0


def reset_game():
    global fallenX, fallenY, xArr, yArr, score, game_over, piece_spawn, game_pause, colorArr
    fallenX = []
    fallenY = []
    xArr = []
    yArr = []
    colorArr = []
    score = 0
    game_over = False
    game_pause = True
    piece_spawn = True

game_pause = False

def key_event(down, key):
    global keys, game_pause, game_over
    if key == pygame.K_UP:
        keys['up'] = down
    if key == pygame.K_DOWN:
        keys['down'] = down
    if key == pygame.K_LEFT:
        keys['left'] = down
    if key == pygame.K_RIGHT:
        keys['right'] = down
    if key == pygame.K_a:
        keys['a'] = down
    if key == pygame.K_d:
        keys['d'] = down
    if key == pygame.K_q:
        keys['q'] = down
    if key == pygame.K_e:
        keys['e'] = down
    if key == pygame.K_s:
        keys['s'] = down
    if key == pygame.K_SPACE and down:
        game_pause = not game_pause
        if game_over:
            reset_game()


def check_game_over(yArr):
    for y in yArr:
        if y == 0:
            return True
    return False

counter = 10
count = 0

score = 0
game_over = False

passes = {
        'count':0,
        'limit':4,
        }

rand_color()

def fall_custom():
    global xArr, yArr
    yArr = fall(xArr, yArr)


def check_floor_custom():
    global xArr, yArr, fallenX, fallenY
    return check_floor(xArr, yArr) and check_comlex_floorArr(xArr, yArr, fallenX, fallenY, 1)

while True:
    clock.tick(fps)
    if piece_spawn:
        xLim = 0
        xMov = False
        if len(xArr) > 0:
            score += 1
            if check_game_over(yArr):
                game_over = True
                print(score)
            colorArr.append(copy.deepcopy(colors[color]))
            rand_color()
            fallenX.append(copy.deepcopy(xArr))
            fallenY.append(copy.deepcopy(yArr))
        array2dBool = random_piece_gen()
        from_array2dBool(array2dBool)
        piece_spawn = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_event(True, event.key)
        if event.type == pygame.KEYUP:
            key_event(False, event.key)
    if game_pause or game_over:
        continue
    passes['count'] += 1
    blacken_data()
    make_data(xArr, yArr, colors[color])
    make_datas(fallenX, fallenY, colorArr)
    draw_from_data()
    pygame.display.flip()
    screen.fill(colors['black'])
    localXArr = copy.deepcopy(xArr)
    localYArr = copy.deepcopy(yArr)
    if passes['count'] >= passes['limit']:
        passes['count'] = 0
        yArr = fall(xArr, yArr)
    if not check_comlex_floorArr(xArr, yArr, fallenX, fallenY, 0) or not check_floor(xArr, yArr):
        xArr = copy.deepcopy(localXArr)
        yArr = copy.deepcopy(localYArr)
        piece_spawn = True
        continue
    flip_xArr()
    flip_yArr()
    rotate_upleft(fallenX, fallenY)
    xArr = moveXArr(keys, data2d, xArr)
    if not check_walls(xArr):
        xArr = copy.deepcopy(localXArr)
    if not check_comlex_floorArr(xArr, yArr, fallenX, fallenY, 0) or not check_floor(xArr, yArr):
        xArr = copy.deepcopy(localXArr)
        yArr = copy.deepcopy(localYArr)
        piece_spawn = True
    localXArr = copy.deepcopy(xArr)
    localYArr = copy.deepcopy(yArr)
    move_down(fall_custom, keys,check_floor_custom)
    if not check_comlex_floorArr(xArr, yArr, fallenX, fallenY, 0) or not check_floor(xArr, yArr):
        xArr = copy.deepcopy(localXArr)
        yArr = copy.deepcopy(localYArr)
        piece_spawn = True
