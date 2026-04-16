# COMP2090SEF Group Project - Pixel Survivor

A 2D top-down RPG survival game developed with Python and Pygame, demonstrating strong Object-Oriented Programming concepts.

## Project Purpose
This game was created to solve a real-life problem: **making programming education more engaging and practical**. Many students find it difficult to understand OOP concepts (Inheritance, Encapsulation, Polymorphism, Composition) through abstract examples. By building a playable game, students can see how OOP principles are applied in real software development, improving learning motivation and coding skills.

## Features
- Smooth camera system that follows the player with Y-sorting
- Four-direction player walking animation
- Enemy AI that intelligently chases the player
- Attack system with cooldown and range detection
- Tile-based map created with Tiled editor
- Player and enemy health system with Game Over screen
- Collision detection using hitbox

## Controls
- **WASD** → Move the player
- **Space** → Attack
- Close window → Quit game

## How to Run the Game

1. Make sure Python 3.8 or higher is installed
2. Install the required package:
   ```bash
   pip install -r requirements.txt

Run the game:Bashpython main.py

Project Structure

main.py - Main game loop
level.py - Game level management and camera
player.py - Player class with movement and attack
enemy.py - Enemy AI and behavior
tile.py - Tile and obstacle system
support.py - CSV map loader
PNGs/ - All game images
map.tmx - Tiled map file

OOP Concepts Demonstrated

Inheritance: Player and Enemy inherit from pygame.sprite.Sprite
Encapsulation: Game logic is properly encapsulated in classes
Polymorphism: Different update() behaviors for Player and Enemy
Composition: Level class composes sprite groups and camera

Future Improvements

Add sound effects and background music
Multiple levels and boss fights
Inventory and item system
Better multi-frame attack animations

Video Demonstration

Group Members

Kenneth Kwan (Team Leader & Main Programmer)
