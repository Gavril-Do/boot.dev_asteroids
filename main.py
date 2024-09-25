# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *

def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable_group = pygame.sprite.Group()
	drawable_group = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()

	Player.containers = (updatable_group, drawable_group)
	Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
	AsteroidField.containers = (updatable_group)

	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	asteroidfield = AsteroidField()

	d_time = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill('black')

		for obj in updatable_group:
			obj.update(d_time)

		for obj in drawable_group:
			obj.draw(screen)
	#	player1.draw(screen)
	#	player1.update(d_time)
		pygame.display.flip()

		# limit to 60 FPS
		d_time = clock.tick(60) / 1000


if __name__ == "__main__":
	main()

