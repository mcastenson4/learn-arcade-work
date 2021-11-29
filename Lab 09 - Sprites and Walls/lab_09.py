""" Sprite Sample Program """

import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_ROBOT = 0.5
SPRITE_SCALING_STAR = 0.2
STAR_COUNT = 40

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

MOVEMENT_SPEED = 5
CAMERA_SPEED = 1


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.robot_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.robot_sprite = None
        self.score = 0

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.PINK)

        # Sprite lists
        self.robot_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.robot_sprite = arcade.Sprite("robot_jump.png", SPRITE_SCALING_ROBOT)
        self.robot_sprite.center_x = 160
        self.robot_sprite.center_y = 120
        self.robot_list.append(self.robot_sprite)

        # Manually create and position a box at 300, 200
        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 600
        wall.center_y = 150
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 650
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 150
        wall.center_y = 500
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 200
        wall.center_y = 900
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 400
        wall.center_y = 965
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 670
        wall.center_y = 450
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 670
        wall.center_y = 965
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 750
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 200
        wall.center_y = 250
        self.wall_list.append(wall)

        # --- Left
        for x in range(128, 1024, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)
        # --- Bottom
        for y in range(0, 1024, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 90
            wall.center_y = y
            self.wall_list.append(wall)
        # --- Top
        for x in range(128, 1024, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)
        # --- Bottom
        for y in range(0, 1024, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 1024
            wall.center_y = y
            self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 640
            self.wall_list.append(wall)

        for x in range(173, 832, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 320
            self.wall_list.append(wall)

        for x in range(173, 832, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 808
            self.wall_list.append(wall)

        for x in range(173, 300, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 720
            self.wall_list.append(wall)

        for x in range(250, 450, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        for y in range(300, 200, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 550
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(173, 500, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 880
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(173, 500, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 810
            wall.center_y = y
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        for i in range(STAR_COUNT):
            star = arcade.Sprite("star.png", SPRITE_SCALING_STAR)

            coin_placed_successfully = False

        # Keep trying until success
            while not coin_placed_successfully:

                star.center_x = random.randrange(960)
                star.center_y = random.randrange(960)

                wall_hit_list = arcade.check_for_collision_with_list(star, self.wall_list)

                star_hit_list = arcade.check_for_collision_with_list(star, self.coin_list)

                if len(wall_hit_list) == 0 and len(star_hit_list) == 0:
                    star_placed_successfully = True

        # Add the coin to the lists
            self.coin_list.append(star)

    def on_draw(self):
        arcade.start_render()

        # Select the scrolled camera for our sprites
        self.camera_for_sprites.use()

        # Draw the sprites
        self.wall_list.draw()
        self.robot_list.draw()
        self.star_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        self.star_list.update()
        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for star in star_hit_list:
            star.remove_from_sprite_lists()
            self.score += 1

        lower_left_corner = (self.robot_sprite.center_x - self.width / 2,
                             self.robot_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.robot_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.robot_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.robot_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.robot_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.robot_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.robot_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()