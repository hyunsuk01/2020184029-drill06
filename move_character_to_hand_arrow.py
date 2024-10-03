from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def random_hand():
    hand_x = random.randint(0, TUK_WIDTH)
    hand_y = random.randint(0, TUK_HEIGHT)
    return hand_x, hand_y

def move_character(x1, y1, x2, y2, speed = 1):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if distance == 0:
        return x1, y1

    if distance > speed:
        t = speed / distance
    else:
        t = 1
    new_x = (1 - t) * x1 + t * x2
    new_y = (1 - t) * y1 + t * y2

    return new_x, new_y

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x, hand_y = random_hand()
frame = 0

hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(hand_x, hand_y)

    x, y = move_character(x, y, hand_x, hand_y)
    if (x - hand_x < 1 and hand_x - x < 1) and (y - hand_y < 1 and hand_y - y < 1):
        hand_x, hand_y = random_hand()
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()