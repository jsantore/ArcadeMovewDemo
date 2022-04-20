import types

import arcade
import random

import Comp151Window


def main():
    window = Comp151Window.Comp151Window(800, 800, "Moving demo")
    window.ship = arcade.Sprite("galleon.png")
    window.ship.center_x = 350
    window.ship.center_y = 350
    window.ship_dx =0
    window.coins = arcade.Sprite("gold-coins-large.png")
    window.coins.center_x = random.randint(36, 664)
    window.coins.center_y = random.randint(36, 664)
    window.on_draw = types.MethodType(comp151_draw, window) #magic line to make comp151 draw work for arcade
    window.on_key_press = types.MethodType(handle_key_press, window)
    arcade.run()

def comp151_draw(window):
    arcade.start_render()
    if window.ship_dx != 0:
        window.ship.center_x += window.ship_dx
    window.ship.draw()
    window.coins.draw()
    arcade.finish_render()

def handle_key_press(window, key, mod):
    if key == arcade.key.LEFT:
        window.ship_dx= -3
    elif key == arcade.key.RIGHT:
        window.ship_dx =3

main()