# 🧩 ASCII DFS Maze

An ASCII-based maze game developed as a university project. The game is played in the terminal and challenges players to reach the goal while avoiding obstacles like walls and monsters. Additionally, a Depth-First Search (DFS) algorithm can be triggered to automatically find a path to the goal, if one exists.

![Gameplay](media/gameplay.gif)

## 📜 Description

Upon launching the game, a random maze is generated with:

- Walls and doors randomly placed across the grid.
- A player `@` and a goal `>` positioned at opposite ends.
- Monsters (`Č`) and danger zones (`.`) around them.
- A sword (`:`) that allows the player to survive dangers once.

Each playthrough is unique due to the procedural map generation. Because of this, it's possible that some mazes may not have a valid path to the goal.

## 🎮 Controls

- `W` - Move up
- `A` - Move left
- `S` - Move down
- `D` - Move right
- `DFS` - Trigger automatic DFS pathfinding
- `Q` - Quit the game

## 🧠 Features

- ASCII map rendering in terminal
- Random map generation each run
- Monster and sword mechanics
- DFS algorithm for solving the maze
- Visual display of the DFS path with `*`

## 🚀 Running the Game

To run the game, execute the `main.py` file:

```bash
python main.py
```

Make sure `main.py`, `map.py`, and `symbols.py` are in the same directory.

> ⚠️ Recommended: Run the game in PyCharm or a terminal that handles ANSI colors properly.
> In some cases (e.g., VS Code terminal), extra lines may appear due to rendering issues.

## 📁 File Structure

```
ascii-dfs-maze/
├── main.py
├── map.py
├── symbols.py
├── media/
│   └── gameplay.gif
```

## 🧪 Example Output

When DFS is triggered, the game outputs the list of coordinates leading from the player to the goal, and displays the path directly in the maze using yellow `*` symbols.

---

### 🎮 Good luck navigating the maze — may the DFS be ever in your favor! 🔍✨
