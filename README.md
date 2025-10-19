# Conway's Game of Life

An interactive implementation of **Conway's Game of Life** using Python and Pygame.

### Rules of the Game

The Game of Life is a zero-player game where each cell follows simple rules:

1. Any live cell with **2 or 3 neighbors** survives.  
2. Any dead cell with **exactly 3 neighbors** becomes alive.  
3. All other live cells **die**, and dead cells **stay dead**.  

From these simple rules, complex and beautiful patterns can emerge!

## Installation
### 1. Clone the repository
### 2. Create a virtual environment (optional but recommended):
``` 
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```
### 3. Install dependencies:
``` 
pip install -r requirements.txt
```
### 4. Run the game and have fun!
```bash
python3 main.py
```

## Controls

- **Left Click** – Draw a live cell (only when paused)  
- **Right Click** – Erase a live cell (only when paused)  
- **SPACE** – Toggle pause/play

## Notes
- This is a simple demo of Conway's Game of Life. Feel free to **modify anything you like**!  
- Adjust the `WIDTH`, `HEIGHT`, and `CELL_SIZE` in `main.py` to fit your screen resolution perfectly.  
- Experiment with colors, speed, or even start patterns — the code is easy to tweak!  
- Have fun exploring the game and creating your own life patterns!

## License
Released under the **[MIT License](LICENSE)**
