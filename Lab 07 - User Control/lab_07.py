""" Lab 7 - User Control """

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

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

class Cactus:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        x = self.position_x
        y = self.position_y

        arcade.draw_ellipse_filled(15 + x, 18 + y, 200, 50, arcade.color.DARK_GREEN, 90)
        arcade.draw_ellipse_filled(15 + x, 40 + y, 150, 25, arcade.color.DARK_GREEN, 180)
        arcade.draw_ellipse_filled(x + 80, 65 + y, 70, 25, arcade.color.DARK_GREEN, 90)
        arcade.draw_ellipse_filled(x + 20 - 70, 65 + y, 70, 25, arcade.color.DARK_GREEN, 90)


class Cloud:
    def __init__(self, position_x, position_y, radius, color):
        self.change_x = 0
        self.change_y = 0
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color


    def draw(self):
        x = self.position_x
        y = self.position_y

        arcade.draw_circle_filled(180 + x, 180 + y, 60, arcade.color.WHITE)
        arcade.draw_circle_filled(250 + x, 260 + y, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(260 + x, 190 + y, 40, arcade.color.WHITE)
        arcade.draw_circle_filled(170 + x, 250 + y, 40, arcade.color.WHITE)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


def draw_background():
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.SAND)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self, width, height, title):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.laser_sound = arcade.load_sound("laser.wav")

        self.set_mouse_visible(False)

        self.cactus = Cactus(50, 50, 0, 0, 25, arcade.color.DARK_GREEN)
        self.cloud = Cloud(50, 50, 0, arcade.color.WHITE)


    def on_draw(self):
        arcade.start_render()
        draw_background()
        self.cactus.draw()
        self.cloud.draw()

    def update(self, delta_time):
        self.cloud.update()

    def on_key_press(self, key, modifiers):
        print("Hello")
        if key == arcade.key.LEFT:
            self.cloud.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.cloud.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.cloud.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.cloud.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.cloud.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.cloud.change_y = 0


    def on_mouse_motion(self, x, y, dx, dy):

        self.cactus.position_x = x
        self.cactus.position_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers):
        laser_sound = arcade.load_sound("laser.wav")
        arcade.play_sound(laser_sound)

        self.laser = arcade.load_sound("laser.wav")
        self.laser_sound_player = None

        if not self.laser_sound_player or not self.laser_sound_player:
            self.laser_sound_player = arcade.play_sound(self.laser_sound)

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.laser_sound)


def main():
    MyGame(600, 800, "Lab 7")
    arcade.run()


main()
