import arcade
import random
import math

# --- Constants ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 7
ROBOT_SCALE = 0.5
SLIME_SCALE = 0.40
SLIME_COUNT = 40
METEOR_SCALE = 0.40
METEOR_COUNT = 40
STAR_SPEED = 40
STAR_SCALE = 1
BALL_SCALE = 0.05


class Slime(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Meteor(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 Sprites")

        # Sprite lists
        self.robot_list = None
        self.slime_list = None
        self.meteor_list = None
        self.star_list = None
        self.ball_list = None

        # robot Info
        self.robot_sprite = None
        self.score = 0

        self.ball_sprite = None

        self.gun_sound = arcade.load_sound("arcade_resources_sounds_error2.wav")
        self.good_hit_sound = arcade.sound.load_sound("arcade_resources_sounds_explosion1.wav")
        self.bad_hit_sound = arcade.sound.load_sound("arcade_resources_sounds_rockHit2.wav")

        self.time_taken = 0
        arcade.set_background_color(arcade.color.CADET_BLUE)

        self.set_mouse_visible(False)

    def setup(self):

        # Sprite Lists
        self.robot_list = arcade.SpriteList()
        self.slime_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up Robot
        # Character image from api.arcade.academy in Python Arcade Library Resources
        self.robot_sprite = arcade.Sprite("robot_jump.png", ROBOT_SCALE, flipped_horizontally=True)
        self.robot_sprite.center_x = 50
        self.robot_sprite.center_y = 50
        self.robot_list.append(self.robot_sprite)

        # BAll image from clipart-library.com in Clipart Library
        self.ball_sprite = arcade.Sprite("pool_cue_ball.png", BALL_SCALE)
        self.ball_sprite.center_x = 60
        self.ball_sprite.center_y = 60
        self.ball_list.append(self.ball_sprite)

        # Create the Slime
        for i in range(SLIME_COUNT):

            # slime image from api.arcade.academy in Python Arcade Library Resources
            slime = Slime("slimePurple.png", SLIME_SCALE)

            slime.center_x = random.randrange(SCREEN_WIDTH)
            slime.center_y = random.randrange(120, SCREEN_HEIGHT)
            slime.change_x = random.randrange(-3, 4)
            slime.change_y = random.randrange(-3, 4)

            self.slime_list.append(slime)

        for i in range(METEOR_COUNT):

            # Meteor image from api.arcade.academy in Python Arcade Library Resources
            meteor = Meteor("meteorGrey_big4.png", METEOR_SCALE)

            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(120, SCREEN_HEIGHT)
            meteor.change_x = random. randrange(-3, 4)
            meteor.change_y = random. randrange(-3, 4)

            self.meteor_list.append(meteor)

    def on_draw(self):

        arcade.start_render()
        self.robot_list.draw()
        self.ball_list.draw()
        self.slime_list.draw()
        self.meteor_list.draw()
        self.star_list.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 30)

        if len(self.slime_list) == 0:
            arcade.draw_text("Game Over",
                             SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT / 2,
                             arcade.color.WHITE, 80,
                             anchor_x="center")

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.slime_list) != 0:
            self.ball_sprite.center_x = x
            self.ball_sprite.center_y = y
        else:
            self.set_mouse_visible(True)

    def on_mouse_press(self, x, y, button, modifiers):
        if len(self.meteor_list) != 0:
            # Star image from api.arcade.academy in Python Arcade Library Resources
            star = arcade.Sprite("star.png", STAR_SCALE)

            start_x = self.robot_sprite.center_x
            start_y = self.robot_sprite.center_y + 30
            star.center_x = start_x
            star.center_y = start_y

            destination_x = x
            destination_y = y

            x_diff = destination_x - start_x
            y_diff = destination_y - start_y
            angle = math.atan2(y_diff, x_diff)

            star.change_x = math.cos(angle) * STAR_SPEED
            star.change_y = math.sin(angle) * STAR_SPEED

            self.star_list.append(star)
            arcade.play_sound(self.gun_sound)

    def update(self, delta_time):
        if len(self.slime_list) != 0:
            self.slime_list.update()
            self.meteor_list.update()
            self.star_list.update()
            self.robot_sprite.update()

            good_hit_list = arcade.check_for_collision_with_list(self.robot_sprite, self.slime_list)
            bad_hit_list = arcade.check_for_collision_with_list(self.robot_sprite, self.meteor_list)

            for slime in good_hit_list:
                slime.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.good_hit_sound)

            for meteor in bad_hit_list:
                meteor.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.bad_hit_sound)

            for star in self.star_list:

                good_hit_list = arcade.check_for_collision_with_list(star, self.slime_list)
                bad_hit_list = arcade.check_for_collision_with_list(star, self.meteor_list)

                if len(good_hit_list) > 0:
                    star.remove_from_sprite_lists()
                for slime in good_hit_list:
                    slime.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.good_hit_sound)

                if len(bad_hit_list) > 0:
                    star.remove_from_sprite_lists()
                for meteor in bad_hit_list:
                    meteor.remove_from_sprite_lists()
                    self.score -= 1
                    arcade.play_sound(self.bad_hit_sound)

                if star.bottom > self.width or\
                        star.top < 0 or\
                        star.right < 0 or\
                        star.left > self.width:
                    star.remove_from_sprite_lists()

            if self.robot_sprite.top > SCREEN_HEIGHT:
                self.robot_sprite.top = SCREEN_HEIGHT
            if self.robot_sprite.left < 0:
                self.robot_sprite.left = 0
            if self.robot_sprite.bottom < 0:
                self.robot_sprite.bottom = 0
            if self.robot_sprite.right > SCREEN_WIDTH:
                self.robot_sprite.right = SCREEN_WIDTH

    def on_key_press(self, key, modifiers):

        if key == arcade.key.A:
            self.robot_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.robot_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.robot_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.robot_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.robot_sprite.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.robot_sprite.change_y = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()