"""
Constants used throughout the Asteroids game.

This file defines screen dimensions, asteroid properties, player properties, and other game settings.
"""

SCREEN_WIDTH = 1280
"""int: Width of the game screen in pixels."""

SCREEN_HEIGHT = 720
"""int: Height of the game screen in pixels."""

ASTEROID_MIN_RADIUS = 20
"""int: Minimum radius of an asteroid."""

ASTEROID_KINDS = 3
"""int: Number of asteroid size types."""

ASTEROID_SPAWN_RATE = 0.8  # seconds
"""float: Time interval (in seconds) between asteroid spawns."""

ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
"""int: Maximum radius of an asteroid."""

PLAYER_RADIUS = 20
"""int: Radius of the player ship."""

PLAYER_TURN_SPEED = 300
"""int: Player ship turn speed in degrees per second."""

PLAYER_SPEED = 200
"""int: Player ship movement speed in pixels per second."""

PLAYER_SHOOT_SPEED = 500
"""int: Speed of the player's shots in pixels per second."""

PLAYER_SHOOT_RATE = 0.3   # seconds
"""float: Time interval (in seconds) between player shots."""

SHOT_RADIUS = 5
"""int: Radius of a shot."""

PLAYER_SHIELD_RADIUS = #?
"""int: Radius of the player's shield. (Value to be set)"""

PLAYER_SHEILD_TIME = 
"""float: Duration of the player's shield in seconds. (Value to be set)"""