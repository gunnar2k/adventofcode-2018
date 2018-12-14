input = open("input.txt")
track = [list(row.rstrip()) for row in input]

CART_SYMBOLS = "<^>v"
TURN_SYMBOLS = "/\\"
INTERSECTION_SYMBOL = "+"

TURN_LEFT = "<"
TURN_FORWARD = "^"
TURN_RIGHT = ">"

DIRECTION_UP = "^"
DIRECTION_LEFT = "<"
DIRECTION_RIGHT = ">"
DIRECTION_DOWN = "v"

directions = {
    "^": DIRECTION_UP,
    ">": DIRECTION_RIGHT,
    "<": DIRECTION_LEFT,
    "v": DIRECTION_DOWN,
}


'''
Lift the carts from the track and replace with tracks
'''

carts = {}
cart_id = 1
for x, row in enumerate(track):
    for y, val in enumerate(row):
        if val in CART_SYMBOLS:
            direction = directions[val]
            carts[cart_id] = {
                'x': x,
                'y': y,
                'direction': direction,
                'prev_intersection_turn': TURN_RIGHT,
            }
            cart_id += 1

            if direction == DIRECTION_UP:
                track[x][y] = "|"
            elif direction == DIRECTION_RIGHT:
                track[x][y] = "-"
            elif direction == DIRECTION_DOWN:
                track[x][y] = "|"
            elif direction == DIRECTION_LEFT:
                track[x][y] = "-"


def is_occupied(x, y):
    for id, cart in carts.items():
        if cart['x'] == x and cart['y'] == y:
            return True
    return False

def is_turn(x,y):
    if track[x][y] in TURN_SYMBOLS:
        return True
    return False

def turn(cart_id,x,y):
    turn_symbol = track[x][y]
    current_direction = carts[cart_id]['direction']
    if direction == DIRECTION_UP and turn_symbol == "/":
        carts[cart_id]['direction'] = DIRECTION_RIGHT
    elif direction == DIRECTION_RIGHT and turn_symbol == "/":
        carts[cart_id]['direction'] = DIRECTION_UP
    elif direction == DIRECTION_LEFT and turn_symbol == "/":
        carts[cart_id]['direction'] = DIRECTION_DOWN
    elif direction == DIRECTION_DOWN and turn_symbol == "/":
        carts[cart_id]['direction'] = DIRECTION_LEFT
    elif direction == DIRECTION_UP and turn_symbol == "\\":
        carts[cart_id]['direction'] = DIRECTION_LEFT
    elif direction == DIRECTION_RIGHT and turn_symbol == "\\":
        carts[cart_id]['direction'] = DIRECTION_DOWN
    elif direction == DIRECTION_LEFT and turn_symbol == "\\":
        carts[cart_id]['direction'] = DIRECTION_UP
    elif direction == DIRECTION_DOWN and turn_symbol == "\\":
        carts[cart_id]['direction'] = DIRECTION_RIGHT

def is_intersection(x,y):
    if track[x][y] == INTERSECTION_SYMBOL:
        return True
    return False

def intersection(cart_id,x,y):
    prev_intersection_turn = carts[cart_id]['prev_intersection_turn']
    current_intersection_turn = None

    if prev_intersection_turn == TURN_RIGHT:
        current_intersection_turn = TURN_LEFT
    elif prev_intersection_turn == TURN_LEFT:
        current_intersection_turn = TURN_FORWARD
    elif prev_intersection_turn == TURN_FORWARD:
        current_intersection_turn = TURN_RIGHT

    direction = carts[cart_id]['direction']
    new_direction = direction
    if direction == DIRECTION_UP:
        if current_intersection_turn == TURN_RIGHT:
            new_direction = DIRECTION_RIGHT
        if current_intersection_turn == TURN_LEFT:
            new_direction = DIRECTION_LEFT
    elif direction == DIRECTION_RIGHT:
        if current_intersection_turn == TURN_RIGHT:
            new_direction = DIRECTION_DOWN
        if current_intersection_turn == TURN_LEFT:
            new_direction = DIRECTION_UP
    elif direction == DIRECTION_DOWN:
        if current_intersection_turn == TURN_RIGHT:
            new_direction = DIRECTION_LEFT
        if current_intersection_turn == TURN_LEFT:
            new_direction = DIRECTION_RIGHT
    elif direction == DIRECTION_LEFT:
        if current_intersection_turn == TURN_RIGHT:
            new_direction = DIRECTION_UP
        if current_intersection_turn == TURN_LEFT:
            new_direction = DIRECTION_DOWN

    carts[cart_id]['direction'] = new_direction
    carts[cart_id]['prev_intersection_turn'] = current_intersection_turn

def cart_id_at(x,y):
    for id, cart in carts.items():
        if cart['x'] == x and cart['y'] == y:
            return id

def print_track():
    for row in track:
        print("".join(row))

while True:
    for id, cart in sorted(carts.items(), key=lambda c: (c[1]['x'],c[1]['y'])):
        if id not in carts:
            continue

        if len(carts) == 1:
            print(carts)
            exit()

        x = cart['x']
        y = cart['y']

        direction = cart['direction']
        prev_intersection_turn = cart['prev_intersection_turn']

        # find the next coordinate of the cart
        x_next = x
        y_next = y
        if direction == DIRECTION_UP:
            x_next -= 1
        elif direction == DIRECTION_DOWN:
            x_next += 1
        elif direction == DIRECTION_RIGHT:
            y_next += 1
        elif direction == DIRECTION_LEFT:
            y_next -= 1

        if is_occupied(x_next, y_next):
            # Part 1:
            # print("CRASH", y_next, x_next)
            # exit()
            occupying_cart_id = cart_id_at(x_next,y_next)
            del carts[id]
            del carts[occupying_cart_id]
            continue

        if is_turn(x_next, y_next):
            turn(id, x_next, y_next)

        if is_intersection(x_next, y_next):
            intersection(id, x_next, y_next)

        carts[id]['x'] = x_next
        carts[id]['y'] = y_next
