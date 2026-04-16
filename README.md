This project is an OOP-based 2D simulation engine developed with Python and Pygame. It focuses on solving the real-life problem of visualizing spatial interaction algorithms, specifically vector-based pursuit and grid-based collision detection.

🚀 How to Download and Run
Follow these steps to get the project running on your local machine:

1. Prerequisites
Ensure you have Python 3.8 or higher installed. You can check your version by running:
python --version

2. Download the Project

Open your terminal/command prompt and run:
git clone https://github.com/yhkwan36/COMP2090SEFgroup-project.git
cd COMP2090SEFgroup-project

3. Install Required Libraries
This project requires the pygame library. Install it using pip:

pip install pygame
4. Running the Simulation
Navigate to the project root folder (where main.py is located) and execute:
python main.py

🎮 Controls & Gameplay
Movement: Use W, A, S, D to navigate the agent.

Attack: Press Spacebar to trigger attack.

Objective: The simulation demonstrates how the enemy agent (Autonomous AI) calculates vectors to track the player while the camera manages Y-sorting depth perception.

🛠️ Technical Architecture (OOP)
This application implements all core Object-Oriented Programming concepts:

Inheritance: Player and Enemy inherit from pygame.sprite.Sprite.

Encapsulation: Object attributes (health, hitbox) are managed via internal class methods.

Polymorphism: The visible_sprites group handles diverse entity types via a unified .update() interface.

Abstraction: The Level class abstracts complex map parsing and rendering logic.

📁 File Structure
main.py: Entry point.

level.py: World coordination and Camera logic.

player.py & enemy.py: Entity behaviors.

support.py: CSV data importer.

PNGs/: (Crucial) Contains all required 16-bit visual assets.

data/: Contains .csv files for level layout.
