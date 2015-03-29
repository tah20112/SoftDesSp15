""" Exploring Turtle World """

from swampy.TurtleWorld import *

def draw_line(turtle, angle, start_x, start_y, line_length):
	""" Draws a line with the specified turtle.

		turtle: this is the turtle that will do the drawing
		angle: the angle in degrees where 0 degrees is East
		start_x: the starting x-coordinate for the line
		start_y: the starting y-coordinate for the line
		line_length: the length of the line that should be drawn """
	# first move to the appropriate starting location
	turtle.x = start_x
	turtle.y = start_y

	# turn the to the appropriate angle
	turtle.lt(angle)

	# put the pen down, and walk forward the appropriate number of steps
	turtle.fd(line_length)

# create the Turtle world object
world = TurtleWorld();
beth = Turtle();
beth.set_color('green')
beth.set_pen_color('red')
beth.delay = .01
draw_line(beth, 45, -100, -100, 200)


wait_for_user()