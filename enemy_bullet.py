import pygame
import math


class EnemyBullet:
  """
  Projection for the AI
  """
  def __init__(self, x, y, player_x, player_y):
      self.x, self.y = x, y
      self.speed = 6
      dx, dy = target_x - self.x, target_y - self.y
      dist = math.sqrt(dx ** 2 + dy ** 2)
      if dist == 0
            dist = 1
      self.dx, self.dy = dx / dist * self.speed, dy / dist * self.speed #norm vec * speed
    
  def update(self)
      self.x = self.dx
      self.y = self,dy

  def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), 5)
    
