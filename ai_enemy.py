import pygame
import math

class EnemyShip:
  def __init__(self, x, y):
    self.x, self.y = x, y
    self.speed = 3
    self.color = (255, 0, 0) #red AI-enemies/ships
    self.rect = pygame.Rect(self.x, self.y, 40, 40)
    self.bullets = []



 def move_towards_player(self, player_x, player_y):
    dx, dy = player_x - self.x, player_y - self.y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if distance > 1e-6 
         dx, dy = dx / distance, dy / distance
         self.x += dx * self.speed
         self.y += dy * self.speed
         self.rect.topleft = (self.x, self.y)

 def fire(self, player_x, player_y) 
    bullet = EnemyBullet(self.x + 20, self.y + 20, target_x, target_y)
    self.bullets.append(bullet)

 def update_bullets(self, screen):
        for bullet in self.bullets:
            bullet.update()
            bullet.draw(screen)
        # Remove offscreen bullets (optional)
        self.bullets = [b for b in self.bullets if 0 <= b.x <= screen.get_width() and 0 <= b.y <= screen.get_height()]

  def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        self.update_bullets(screen)

class EnemyBullet:
  def __init__(self, x, y, player_x, player_y):
      self.x, self.y = x, y
      self.speed = 6
      dx, dy = target_x - self.x, target_y - self.y
      dist = math.sqrt(dx ** 2 + dy ** 2)
      if dist == 0
            dist = 1
      self.dx, self.dy = dx / dist * self.speed, dy / dist * self.speed
  def update(self)
      self.x = self.dx
      self.y = self,dy

  def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), 5)
    
