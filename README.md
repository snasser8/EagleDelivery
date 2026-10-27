
# Eagle Delivery — COSC 461 Project 1

This project uses search algorithms and Q-learning to help a robot find delivery routes between buildings on a campus map.

## Requirements

- Python 3.9 or newer
- Python's built-in `unittest` module

## Part A: BFS and A* Search

I implemented A* search using Manhattan distance as the heuristic and compared its results with BFS on the original campus map and a detour map.

Both algorithms found the same shortest paths, but A* expanded fewer nodes in all six tests.

## Part B: Q-Learning

I implemented epsilon-greedy action selection and Q-learning to train the robot on three delivery routes: S → W, L → D, and H → P.

Each route was trained for 2,000 episodes using seeds 0, 1, and 2. After training, all three routes achieved a 100% evaluation success rate.

## Part C: Custom Map and Experiment

I created a 9 × 13 custom campus map containing six building entrances, walls, dead ends, and a cycle.

I tested epsilon values of 0.05, 0.20, and 0.50 to compare exploration during training. All three settings achieved a 100% final evaluation success rate and found the shortest 10-step route from S to W.

## Running the Project

### Show the campus map

```bash
python3 run_project.py show
```

### Run BFS

```bash
python3 run_project.py search --algorithm bfs --start S --goal W
```

### Run A* Search

```bash
python3 run_project.py search --algorithm astar --start S --goal W
```

### Run A* on the custom map

```bash
python3 run_project.py search --map maps/my_campus.txt --algorithm astar --start S --goal W
```

### Train the robot using Q-learning

```bash
python3 run_project.py train --map maps/emu_campus.txt --start S --goal W --episodes 2000 --seeds 0 1 2 --eval-episodes 100 --max-steps 200 --alpha 0.3 --gamma 0.95 --epsilon 0.2 --slip 0 --output results/baseline_S_W.csv
```

### Run the tests

```bash
python3 -m unittest discover -v
```

## Project Files

- `agents.py` — A* search, Manhattan distance, epsilon-greedy, and Q-learning implementations
- `campus.py` — Campus map environment
- `run_project.py` — Commands for running searches and training
- `summarize_results.py` — Generates learning curve summaries
- `maps/` — Original, detour, and custom campus maps
- `results/` — Training and evaluation CSV files
- `plots/` — Learning curves and exploration comparison graphs
- `tests/` — Project tests
- `Eagle_Delivery_Report.pdf` — Final project report

## Results

Both BFS and A* found optimal routes, but A* expanded fewer nodes in all six comparisons.

After Q-learning training, all three baseline delivery routes achieved 100% evaluation success.

On the custom map, all three exploration settings achieved 100% final evaluation success, although higher epsilon values produced lower average training rewards.

The complete results, tables, and graphs are included in [Eagle Delivery Report](Eagle_Delivery_Report.pdf).
