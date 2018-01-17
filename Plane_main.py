# 使用pygame 先导入这个包
import pygame
from Plane_sprites import *


class PlaneGame(object):
	'''飞机大战主游戏'''
	def __init__(self):
		print('游戏初始化')


		# 创建游戏窗口   pygame.display.set_mode 创建游戏窗口 需要宽和高   size 取宽高 .x取x轴的值  .y取y轴的值
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 创建游戏时钟  pygame.time.Clock()  会返回一个时钟对象
		self.clock = pygame.time.Clock()
		# 调用私有方法 里面的创建精灵和精灵组
		self.__create_sprites()
		# 设置定时器事件 每秒创建一架敌机
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		# 射子弹
		#pygame.time.set_timer(HERO_FIRE_EVENT,500)


	def start_game(self):
		print('开始游戏')
		
		while True:
			# 设置帧率
			self.clock.tick(60)	
			# 事件监听
			self.__event_handler()
			# 碰撞检测
			self.__check_collide()
			# 更新精灵组
			self.__update_sprites()
			# 刷新屏幕
			pygame.display.update()


	def __create_sprites(self):
		'''创建精灵和精灵组'''
		# pygame.sprite.Group() 可以创建一个精灵组
		# 背景精灵组
		bg1 = Backgroup('/mnt/background.png')
		bg2 = Backgroup('/mnt/background.png')
		bg2.rect.y = -bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1,bg2)
		# 敌机精灵组 
		self.enemy_group = pygame.sprite.Group()
		# 英雄组
		self.hero = Hero()
		self.hero1 = Hero()
		self.hero_group = pygame.sprite.Group(self.hero,self.hero1)
		

	def __event_handler(self):
		'''事件监听的方法'''
		# pygame.event.get() 获取监听事件的列表
		# 获取完列表以后 我写了一个for循环 循环这个列表 
		for event in pygame.event.get():
			# 当列表里面有ptgame.QUIT这个值的时候  说明用户点了关闭按钮
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				enemy = Enemy()
				self.enemy_group.add(enemy)
			#elif event.type == HERO_FIRE_EVENT:
				#self.hero.fire()
			#elif event.type == pygame.KEYDOWN and event.key == pygame.k_RIGHT:
				#print('向右移动')

			key_pressed = pygame.key.get_pressed()			
			if key_pressed[pygame.K_RIGHT]:
				print('向右移动')
				self.hero.speed = 4

			else:
				self.hero.speed = 0

			if key_pressed[pygame.K_LEFT]:
				print('想左移动')
				self.hero.speed = -4


			
			if key_pressed[pygame.K_KP0]:
				print('发射子弹')
				self.hero.fire()

			

			if key_pressed[pygame.K_d]:
				self.hero1.speed = 5

			else:
				self.hero1.speed = 0


			if key_pressed[pygame.K_a]:
				self.hero1.speed = -5


			if key_pressed[pygame.K_SPACE]:
				self.hero1.fire()

			




	def __check_collide(self):
		'''碰撞检测'''
		# 子弹摧毁飞机
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,False,True)
		pygame.sprite.groupcollide(self.hero1.bullets,self.enemy_group,False,True)

		# 英雄撞到敌机
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,False)
		enemies = pygame.sprite.spritecollide(self.hero1,self.enemy_group,False)

		# 判断列表是否有内容
		if len(enemies) > 0:
			
			# 让英雄牺牲
			self.hero.kill

			# 结束游戏
			PlaneGame.__game_over()

	def __update_sprites(self):
		'''更新精灵组'''
		for group in [self.back_group,self.enemy_group,self.hero_group]:
			for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets,self.hero1.bullets]:
				# 更新精灵组里所有精灵的位置
				group.update()
				# 绘制到屏幕上
				group.draw(self.screen)

	@staticmethod
	def __game_over():
		'''游戏结束'''
		print('游戏结束')
		pygame.quit()
		exit()
		




if __name__ == '__main__':
	# 创建游戏对象
	game = PlaneGame()
	# 调用开始游戏的方法
	game.start_game()

