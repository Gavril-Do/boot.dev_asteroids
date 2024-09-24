# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	player1 = player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	d_time = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill('black')
		player1.draw(screen)
		pygame.display.flip()

		# limit to 60 FPS
		d_time = clock.tick(60) / 1000


if __name__ == "__main__":
	main()

