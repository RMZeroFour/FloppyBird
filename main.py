import pygame as pg
from bird import Bird
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize the pygame library
pg.init()

# Create the window and set the title
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Floppy Bird")

# Clock for timing purposes
clock = pg.time.Clock()

# Create a peacock
peacock = Bird((0, 0, 255))

# Infinite loop to run the game
running = True
while running:

	# Loop through all the events like closing, mouse click, key press, etc.
	for event in pg.event.get():
		if event.type == pg.QUIT:
			# If window is closed end the loop
			running = False
		elif event.type == pg.KEYDOWN and event.key == pg.K_F4 and event.mod & pg.KMOD_ALT:
			# Else if Alt-F4 is pressed end the loop
			running = False
		else:
			# Handle all other events
			peacock.process(event)
	
	# Clear the screen with sky blue
	screen.fill((43, 206, 227))

	# Render the peacock
	peacock.draw(screen)

	# Update the window graphics (Flips the double buffer)
	pg.display.flip()

	# Limit the framerate to 60fps
	dt = clock.tick(60)

	# Update the physics of the bird
	peacock.update(dt)

pg.quit()