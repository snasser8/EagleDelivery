from collections import deque
import heapq
from itertools import count


class SearchResult:
    def __init__(self, path, expanded):
        self.path = path
        self.expanded = expanded


def reconstruct_path(parents, goal):
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parents[state]
    path.reverse()
    return path


def bfs(campus, start, goal):
    frontier = deque([start])
    parents = {start: None}
    expanded = 0
    while frontier:
        state = frontier.popleft()
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)
        expanded += 1
        for action, successor in campus.neighbors(state):
            if successor not in parents:
                parents[successor] = state
                frontier.append(successor)
    return SearchResult(None, expanded)


def manhattan(state, goal):
    """TODO 1: Return Manhattan distance between two (row, column) tuples."""
    # Add the absolute row difference and the absolute column difference.

    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])



def astar(campus, start, goal):
    """TODO 2: Return SearchResult(path, expanded) for A* graph search."""
    # Use heapq as a priority queue and manhattan() as the heuristic.
    # Track best known g-costs and parent states in dictionaries.
   
    if start == goal:
        return SearchResult([start], 0) 

    frontier = []
    best_g = {start: 0}
    parent = {start: None}
    expanded = 0

    insertion_number = 0
    start_f = manhattan(start, goal)

    heapq.heappush(
        frontier, 
        (start_f, insertion_number, 0, start)
    )

    while frontier:
        f,order,g, state = heapq.heappop(frontier)

        if g != best_g[state]:
            continue

        if state == goal:
            return SearchResult(
                reconstruct_path(parent, goal), 
                expanded
                )
        expanded += 1

        for action, neighbor in campus.neighbors(state):
            new_g = g + 1

            if new_g < best_g.get(neighbor,
                                  float('inf')):
                best_g[neighbor] = new_g
                parent[neighbor] = state

                new_f = new_g + manhattan(neighbor, goal)

                insertion_number += 1
                heapq.heappush(
                    frontier,
                    (new_f, insertion_number, new_g, neighbor)
                )

    return SearchResult(None, expanded)


def epsilon_greedy(q_values, state, actions, epsilon, rng):
    """TODO 3: Choose an action with epsilon-greedy exploration."""
    # q_values is a dictionary. Its keys are (state, action) pairs.
    # Example key: ((1, 1), "RIGHT"). Unseen entries have value 0.0.

    if rng.random() < epsilon:
        return rng.choice(actions)

    best_vaule = max(
        q_values.get((state, action), 0.0) 
        for action in actions
    )

    best_actions = [
        action for action in actions
        if q_values.get((state, action), 0.0) == best_vaule
    ]

    return rng.choice(best_actions)

def q_learning_update(q_values, state, action, reward, next_state,
                      actions, alpha, gamma, terminal):
    """TODO 4: Update exactly one Q-table entry in place; return nothing."""
    # Get Q(state, action), defaulting to 0.0.
    # If terminal is True, the target is reward with no continuation term.
    # Otherwise target = reward + gamma * max Q(next_state, next_action).
    # Consider every action, including unseen entries with value 0.0.
    # Apply Q <- Q + alpha * (target - Q).
   
    # Get the current Q-value (default is 0)
    old_q = q_values.get((state, action), 0.0)

    # Calculate the target
    if terminal:
        target = reward
    else:
        best_next_q = max(
            q_values.get((next_state, next_action), 0.0)
            for next_action in actions
        )
        target = reward + gamma * best_next_q

    # Update the Q-value
    q_values[(state, action)] = old_q + alpha * (target - old_q)
