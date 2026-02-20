# Snake (Python Turtle) 🐍

A classic Snake game built in **Python** using the built-in **turtle** graphics module.  
This project was a focused exercise in **object-oriented programming** — separating game entities into dedicated classes and keeping the game loop clean and readable.

## What this repo accomplishes

- Fully playable Snake game with real-time movement
- **Arrow key controls** (event-driven input via `Screen.onkey`)
- **Food spawning** at random positions and snake **growth** on collision
- **Score tracking** displayed on-screen
- Collision detection:
  - Snake ↔ wall boundary
  - Snake ↔ tail (self-collision)
- Game ends cleanly with a **GAME OVER** message

## Tech + concepts used

- **Python 3**
- **turtle** (`Screen`, `Turtle`, animation control with `tracer(0)` + `update()`)
- **OOP / Classes**
  - `Snake` manages segments + movement + direction rules
  - `Food` uses **inheritance** (`class Food(Turtle)`) to behave like a turtle object with extra spawn logic
  - `Scoreboard` uses **inheritance** (`class Scoreboard(Turtle)`) to draw UI text and manage score state
- **Game loop pattern**
  - `update → sleep → move → collision checks → render`
- **Separation of concerns** across 4 files for maintainability

## Project structure

- `main.py`  
  Sets up the screen, binds keyboard controls, runs the game loop, and coordinates collisions.

- `snake.py`  
  Implements the `Snake` class:
  - initializes the starting body
  - moves segments by shifting each segment to the previous segment’s position
  - grows the snake by appending a new segment at the tail
  - enforces direction constraints (prevents immediate 180° reversal)

- `food.py`  
  Implements `Food(Turtle)`:
  - spawns a small circular “food” turtle
  - randomly relocates food using `random.randint` within bounds

- `score.py`  
  Implements `Scoreboard(Turtle)`:
  - displays score at the top of the screen
  - increments and redraws score
  - renders “GAME OVER!” when the game ends

## How it works (based on the code)

### Screen + animation
The game uses:
- `screen.tracer(0)` to disable automatic drawing
- manual `screen.update()` each frame for smooth animation
- `time.sleep(0.1)` to control game speed

### Controls
Arrow keys trigger snake direction methods:
- Up → `snake.move_up()`
- Down → `snake.move_down()`
- Left → `snake.turn_left()`
- Right → `snake.turn_right()`

Direction changes include a heading check to prevent reversing into itself.

### Collision rules
- **Food collision**: if `food.distance(snake.head) < 15`
  - respawn food
  - extend snake
  - increment score
- **Wall collision**: if head crosses the boundary (`±280`)
  - end game + show “GAME OVER!”
- **Tail collision**: if head collides with any segment in `snake.segments[1:]`
  - end game + show “GAME OVER!”

## Run locally

### Requirements
- Python 3.x
- No external dependencies (only standard library modules)

### Start
```bash
python main.py
