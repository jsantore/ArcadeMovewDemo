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
    window.ship_dy = 0
    window.coins = arcade.Sprite("gold-coins-large.png")
    window.coins.center_x = random.randint(36, 664)
    window.coins.center_y = random.randint(36, 664)
    window.on_draw = types.MethodType(comp151_draw, window) #magic line to make comp151 draw work for arcade
    window.on_key_press = types.MethodType(handle_key_press, window)
    window.on_key_release = types.MethodType(handle_key_release, window)
    arcade.run()

def comp151_draw(window):
    arcade.start_render()
    if window.ship_dx != 0:
        window.ship.center_x += window.ship_dx
    if window.ship_dy !=0:
        window.ship.center_y += window.ship_dy
    if window.ship.center_x <-36:
        window.ship.center_x = 836
    if window.ship.center_x > 836:
        window.ship.center_x = -36
    window.ship.draw()
    window.coins.draw()
    arcade.finish_render()

def handle_key_press(window, key, mod):
    if key == arcade.key.LEFT:
        window.ship_dx= -3
    elif key == arcade.key.RIGHT:
        window.ship_dx =3
    if key == arcade.key.UP:
        window.ship_dy = 3
    elif key == arcade.key.DOWN:
        window.ship_dy = -3

def handle_key_release(window, key, mod):
    if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        window.ship_dx =0
    if key == arcade.key.UP or key == arcade.key.DOWN:
        window.ship_dy =0

main()