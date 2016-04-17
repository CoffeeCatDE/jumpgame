import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	s = pygame.display.set_mode((600, 600))
	pygame.display.set_caption('Jump')
	clock = pygame.time.Clock()

	x = 300
	y = 580
	move_left = False
	move_right = False
	jump = False
	jump_down = False
	img = pygame.Surface((20, 20))
	img.fill((255, 0, 0))

	while True:
		clock.tick(10)
		for e in pygame.event.get():
			if e.type == QUIT:
				sys.exit(0)
			elif e.type == KEYDOWN:
				if e.key == K_UP: jump = True
				elif e.key == K_LEFT: move_left = True
				elif e.key == K_RIGHT: move_right = True
			elif e.type == KEYUP:
				if e.key == K_UP: jump = False
				elif e.key == K_LEFT: move_left = False
				elif e.key == K_RIGHT: move_right = False

		if move_left: x -= 10
		if move_right: x += 10
		if jump_down and y < 580:
			y += 10
		elif jump_down:
			y = 580
			jump_down = False
		elif 500 < y < 580:
			y -= 10
		elif y <= 500:
			y = 500
			jump_down = True
		elif jump:
			y -= 10

		s.fill((255, 255, 255))	
		s.blit(img, (x, y))
		pygame.display.update()
	

if __name__ == '__main__':
	main() 
