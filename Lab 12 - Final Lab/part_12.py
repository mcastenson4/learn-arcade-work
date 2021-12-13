## Final Lab - Block Builder
## Morgan Castenson
## 12/13/21

import arcade

######################### VARIABLES ###################################################
ROW_COUNT = 10
COLUMN_COUNT = 10
MOVEMENT_SPEED = 25

WIDTH = 20
HEIGHT = 20
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

######################### ENEMY KILLERS ###################################################
class LevelOneHorizontalKiller:
    def __init__(self, position_x, position_y, radius, color):
        self.change_x = 1
        self.change_y = 0
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        x = self.position_x
        y = self.position_y
        arcade.draw_rectangle_filled(x, y, 20, 20, self.color, 0)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            self.change_x = 1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            self.change_x = -1

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class LevelTwoFastHorizontalKiller:
    def __init__(self, position_x, position_y, radius, color):
        self.change_x = 5
        self.change_y = 0
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        x = self.position_x
        y = self.position_y
        arcade.draw_rectangle_filled(x, y, 20, 20, self.color, 0)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            self.change_x = 5

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            self.change_x = -5

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class LevelTwoFastVerticalKiller:
    def __init__(self, position_x, position_y, radius, color):
        self.change_x = 0
        self.change_y = 5
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        x = self.position_x
        y = self.position_y
        arcade.draw_rectangle_filled(x, y, 20, 20, self.color, 0)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius
            self.change_y = 5

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            self.change_y = -5

######################### PLAYER ###################################################
class Player:
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
        arcade.draw_rectangle_filled(x, y, 20, 20, self.color, 0)

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

######################### LEVEL ONE ###################################################
class LevelOne(arcade.View):
    def __init__(self, width, height, title):
        super().__init__()
        self.grid = []
        self.total = 0
        self.player = Player(15, 15, 15, arcade.color.RED)
        self.killer = LevelOneHorizontalKiller(15, 215, 15, arcade.color.AIR_FORCE_BLUE)
        self.killer2 = LevelOneHorizontalKiller(15, 115, 15, arcade.color.AIR_FORCE_BLUE)
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.WHITE
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
        self.player.draw()
        self.killer.draw()
        self.killer2.draw()

    def update(self, delta_time):
        self.player.update()
        self.killer.update()
        self.killer2.update()

        if self.player.position_x == self.killer.position_x and self.player.position_y == self.killer.position_y\
                or self.player.position_x == self.killer2.position_x and self.player.position_y == self.killer2.position_y:
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    self.grid[row][column] = 0
            over_view = GameOverView(self.total)
            self.window.show_view(over_view)

        if self.player.change_x != 0:
            self.player.change_x = 0
        if self.player.change_y != 0:
            self.player.change_y = 0

    def on_key_press(self, key, modifiers):
        column = self.player.position_x // (WIDTH + MARGIN)
        row = self.player.position_y // (HEIGHT + MARGIN)

        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
        elif key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1

        self.total = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    self.total = self.total + 1

        if self.total == 100:
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    self.grid[row][column] = 0
            level_two_instructions = LevelTwoInstructionView()
            self.window.show_view(level_two_instructions)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

######################### LEVEL TWO ###################################################
class LevelTwo(arcade.View):
    def __init__(self, width, height, title):
        super().__init__()
        self.grid = []
        self.total = 100
        self.player = Player(15, 15, 15, arcade.color.GREEN)
        self.killer = LevelTwoFastHorizontalKiller(15, 215, 15, arcade.color.PURPLE)
        self.killer2 = LevelTwoFastHorizontalKiller(15, 115, 15, arcade.color.PURPLE)
        self.killer3 = LevelTwoFastVerticalKiller(115, 15, 15, arcade.color.PURPLE)
        self.killer4 = LevelTwoFastVerticalKiller(215, 15, 15, arcade.color.PURPLE)
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.WHITE
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
        self.player.draw()
        self.killer.draw()
        self.killer2.draw()
        self.killer3.draw()
        self.killer4.draw()

    def update(self, delta_time):
        self.player.update()
        self.killer.update()
        self.killer2.update()
        self.killer3.update()
        self.killer4.update()

        if self.player.position_x == self.killer.position_x and self.player.position_y == self.killer.position_y\
                or self.player.position_x == self.killer2.position_x and self.player.position_y == self.killer2.position_y\
                or self.player.position_x == self.killer3.position_x and self.player.position_y == self.killer3.position_y\
                or self.player.position_x == self.killer4.position_x and self.player.position_y == self.killer4.position_y:
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    self.grid[row][column] = 0
            over_view = GameOverView(self.total)
            self.window.show_view(over_view)

        if self.player.change_x != 0:
            self.player.change_x = 0
        if self.player.change_y != 0:
            self.player.change_y = 0

    def on_key_press(self, key, modifiers):
        column = self.player.position_x // (WIDTH + MARGIN)
        row = self.player.position_y // (HEIGHT + MARGIN)

        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
        elif key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1

        self.total = 100
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    self.total = self.total + 1

        if self.total == 200:
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    self.grid[row][column] = 0
            over_view = GameOverView(200)
            self.window.show_view(over_view)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

######################### INSTRUCTIONS ###################################################
class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.YELLOW)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to Block Builder", self.window.width / 2, self.window.height / 2 + 75,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("By Morgan Castenson", self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("Click Mouse to Start Level 1", self.window.width / 2, self.window.height / 2 + 25,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("Use arrow keys to move red player.", self.window.width / 2, self.window.height / 2 - 25,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("Watch out for blue killers!", self.window.width / 2, self.window.height / 2 - 50,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("Fill the board to advance to Level 2!", self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.BLACK, font_size=10, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        level_one = LevelOne(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Lab")
        level_one.__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Lab")
        self.window.show_view(level_one)

######################### LEVEL TWO INSTRUCTIONS ###################################################
class LevelTwoInstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.YELLOW)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You made it to Level 2", self.window.width / 2, self.window.height / 2 + 25,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("Current Score = 100", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("Click Mouse to Start!", self.window.width / 2, self.window.height / 2 - 25,
                         arcade.color.BLACK, font_size=10, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        level_two = LevelTwo(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Lab")
        level_two.__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Lab")
        self.window.show_view(level_two)

######################### GAME OVER ###################################################
class GameOverView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.score = str(score)

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.YELLOW)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", self.window.width / 2, self.window.height / 2 + 75,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("Score = " + self.score, self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.BLACK, font_size=10, anchor_x="center")
        arcade.draw_text("Click Mouse to Restart", self.window.width / 2, self.window.height / 2 + 25,
                         arcade.color.BLACK, font_size=10, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        start_view = InstructionView()
        self.window.show_view(start_view)

######################### MAIN ###################################################
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Lab")
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

main()
