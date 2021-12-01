"""
Array Backed Grid

Show how to use a two-dimensional list/array to back the display of a
grid on-screen.
"""
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # Counting variables
        total = 0
        rowTotal = 0
        columnTotal = 0
        continuous_count = 0

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            ## test corners
            ## top left corner
            if row == 0 and column == 0:
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    self.grid[row][column + 1] = 1
                    self.grid[row + 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column + 1] = 0
                    self.grid[row + 1][column] = 0
            ## top right corner
            elif row == 0 and column == COLUMN_COUNT - 1:
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    self.grid[row][column - 1] = 1
                    self.grid[row + 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column - 1] = 0
                    self.grid[row + 1][column] = 0
            ## bottom left corner
            elif row == ROW_COUNT - 1 and column == 0:
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    self.grid[row][column + 1] = 1
                    self.grid[row - 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column + 1] = 0
                    self.grid[row - 1][column] = 0
            ## bottom right corner
            elif row == ROW_COUNT - 1 and column == COLUMN_COUNT - 1:
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    self.grid[row][column - 1] = 1
                    self.grid[row - 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column - 1] = 0
                    self.grid[row - 1][column] = 0
            ## test sides
            # top side
            elif row == 0:
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    self.grid[row][column + 1] = 1
                    self.grid[row][column - 1] = 1
                    self.grid[row + 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column + 1] = 0
                    self.grid[row][column - 1] = 0
                    self.grid[row + 1][column] = 0
            # bottom side
            elif row == ROW_COUNT - 1:
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    self.grid[row][column + 1] = 1
                    self.grid[row][column - 1] = 1
                    self.grid[row - 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column + 1] = 0
                    self.grid[row][column - 1] = 0
                    self.grid[row - 1][column] = 0
            # left side
            elif column == 0:
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    self.grid[row][column + 1] = 1
                    self.grid[row + 1][column] = 1
                    self.grid[row - 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column + 1] = 0
                    self.grid[row + 1][column] = 0
                    self.grid[row - 1][column] = 0
            # right side
            elif column == COLUMN_COUNT - 1:
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    self.grid[row][column - 1] = 1
                    self.grid[row + 1][column] = 1
                    self.grid[row - 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column - 1] = 0
                    self.grid[row + 1][column] = 0
                    self.grid[row - 1][column] = 0
            # anywhere in the middle
            else:
                # Flip the location between 1 and 0.
                if self.grid[row][column] == 0:
                    self.grid[row][column] = 1
                    #left
                    self.grid[row][column - 1] = 1
                    #right
                    self.grid[row][column + 1] = 1
                    #down
                    self.grid[row + 1][column] = 1
                    #up
                    self.grid[row - 1][column] = 1
                else:
                    self.grid[row][column] = 0
                    self.grid[row][column - 1] = 0
                    self.grid[row][column + 1] = 0
                    self.grid[row + 1][column] = 0
                    self.grid[row - 1][column] = 0

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    total = total + 1
        print(f"Total of {total} cells are selected")

        for row in range(ROW_COUNT):
            rowTotal = 0
            continuous_count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    rowTotal = rowTotal + 1
                    continuous_count = continuous_count + 1
                else:
                    if continuous_count > 2:
                        print(f"There are {continuous_count} continuous blocks selected on row {row}")
                        continuous_count = 0
                    else:
                        continuous_count = 0
            if continuous_count > 2:
                print(f"There are {continuous_count} continuous blocks selected on row {row}")
            print(f"Row {row} has {rowTotal} cells selected")

        for column in range(COLUMN_COUNT):
            columnTotal = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    columnTotal = columnTotal + 1
            print(f"Column {column} has {columnTotal} cells selected")

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
