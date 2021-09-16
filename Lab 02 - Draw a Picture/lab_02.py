"""
Drawing lab 2
"""
import arcade

arcade.open_window(800, 600, "Christmas Tree")

arcade.set_background_color(arcade.color.BRICK_RED)

arcade.start_render()
# Snow
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.csscolor.BEIGE)

# Body of the Snowman
arcade.draw_circle_filled(400, 400, 35, arcade.csscolor.WHITE)
arcade.draw_circle_filled(400, 320, 55, arcade.csscolor.WHITE)
arcade.draw_circle_filled(400, 220, 85, arcade.csscolor.WHITE)

# Sun in the Sky
arcade.draw_circle_filled(700, 500, 55, arcade.csscolor.YELLOW)
arcade.draw_line(700, 500, 590, 550, arcade.csscolor.YELLOW, 10)
arcade.draw_line(700, 500, 700, 390, arcade.csscolor.YELLOW, 10)
arcade.draw_line(700, 500, 845, 400, arcade.csscolor.YELLOW, 10)
arcade.draw_line(700, 500, 575, 450, arcade.csscolor.YELLOW, 10)
arcade.draw_line(700, 500, 590, 6000, arcade.csscolor.YELLOW, 10)
arcade.draw_line(700, 500, 800, 550, arcade.csscolor.YELLOW, 10)

# Snowman's Hat
arcade.draw_rectangle_filled(400, 430, 100, 20, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(400, 470, 70, 70, arcade.csscolor.BLACK)

# Snowman's Eyes and Nose
arcade.draw_circle_filled(415, 410, 7, arcade.color.BLACK)
arcade.draw_circle_filled(390, 410, 7, arcade.color.BLACK)
arcade.draw_triangle_filled(350, 390, 410, 390, 410, 400, arcade.csscolor.ORANGE)

# Button's
arcade.draw_circle_filled(403, 300, 7, arcade.color.BLACK)
arcade.draw_circle_filled(403, 320, 7, arcade.color.BLACK)
arcade.draw_circle_filled(403, 340, 7, arcade.color.BLACK)

arcade.finish_render()

arcade.run()







