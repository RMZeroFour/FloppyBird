import pygame as pg

# Initialize the pygame library
pg.init()

# Create the window and set the title
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Floppy Bird")

# Clock for timing purposes
clock = pg.time.Clock()

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
		elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
			print("123")
	
	# Clear the screen with black
	screen.fill((0, 0, 0))
	
	# Update the window graphics (Flips the double buffer)
	pg.display.flip()

	# Limit the framerate to 60fps
	clock.tick(60)

pg.quit()