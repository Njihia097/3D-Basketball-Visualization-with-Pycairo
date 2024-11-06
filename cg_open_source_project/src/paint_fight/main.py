import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 20, 20
BOX_SIZE = WIDTH // COLS
FPS = 30  # Increased FPS for smoother animation
GAME_TIME = 30  # Game duration in seconds
OBSTACLE_SPEED = 0.2  # Slowed down
OBSTACLE_START_TIME = 0  # Seconds to introduce the obstacle
PLAYER_MOVE_DELAY = 5  # Frames between player moves

# Colors
EMPTY_COLOR = (200, 200, 200)
PLAYER1_COLOR = (255, 0, 0)
PLAYER2_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (240, 235, 210)
SCOREBOARD_COLOR = (255, 255, 255)
OBSTACLE_COLOR = (255, 255, 0)
TEXT_COLOR = (255, 255, 255)

# Player settings
player1_pos = [1, 1]
player2_pos = [COLS - 2, ROWS - 6]
player1_keys = {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d}
player2_keys = {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}

# Obstacle settings
obstacle_pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
obstacle_velocity = [OBSTACLE_SPEED, OBSTACLE_SPEED]
obstacle_active = False

# Initialize grid and scores
grid = [[EMPTY_COLOR for _ in range(COLS)] for _ in range(ROWS)]
player1_score = 0
player2_score = 0

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Capture Game with Enhanced Visuals")

# Game timer
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
font = pygame.font.Font(None, 36)