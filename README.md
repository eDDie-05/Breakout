#  Breakout Game — Python

A simple **Breakout arcade game** built with Python and Pygame.

##  About the Game

The goal is to control the paddle and bounce the ball to destroy all the bricks.

### Features

*  Player-controlled paddle
*  Bouncing ball
*  Destructible bricks
*  Score system
*  Lives system
*  Win and game-over conditions
*  Keyboard controls

##  Requirements

* Python 3
* Pygame

##  Installation

Install Pygame using:

```bash
python3 -m pip install pygame
```

Check that it was installed:

```bash
python3 -m pygame
```

##  How to Run

Go to the folder containing the game:

```bash
cd path/to/breakout
```

Then run:

```bash
python3 main.py
```

If the main file has a different name, for example `breakout.py`:

```bash
python3 breakout.py
```

##  Controls

| Key   | Action               |
| ----- | -------------------- |
| ←     | Move paddle left     |
| →     | Move paddle right    |
| Space | Start / restart game |
| Esc   | Quit game            |

##  Project Structure

```text
breakout/
│
├── main.py
├── README.md
├── assets/
│   ├── images/
│   └── sounds/
└── requirements.txt
```

##  requirements.txt

```text
pygame
```

##  Future Improvements

* Multiple levels
* Different brick types
* Power-ups
* Sound effects
* Background music
* High-score saving
* Improved graphics

##  Built With

* Python
* Pygame

##  License
By eDDie
This project is for educational and personal use.
