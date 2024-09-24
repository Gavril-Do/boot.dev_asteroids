# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.locals import *
from constants import *

def main():
	pygame.init
	print("Starting asteroids!")
	clock = pygame.time.Clock()
	d_time = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		screen.fill('black')
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		d_time = clock.tick(60) / 1000


if __name__ == "__main__":
	main()

