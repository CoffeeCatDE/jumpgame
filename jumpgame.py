import pygame, random, sys
from pygame.locals import *

game = {
	'clock': None,
	'screen': None,
	'blockimg': None,
	'blocks': []
}

player = {
	'x': 300,
	'y': 580,
	'move_left': False,
	'move_right': False,
	'jump': False,
	'jump_height': 120,
	'jump_down': False,
	'jump_up': False
}

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	return x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2

def handleinput():
	for e in pygame.event.get():
		if e.type == QUIT:
			sys.exit(0)
		elif e.type == KEYDOWN:
			if e.key == K_UP: player['jump'] = True
			elif e.key == K_LEFT: player['move_left'] = True
			elif e.key == K_RIGHT: player['move_right'] = True
		elif e.type == KEYUP:
			if e.key == K_UP: player['jump'] = False
			elif e.key == K_LEFT: player['move_left'] = False
			elif e.key == K_RIGHT: player['move_right'] = False

def moveplayer():
	if player['move_left']: player['x'] -= 10
	if player['move_right']: player['x'] += 10

	if player['x'] < 0:
		player['x'] = 600
	elif player['x'] > 600:
		player['x'] = 0

	if player['jump_down'] and player['y'] < 580:
		player['y'] += 10
	elif player['jump_up'] and player['jump_height'] > 0:
		player['y'] -= 10
		player['jump_height'] -= 10
	elif player['jump_up']:
		player['jump_up'] = False
		player['jump_down'] = True
	elif player['jump']:
		player['jump_up'] = True
		player['jump_down'] = False
		player['jump_height'] = 100

def collision():
	for block in game['blocks']:
		collides = collide(player['x'], block['x'], player['y'], block['y'], 20, 100, 20, 10)
		if player['jump_down'] and collides:
			player['y'] = block['y'] - 20
			player['jump_down'] = False
			return
	
	# if we got here we don't have any collision with blocks, so we fall down again
	if not player['jump_up']:
		player['jump_down'] = True

def win():
	if player['y'] < 20:
		font = pygame.font.SysFont('Arial', 40)
		text = font.render('You have won :)', True, (0, 0, 0))
		game['screen'].fill((255, 255, 255))
		game['screen'].blit(text, (100, 270))
		pygame.display.update()
		return True
	else:
		return False

def gameloop():
	game['clock'].tick(10)
	handleinput()
	moveplayer()
	collision()

	# draw everything
	game['screen'].fill((255, 255, 255))	
	game['screen'].blit(player['img'], (player['x'], player['y']))
	for block in game['blocks']:
		game['screen'].blit(game['blockimg'], (block['x'], block['y']))
	pygame.display.update()


def main():
	pygame.init()
	game['screen'] = pygame.display.set_mode((600, 600))
	pygame.display.set_caption('Jump')
	game['clock'] = pygame.time.Clock()

	player['img'] = pygame.Surface((20, 20))
	player['img'].fill((255, 0, 0))

	game['blockimg'] = pygame.Surface((100, 10))
	game['blockimg'].fill((128, 128, 128))

	for i in range(0, 11):
		block = {'x': random.randint(0, 600), 'y': random.randint(i * 50, i * 50 + 50)}
		game['blocks'].append(block)

	while True:
		gameloop()
		if win():
			break
	
	while True:
		handleinput()

if __name__ == '__main__':
	main()
