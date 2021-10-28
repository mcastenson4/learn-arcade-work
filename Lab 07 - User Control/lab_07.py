""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.start_render()

def draw_sand():
    """ Draw the sand """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.SAND)

def draw_a_cactus(x, y):
    """ Draw a cactus """

    arcade.draw_ellipse_filled(15 + x, 18 + y, 200, 50, arcade.color.DARK_GREEN, 90)
    arcade.draw_ellipse_filled(15 + x, 40 + y, 150, 25, arcade.color.DARK_GREEN, 180)
    arcade.draw_ellipse_filled(x + 80, 65 + y, 70, 25, arcade.color.DARK_GREEN, 90)
    arcade.draw_ellipse_filled(x + 20 - 70, 65 + y, 70, 25, arcade.color.DARK_GREEN, 90)


def draw_a_cloud(x, y):
    arcade.draw_circle_filled(180 + x, 180 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(250 + x, 260 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(260 + x, 190 + y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(170 + x, 250 + y, 40, arcade.color.WHITE)

def draw_sun(x, y):
    arcade.draw_circle_filled(x + 25 - 180, 270 + y, 50, arcade.csscolor.YELLOW)
    arcade.draw_rectangle_filled(x + 25 - 140, 220 + y, 50, 10, arcade.csscolor.YELLOW, 45)
    arcade.draw_rectangle_filled(x + 25 - 140, 220 + y, 50, 10, arcade.csscolor.YELLOW, 45)
    arcade.draw_rectangle_filled(x + 25 - 180, 210 + y, 50, 10, arcade.csscolor.YELLOW, 90)
    arcade.draw_rectangle_filled(x + 25 - 120, 260 + y, 50, 10, arcade.csscolor.YELLOW, 180)
    arcade.draw_rectangle_filled(x + 25 - 120, 295 + y, 50, 10, arcade.csscolor.YELLOW, 165)
    arcade.draw_rectangle_filled(x + 25 - 210, 215 + y, 50, 10, arcade.csscolor.YELLOW, 115)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

    draw_sand()
    draw_a_cactus(400, 280)
    draw_a_cloud(300, 300)
    draw_sun(200, 300)
    draw_a_cloud(50, 300)
    draw_a_cloud(500, 200)
    draw_a_cactus(100, 200)
    draw_a_cactus(300, 100)
    draw_a_cactus(600, 250)
    draw_a_cactus(720, 100)

def main():
    window = MyGame()
    arcade.run()


main()
