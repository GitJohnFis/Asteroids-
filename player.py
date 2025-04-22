 import pygame
 from constants import *
 from circleshape import CircleShape
 form shoot import Shot


 class Player(CircleShape):
    def _init_(self, x, y):
        super._init_(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.speed_boost = 1.0
        self.sheild_active = False 
        self.sheild_timer = 0
 
 def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(),2)
 
 
 def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

def update(self, dt):
        keys = pygame.key.get_pressed()
         self.shoot_timer -= dt

         if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
         self.move(-dt)
         if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
            if keys[pygame.K_SPACE]:
                self.shoot()
                
                # apply the speed boost to movements
                actual_speed = self.speed * self.speed_boost
                  
                  self.position.y += actual_speed * dt
                  self.position.x += actual_speed * dt

                  # update the sheild timer
                  if self.sheild_active:
                     self.sheild.timer -= dt
                     if self.sheild_timer <= 0:
                        self.sheild_active = False
                        self.sheild_timer = 0
                        
def shoot(self)
# now you should only be able to shoot if the timer is 0
if self.shoot_timer > 0: 
      return
      self.shoot_timer = PLAYER_SHOOT_RATE
shot - Shot(self.position.x, self.position.y)
shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED


def rotate(self, dt):
   self.rotation += dt * SELF_TURN_SPEED * dt

def move(self, dt):
   forward = pygame.Vector2(0, 1).rotate(self.rotation)
   self.potion += forward *  PLAYER_SPEED * dt

# Powerups handling methods activation and deactivation
def activate_shield(self):
      self.sheild_active = True
      self.sheild_timer = PLAYER_SHEILD_TIME # duration of the shield in seconds

def activate_speed_boost(self):
      self.sheild_boost = SPEED_BOOST_MULTI # multiplier for speed
      pygame.time.set_timer(SPEED_BOOST_END_EVENT, int(SPEED_BOOST_DURATION * 1000), 1) # set a timer for the speed boost

def deactivate_speed_boost(self):
      self.speed_boost = 1.0 #reset the normal speed