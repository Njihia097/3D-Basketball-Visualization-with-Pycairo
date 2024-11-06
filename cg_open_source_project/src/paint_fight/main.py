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
OBSTACLE_SPEED = 0.2
OBSTACLE_START_TIME = 5
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
pygame.display.set_caption("Color Capture Game")

# Game timer
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
font = pygame.font.Font(None, 36)


# Gradient Background Colors
grad_start_color = [30, 30, 60]
grad_end_color = [0, 0, 0]
color_shift = 0

def draw_gradient_background():
    global color_shift
    color_shift = (color_shift + 1) % 255
    grad_start_color[1] = (grad_start_color[1] + 1) % 255  # Cycle green component

    for y in range(HEIGHT):
        r = grad_start_color[0] + (grad_end_color[0] - grad_start_color[0]) * y // HEIGHT
        g = grad_start_color[1] + (grad_end_color[1] - grad_start_color[1]) * y // HEIGHT
        b = grad_start_color[2] + (grad_end_color[2] - grad_start_color[2]) * y // HEIGHT
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))


# Player movement cooldowns
player1_move_cooldown = PLAYER_MOVE_DELAY
player2_move_cooldown = PLAYER_MOVE_DELAY
player1_delay_timer = 0  # Timer for collision delay
player2_delay_timer = 0

player1_in_delay = False
player2_in_delay = False

def draw_player_delay_effect(screen, player_pos, player_color, delay_timer):
    # Pulse effect with a growing and shrinking radius
    pulse_radius = BOX_SIZE // 2 + int(math.sin(pygame.time.get_ticks() / 50) * 10)
    pulse_color = (
        min(255, player_color[0] + 100),  # Brightened color
        min(255, player_color[1] + 100),
        min(255, player_color[2] + 100)
    )
    # Draw pulse circle around player position
    pygame.draw.circle(
        screen, pulse_color,
        (player_pos[0] * BOX_SIZE + BOX_SIZE // 2, player_pos[1] * BOX_SIZE + BOX_SIZE // 2),
        pulse_radius, width=4
    )

# Game loop
running = True
game_over = False

while running:
    screen.fill(BACKGROUND_COLOR)
    draw_gradient_background()
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_time = max(0, GAME_TIME - seconds)

    # Check for game over
    if remaining_time == 0 and not game_over:
        game_over = True
        if player1_score > player2_score:
            winner_message = font.render("Red Wins!!", True, TEXT_COLOR)
        elif player2_score > player1_score:
            winner_message = font.render("Blue Wins!!", True, TEXT_COLOR)
        else:
            winner_message = font.render("Draw!", True, TEXT_COLOR)

        # Score message
        score_message = font.render(f"Red: {player1_score}  |  Blue: {player2_score}", True, TEXT_COLOR)

        restart_message = font.render("Game Over! Press R to Restart", True, TEXT_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Handle restarting the game
    if game_over:
        # Display winner message centered
        screen.blit(winner_message,
                    (WIDTH // 2 - winner_message.get_width() // 2, HEIGHT // 3 - winner_message.get_height() // 2))

        # Display score message centered below the winner message
        screen.blit(score_message,
                    (WIDTH // 2 - score_message.get_width() // 2, HEIGHT // 2 - score_message.get_height() // 2))

        # Display restart message at the bottom
        screen.blit(restart_message, (WIDTH // 2 - restart_message.get_width() // 2, HEIGHT - 100))
        if keys[pygame.K_r]:
            player1_score = 0
            player2_score = 0
            player1_pos = [1, 1]
            player2_pos = [COLS - 2, ROWS - 6]
            obstacle_pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
            obstacle_active = False
            start_ticks = pygame.time.get_ticks()
            game_over = False
            grid = [[EMPTY_COLOR for _ in range(COLS)] for _ in range(ROWS)]
            # Reset delay timers to zero
            player1_delay_timer = 0
            player2_delay_timer = 0
    else:
        # Activate the obstacle
        if seconds >= OBSTACLE_START_TIME:
            obstacle_active = True

        # Decrease delay timers if they are active
        if player1_in_delay:
            player1_delay_timer -= 1
            if player1_delay_timer <= 0:
                player1_in_delay = False  # Exit delay mode for player 1
        if player2_in_delay:
            player2_delay_timer -= 1
            if player2_delay_timer <= 0:
                player2_in_delay = False

        # Move players only if they are not in delay
        if not player1_in_delay:
            if player1_move_cooldown == 0:
                player1_move_cooldown = PLAYER_MOVE_DELAY
                if keys[player1_keys['up']] and player1_pos[1] > 0:
                    player1_pos[1] -= 1
                if keys[player1_keys['down']] and player1_pos[1] < ROWS - 1:
                    player1_pos[1] += 1
                if keys[player1_keys['left']] and player1_pos[0] > 0:
                    player1_pos[0] -= 1
                if keys[player1_keys['right']] and player1_pos[0] < COLS - 1:
                    player1_pos[0] += 1
            else:
                player1_move_cooldown -= 1

        if not player2_in_delay:
            if player2_move_cooldown == 0:
                player2_move_cooldown = PLAYER_MOVE_DELAY
                if keys[player2_keys['up']] and player2_pos[1] > 0:
                    player2_pos[1] -= 1
                if keys[player2_keys['down']] and player2_pos[1] < ROWS - 1:
                    player2_pos[1] += 1
                if keys[player2_keys['left']] and player2_pos[0] > 0:
                    player2_pos[0] -= 1
                if keys[player2_keys['right']] and player2_pos[0] < COLS - 1:
                    player2_pos[0] += 1
            else:
                player2_move_cooldown -= 1

        # Check for collisions with obstacle and set delay
        if obstacle_active:
            if [int(obstacle_pos[0]), int(obstacle_pos[1])] == player1_pos:
                player1_delay_timer = 5 * FPS  # 3 seconds delay
                player1_in_delay = True  # Set player1 in delay mode
            if [int(obstacle_pos[0]), int(obstacle_pos[1])] == player2_pos:
                player2_delay_timer = 5 * FPS  # 3 seconds delay
                player2_in_delay = True  # Set player2 in delay mode



        # Update grid colors and scores with takeover logic
        if grid[player1_pos[1]][player1_pos[0]] != PLAYER1_COLOR:
            # If player1 is taking over player2's color
            if grid[player1_pos[1]][player1_pos[0]] == PLAYER2_COLOR:
                player2_score -= 1  # Deduct from player2's score
            grid[player1_pos[1]][player1_pos[0]] = PLAYER1_COLOR  # Color the cell for player1
            player1_score += 1  # Add to player1's score

        if grid[player2_pos[1]][player2_pos[0]] != PLAYER2_COLOR:
            # If player2 is taking over player1's color
            if grid[player2_pos[1]][player2_pos[0]] == PLAYER1_COLOR:
                player1_score -= 1  # Deduct from player1's score
            grid[player2_pos[1]][player2_pos[0]] = PLAYER2_COLOR  # Color the cell for player2
            player2_score += 1  # Add to player2's score

        # Move obstacle if active
        if obstacle_active:
            obstacle_pos[0] += obstacle_velocity[0]
            obstacle_pos[1] += obstacle_velocity[1]
            if obstacle_pos[0] <= 0 or obstacle_pos[0] >= COLS - 1:
                obstacle_velocity[0] *= -1
            if obstacle_pos[1] <= 0 or obstacle_pos[1] >= ROWS - 1:
                obstacle_velocity[1] *= -1

        # Draw elements
        for row in range(ROWS):
            for col in range(COLS):
                color = grid[row][col]
                pygame.draw.rect(screen, color, (col * BOX_SIZE, row * BOX_SIZE, BOX_SIZE, BOX_SIZE))
                pygame.draw.rect(screen, BACKGROUND_COLOR, (col * BOX_SIZE, row * BOX_SIZE, BOX_SIZE,
                                                            BOX_SIZE), 1)

        # Draw glowing player heads
        pygame.draw.circle(screen, (255, 150, 150), (player1_pos[0] * BOX_SIZE + BOX_SIZE // 2,
                                                     player1_pos[1] * BOX_SIZE + BOX_SIZE // 2), BOX_SIZE // 2)
        pygame.draw.circle(screen, (150, 150, 255), (player2_pos[0] * BOX_SIZE + BOX_SIZE // 2,
                                                     player2_pos[1] * BOX_SIZE + BOX_SIZE // 2), BOX_SIZE // 2)

        # Player delay effect for Player 1
        if player1_in_delay:
            draw_player_delay_effect(screen, player1_pos, PLAYER1_COLOR, player1_delay_timer)

        # Player delay effect for Player 2
        if player2_in_delay:
            draw_player_delay_effect(screen, player2_pos, PLAYER2_COLOR, player2_delay_timer)

        # Draw intimidating pulsing obstacle
        if obstacle_active:
            # Update obstacle position
            obstacle_pos[0] += obstacle_velocity[0]
            obstacle_pos[1] += obstacle_velocity[1]

            # Reverse and slightly adjust direction upon reaching boundaries
            if obstacle_pos[0] >= COLS - 1 or obstacle_pos[0] <= 0:
                obstacle_velocity[0] *= -1
                obstacle_velocity[0] += random.uniform(-0.1, 0.1)  # Small random angle change
            if obstacle_pos[1] >= ROWS - 1 or obstacle_pos[1] <= 0:
                obstacle_velocity[1] *= -1
                obstacle_velocity[1] += random.uniform(-0.1, 0.1)  # Small random angle change

            # Normalize velocity to keep speed consistent
            velocity_magnitude = math.hypot(obstacle_velocity[0], obstacle_velocity[1])
            obstacle_velocity[0] = (obstacle_velocity[0] / velocity_magnitude) * OBSTACLE_SPEED
            obstacle_velocity[1] = (obstacle_velocity[1] / velocity_magnitude) * OBSTACLE_SPEED

            # Make obstacle pulse with a larger range
            obstacle_radius = BOX_SIZE // 2 + int(math.sin(pygame.time.get_ticks() / 150) * 6)

            # Make the color pulse between bright yellow and a darker yellow-orange
            pulse_intensity = abs(math.sin(pygame.time.get_ticks() / 300)) * 255
            obstacle_color = (255, int(200 - pulse_intensity // 2), 0)  # Shifting towards an orange hue

            # Draw the main obstacle circle
            pygame.draw.circle(screen, obstacle_color,
                               (int(obstacle_pos[0] * BOX_SIZE + BOX_SIZE // 2),
                                int(obstacle_pos[1] * BOX_SIZE + BOX_SIZE // 2)),
                               obstacle_radius)

            # Draw an outer glow effect
            pygame.draw.circle(screen, (255, 150, 0),
                               (int(obstacle_pos[0] * BOX_SIZE + BOX_SIZE // 2),
                                int(obstacle_pos[1] * BOX_SIZE + BOX_SIZE // 2)),
                               obstacle_radius + 8, width=2)

        # Define scoreboard dimensions
        scoreboard_width = 160
        scoreboard_height = 42
        scoreboard_x = (WIDTH - scoreboard_width) // 2
        scoreboard_y = 0

        # Draw the scoreboard background as a rectangle with a white fill
        pygame.draw.rect(screen, SCOREBOARD_COLOR, (scoreboard_x, scoreboard_y, scoreboard_width,
                                                    scoreboard_height))

        # Draw score within the semicircle
        score_text1 = font.render(f"{player1_score}", True, PLAYER1_COLOR)
        score_text2 = font.render(f"{player2_score}", True, PLAYER2_COLOR)
        score_x = WIDTH // 2 - (score_text1.get_width() + score_text2.get_width() + 20) // 2
        score_y = scoreboard_height // 2 - score_text1.get_height() // 2  # Center vertically within the semicircle

        # Blit scores to screen within the semicircle
        screen.blit(score_text1, (score_x, score_y))
        screen.blit(score_text2, (score_x + score_text1.get_width() + 20, score_y))

        # Timer font and transparency setup
        timer_font = pygame.font.Font(None, 140)  # Large font for visibility
        timer_surface = timer_font.render(f"{remaining_time}", True, (128, 128, 128))  # Grayscale color
        timer_surface.set_alpha(200)  # Semi-transparent

        # Center timer on the playground
        timer_x = WIDTH // 2 - timer_surface.get_width() // 2
        timer_y = HEIGHT // 2 - timer_surface.get_height() // 2
        screen.blit(timer_surface, (timer_x, timer_y))

    pygame.display.flip()
    clock.tick(FPS)
