# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.locals import *
from constants import *

def main():
	pygame.init
	print("Starting asteroids!")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		screen.fill('black')
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


if __name__ == "__main__":
	main()

