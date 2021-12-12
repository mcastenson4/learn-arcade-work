## Final Lab - Tetris Exploration
import arcade

ROW_COUNT = 10
COLUMN_COUNT = 10
MOVEMENT_SPEED = 25

WIDTH = 20
HEIGHT = 20
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

class Killer:
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
        arcade.draw_rectangle_filled(x, y, 20, 20, arcade.color.AIR_FORCE_BLUE, 0)

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
        arcade.draw_rectangle_filled(x, y, 20, 20, arcade.color.RED, 0)

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

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height)
        self.grid = []
        self.player = Player(15, 15, 15, arcade.color.RED)
        self.killer = Killer(15, 215, 15, arcade.color.AIR_FORCE_BLUE)
        self.killer2 = Killer(15, 115, 15, arcade.color.AIR_FORCE_BLUE)
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

        if self.player.position_x == self.killer.position_x and self.player.position_y == self.killer.position_y or self.player.position_x == self.killer2.position_x and self.player.position_y == self.killer2.position_y:
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    self.grid[row][column] = 0

        if self.player.change_x != 0:
            self.player.change_x = 0
        if self.player.change_y != 0:
            self.player.change_y = 0


    def on_key_press(self, key, modifiers):
        total = 0
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

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    total = total + 1
        if total == 100:
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    self.grid[row][column] = 0

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0

def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Lab")
    arcade.run()

main()
