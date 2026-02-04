# Python Pong Game
A modular, Object-Oriented implementation of the classic **Pong arcade game** using Python’s built-in **Turtle Graphics** module.

This project demonstrates real-time game loops, collision physics, keyboard-driven controls, and clean separation of responsibilities using OOP principles.

---

## OOP Architecture & Principles
The project is designed with a strong Object-Oriented structure:

* ***Encapsulation***:  
  Each game entity (Paddle, Ball, Scoreboard) is encapsulated in its own class and file, isolating behavior and state.

* ***Inheritance***:  
  `Paddle`, `Ball`, and `Scoreboard` all inherit from the `Turtle` superclass, leveraging built-in rendering, movement, and drawing capabilities.

* ***Abstraction***:  
  The `main.py` controller interacts only with high-level methods such as `ball.move()` or `paddle.go_up()`, without managing internal coordinates or physics.

* ***State Management***:  
  The `Ball` class manages velocity vectors and speed internally, while `Scoreboard` maintains and updates player scores.

---

## Technical Specifications & Game Dimensions
The following dimensions are fixed to ensure consistent gameplay and collision detection:

* **Screen Size**: `800 x 600`
* **Paddle Width**: `20`
* **Paddle Height**: `100`
* **Wall Collision (Y-axis)**: `±280`
* **Paddle Collision (X-axis)**: `±320`
* **Miss Detection (X-axis)**: `±380`

---

## Project Architecture
The game is divided into four core components to maintain clarity and scalability.

### 1. Game Controller (`main.py`)
Acts as the game engine:

* Initializes the screen and disables auto-refresh using `tracer(0)`
* Controls the main game loop and frame updates
* Handles:
  * Wall collision
  * Paddle collision
  * Miss detection
  * Score updates
* Maps keyboard inputs to paddle movement

---

### 2. Paddle Logic (`paddle.py`)
Handles player movement:

* **Structure**:
  * Vertical rectangular paddle using stretched square shape
* **Movement**:
  * Moves up/down in fixed increments of `20` units
* **Controls**:
  * Right Paddle: `↑` / `↓`
  * Left Paddle: `W` / `S`

---

### 3. Ball Physics System (`ball.py`)
Controls motion and collision response:

* **Velocity Vector**:
  * Maintains independent X and Y movement components
* **Wall Bounce**:
  * Inverts Y-direction on top/bottom collision
* **Paddle Bounce**:
  * Inverts X-direction on paddle collision
  * Gradually increases speed (`ball_speed *= 0.9`) for difficulty scaling
* **Reset Logic**:
  * Resets position and speed when a point is scored

---

### 4. Scoreboard System (`scoreboard.py`)
Manages scoring and UI:

* Displays left and right player scores at the top of the screen
* Uses `"Courier"` font with large size for arcade-style visuals
* Automatically clears and redraws the score on each update

---

## Execution
Ensure all files are in the same directory:

```bash
python main.py
