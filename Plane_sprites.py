import random
import pygame

# 游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0,0,480,852)

#敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

#子弹的常量
#HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
	'''游戏精灵的基类'''


	def __init__(self,image_name,speed = 1):
		
		# 调用父类的方法
		super().__init__()
		
		# 加载图像 pygame.image.load() 加载图像
		self.image = pygame.image.load(image_name)

		# 设置尺寸 self.image.get_rect() 返回图片的宽和高
		self.rect = self.image.get_rect()

		# 记录一下速度
		self.speed = speed

	def update(self):
		
		# 默认在垂直方向移动
		self.rect.y += self.speed

class Backgroup(GameSprite):
	'''背景精灵组'''

	def update(self):
		# 调用父类的方法
		super().update()
		
		# 判断是否移出屏幕 如果移出屏幕 将图片移动到上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
		

class Enemy(GameSprite):
	'''敌机精灵类'''
	def __init__(self):
		
		# 调用父类的方法,创建敌机精灵,并且指定敌机的图像
		super().__init__('/mnt/enemy0.png')

		# 设置敌机的随机初始速度
		self.speed = random.randint(1,3)
		
		
		# 设置敌机的随机初始位置
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)



	def update(self):
		
		# 调用父类的方法 让敌机在垂直方向运动
		super().update()

		# 判断是否飞出屏幕 如果是 需要敌机从精灵组删除
		if self.rect.y >= SCREEN_RECT.height:
			
			self.kill()
		def __del__(self):
			print('敌机挂掉了%s'%self.rect)





class Hero(GameSprite):
	'''英雄的精灵'''
	def __init__(self):
		super().__init__('/mnt/hero1.png',2)
	
		# 给英雄设置一个初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 100

		# 创建一个子弹精灵组
		self.bullets = pygame.sprite.Group()
		
	
	def update(self):
				
		self.rect.x += self.speed
		# 使飞机不飞出屏幕
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right


		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height


	def fire(self):
		print('发射子弹')
		
		for i in (1,1,1):
			# 创建子弹
			bullet = Bullet()
			# 设置子弹的位置
			bullet.rect.bottom = self.rect.y - 20*i
			bullet.rect.centerx = self.rect.centerx
			# 将子弹添加到精灵组
			self.bullets.add(bullet)



class Bullet(GameSprite):
	def __init__(self):
		super().__init__('/mnt/bullet.png',-1 )
		
	def update(self):
		
		super().update()

		if self.rect.bottom < 0:
			self.kill()
			









	
