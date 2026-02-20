# Pong

A classic two-player Pong game built with Python's `turtle` module.

## Features

- Two-player local multiplayer
- Adjustable difficulty (game speed)
- Custom target score to win
- Accurate rectangular paddle collision detection
- Random puck launch direction on tip-off
- Live scoreboard with winner announcement

## Project Structure

```
├── main.py         # Game loop and collision logic
├── puck.py         # Puck movement, bouncing, and tip-off
├── paddle.py       # Paddle class and movement
├── score.py        # Scoreboard display and winner announcement
├── config.py       # Constants, field setup, difficulty, and target score
```

## Controls

| Player       | Move Up | Move Down |
|--------------|---------|-----------|
| Left Player  | `W`     | `S`       |
| Right Player | `↑`     | `↓`       |

## How to Run

Make sure you have Python installed, then run:

```bash
python main.py
```

You will be prompted to select a difficulty and a target score before the game begins.

## Configuration

All constants like screen size, padding, and paddle positions are defined in `config.py`. You can tweak these to adjust the feel of the game:

```python
WIDTH = 1000
HEIGHT = 600
W_PADDING = 0.47
H_PADDING = 0.47
```

## Requirements

- Python 3.x
- No external libraries — uses only the built-in `turtle` module
