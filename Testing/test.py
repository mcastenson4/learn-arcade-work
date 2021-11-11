import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 850
MOVEMENT_SPEED = 8


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




class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)


        self.laser_sound = arcade.load_sound("arcade_resources_sounds_upgrade4.wav")

        self.flower = Cactus(50, 50, 0, 0, 25, arcade.color.DARK_GREEN)
        self.cloud = Cloud(50, 50, 0, arcade.color.WHITE)
        self.set_mouse_visible(False)


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.cactus.draw()
        self.cloud.draw()



    def on_mouse_motion(self, x, y, dx, dy):
        self.cloud.position_x = x
        self.cloud.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.pacman.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.pacman.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.pacman.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.pacman.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.pacman.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.pacman.change_y = 0


def main():
    MyGame(640, 480, "Lab 7")
    arcade.run()


main()
