# Paint Fight Game

Paint Fight Game is an engaging, two-player game where players compete to cover the most area with their paint. Players can strategically paint over each other's colors to increase their score and reduce their opponent's, creating a dynamic and competitive experience. The game features a vibrant gradient background, obstacles, and timed gameplay for added excitement.

![Game Preview](#)  
<img width="599" alt="preview_image1" src="https://github.com/user-attachments/assets/6ed1a530-9ce7-4a11-b24e-c118425181e7">

---

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Settings](#game-settings)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Two-Player Mode**: Compete head-to-head with another player.
- **Dynamic Gradient Background**: Smooth color transitions create an eye-catching and dynamic environment.
- **Obstacle Mechanics**: Moving obstacles add a level of difficulty to navigate.
- **Score Tracking**: Gain points for painting new areas; lose points if your paint is covered.
- **Game Timer**: The game ends when the timer runs out, determining the winner based on points.
- **Player Movement Delay**: Adjustable settings allow fine-tuning of player speed.

---

## Getting Started

Follow these steps to install and run the game on your computer.

### Installation

1. **Download the Game**  
   First, download the Paint Fight Game files:
   
   ```bash
   git clone https://github.com/yourusername/paint-fight-game.git
   cd paint-fight-game
   ```

2. **Install Required Software**  
   The game requires Python and the `pygame` library. Install `pygame` by running:
   
   ```bash
   pip install pygame
   ```

3. **Start the Game**  
   To start the game, use the following command:
   
   ```bash
   python main.py
   ```

   > **Note**: You can also refer to the [requirements.txt](cg_open_source_project/src/paint_fight/requirements.txt) file for a list of all dependencies.

---

## How to Play

- **Objective**: Cover the most area with your color before the timer runs out.
- **Controls**:
  - **Player 1**: Use `W`, `A`, `S`, `D` keys to move.
  - **Player 2**: Use `Arrow` keys to move.
- **Scoring**:
  - Paint over empty areas or your opponent's color to increase your score.
  - Painting over the opponent’s color deducts points from them and adds to your score.
- **Obstacles**: Avoid obstacles as they will reset your position if touched.
- **Game End**: When the timer finishes, the player with the most points wins.

---

## Game Settings

You can adjust game settings in the code to customize the experience to your liking:

- **Player Speed**: Modify `PLAYER_MOVE_DELAY` to adjust how fast players move.
- **Background Colors**: Adjust `grad_start_color` and `grad_end_color` to create custom gradient backgrounds.
- **Obstacle Settings**: Change `OBSTACLE_SPEED` and starting `obstacle_pos` for varied gameplay.

---

## Project Structure

```plaintext
paint-fight-game/
├── main.py               # Main game logic and loop
├── settings.py           # Game settings (colors, speeds, etc.)
├── assets/               # Game assets (images, sounds, etc.)
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (for pip installation)
```

---

## Contributing

We welcome contributions to improve Paint Fight Game! Here’s how to get started:

1. **Fork the Repository**  
2. **Create a New Branch**:  
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make Your Changes**  
4. **Commit Changes**  
   ```bash
   git commit -m "Add Your Feature"
   ```
5. **Push Changes**  
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Submit a Pull Request**

---
