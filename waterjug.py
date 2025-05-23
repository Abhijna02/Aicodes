from collections import deque
from math import gcd

def minSteps(m, n, d):
    # If it's impossible to measure 'd' using the jugs
    if d > max(m, n) or d % gcd(m, n): 
        return "Can't obtain the required state"

    q, visited = deque([(0, 0, 0)]), {(0, 0)}  # Queue for BFS, set to track visited states
    prev = {}  # Dictionary to store the path (parent states)

    while q:
        a, b, s = q.popleft()  # Current state: jug1 = a, jug2 = b, steps = s

        # If either jug has the target amount, reconstruct the path
        if a == d or b == d:
            path = []
            while (a, b) in prev:
                path.append((a, b))
                a, b = prev[(a, b)]  # Trace back to the previous state
            path.append((0, 0))  # Add the initial state
            print("Steps to reach the target state:")
            for state in reversed(path): 
                print(state)  # Print each state in the path
            return s  # Return number of steps

        # List of all possible next states (actions)
        for x, y in [
            (m, b),  # Fill jug1
            (a, n),  # Fill jug2
            (0, b),  # Empty jug1
            (a, 0),  # Empty jug2
            (a - min(a, n - b), b + min(a, n - b)),  # Pour jug1 → jug2
            (a + min(b, m - a), b - min(b, m - a))   # Pour jug2 → jug1
        ]:
            if (x, y) not in visited:
                visited.add((x, y))        # Mark new state as visited
                prev[(x, y)] = (a, b)      # Store how we got to this state
                q.append((x, y, s + 1))    # Add new state to queue with incremented steps

    return "No solution found"  # If the queue is exhausted and no solution is found

# Example usage
print("Minimum steps:", minSteps(4 , 3, 2))
