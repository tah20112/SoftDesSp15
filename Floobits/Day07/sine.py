from swampy.TurtleWorld import *
from math import pi, cos, sin, atan2

def draw_sin(turtle, start_theta, end_theta, step):
	nsteps = (end_theta)
	theta = start_theta
	while theta <= end_theta:
		slope = cos(theta*pi/180.0)
		theta += step
		slope = atan2(slope, 1)

		turtle.heading = slope * 180.0/pi
		turtle.fd((1+slope**2)**0.5)

world = TurtleWorld()
beth = Turtle()
beth.set_pen_color('red')
beth.delay = .01
draw_sin(beth, 0, 760*4, 5)
wait_for_user()