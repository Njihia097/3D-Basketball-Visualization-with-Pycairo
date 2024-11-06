# Paint Fight Game

Paint Fight Game is a competitive, two-player game where each player aims to cover the most area with their paint color. Players score points by painting areas of the screen; if one player paints over another player’s color, it adds to their score and deducts from the other player’s score. The game features dynamic gradient backgrounds, obstacles, and timed gameplay.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Settings](#game-settings)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Two-Player Mode**: Compete against another player in real-time.
- **Dynamic Gradient Background**: Smooth color transitions with adjustable RGB values for a dynamic and appealing backdrop.
- **Obstacle Mechanics**: Moving obstacles on the screen that players must avoid.
- **Score Tracking**: Points system that rewards players for covering area with paint and penalizes players if their paint is covered.
- **Game Timer**: A timer tracks the game's duration and signals the end.
- **Player Movement Delay**: Adjustable player move delay for more dynamic gameplay.

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/paint-fight-game.git
   cd paint-fight-game
   ```

2. Install dependencies:

   ```bash
   pip install pygame
   ```

3. Run the game:

   ```bash
   python main.py
   ```

  Refer to [requirements.txt](cg_open_source_project/src/paint_fight/requirements.txt)


## How to Play

- **Objective**: Cover the most screen area with your paint color before the game timer ends.
- **Player Controls**:
  - **Player 1**: Use `WASD` keys to move.
  - **Player 2**: Use `Arrow` keys to move.
- **Scoring**:
  - Paint over unpainted areas or areas painted by the other player to score points.
  - Covering the other player’s color adds to your score and deducts from theirs.
- **Obstacles**: Avoid obstacles moving on the screen, as they reset your position if hit.
- **End of Game**: When the timer ends, the player with the most points wins.

## Game Settings

You can modify game parameters in the code to customize your experience:

- **Player Move Delay**: Adjust `PLAYER_MOVE_DELAY` to control player speed.
- **Gradient Colors**: Modify `grad_start_color` and `grad_end_color` for different background color effects.
- **Obstacle Speed and Position**: Set `OBSTACLE_SPEED` and initial `obstacle_pos` for varied gameplay.

## Project Structure

```plaintext
paint-fight-game/
│
├── main.py               # Main game logic and loop
├── settings.py           # Game settings (colors, speeds, etc.)
├── assets/               # Game assets (images, sounds, etc.)
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (for pip installation)
```

## Contributing

Contributions are welcome! Please open an issue first to discuss your ideas, and then submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.



# 3D Basketball Visualization with Pycairo

A visually realistic 3D basketball illustration built using Python and the Pycairo graphics library. This project utilizes advanced computer graphics techniques to create depth, texture, and accurate curvature lines for a lifelike basketball design.

## Project Overview

This project demonstrates how to use Bezier curves, gradients, and radial shading to simulate a 3D basketball effect in 2D graphics. With Pycairo, a powerful vector graphics library, this project combines artistry and programming to bring a basketball to life, complete with textured shading and realistic seam curves.

## Features

- **3D Sphere Representation**: Uses radial gradients to give the basketball a realistic 3D appearance.
- **Basketball Seam Curves**: Bezier curves simulate the characteristic lines on a basketball, including intersecting diagonal and vertical seams.
- **Texture and Shading**: Applied color gradients and shadows for depth and texture.

## Requirements

- **Python 3.x**
- **Pycairo Library**

Install Pycairo using pip:
```bash
pip install pycairo
