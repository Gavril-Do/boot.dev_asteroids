# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Player.containers = (updatable, drawable)

	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

	d_time = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for obj in updatable:
			obj.update(d_time)

		screen.fill('black')

		for obj in drawable:
			obj.draw(screen)
	#	player1.draw(screen)
	#	player1.update(d_time)
		pygame.display.flip()

		# limit to 60 FPS
		d_time = clock.tick(60) / 1000


if __name__ == "__main__":
	main()

