import pgzrun
import random

HEIGHT=600
WIDTH=800

START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"] #Non Recycable

FINAL_LVL = 6
current_lvl = 1

#losing the game
game_over = False
#win the game
game_complete = False

items = []

animations = []

def draw():
    global items, current_lvl, game_over, game_complete
    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("GAME OVER","Try again")
    elif game_complete:
        display_message("YOU WON","Well done!")
    else:
        for item in items:
            item.draw()

def display_message(heading, subheading):
    screen.draw.text(heading, fontsize=60, center=(400,300),color = "black")
    screen.draw.text(subheading, fontsize=30, center=(400,350),color = "black")

def update():
    global items
    if len(items) == 0:
        items= make_items(current_lvl)

#Make items
#1.get the options from ITEMS list - random
#2.Create actors and add it to items list
#3.Layout items - display them with equal spacing
#4.Animations - move the objects down

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create=["paper"]
    for i in range(0, number_of_extra_items):
        items_to_create.append(random.choice(ITEMS))  #random.choice makes it a random value out of a list or a string
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1 #len finds how many values are in a list
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout): # enumerate finds index value of object
        new_x_pos = (index+1)* gap_size # makes the spacing even on screen
        item.x= new_x_pos


def animate_items(items_to_animate):
    global animations 
    for item in items_to_animate:
        duration = START_SPEED-current_lvl
        animation= animate(item,duration = duration, on_finished= handle_game_over, y=HEIGHT) #checks if object goes to the bottom and ends game if yes
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()   # calls the function that makes it so after all lvls game complete screen shows up
            else:
                handle_game_over()  # checks if you clicked wrong item, and then calls a function

def handle_game_complete():   #function that makes game complete screen
    global current_lvl, items, game_complete, animations
    stop_animations(animations)
    if current_lvl == FINAL_LVL:
        game_complete = True
    else:
        current_lvl = current_lvl + 1  # makes the next lvl happen
        items = []
        animations = []

def stop_animations(animations_to_stop):  # makes animations stop after winning or losing
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
 
pgzrun.go()
