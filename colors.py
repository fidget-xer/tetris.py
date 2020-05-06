import random

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
