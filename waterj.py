from math import gcd
from heapq import heappush, heappop

def heuristic(a, b, d):
    return min(abs(d - a), abs(d - b))

def minSteps_Astar(m, n, d):
    if d > max(m, n) or d % gcd(m, n):
        return "Can't obtain the required state"

    heap = []
    visited = set()
    prev = {}

    # Start from (0, 0), cost = 0, heuristic = h(0, 0)
    heappush(heap, (heuristic(0, 0, d), 0, 0, 0))  # (f, a, b, steps)
    visited.add((0, 0))

    while heap:
        f, a, b, s = heappop(heap)

        if a == d or b == d:
            # Reconstruct path
            path = []
            while (a, b) in prev:
                path.append((a, b))
                a, b = prev[(a, b)]
            path.append((0, 0))
            print("Steps to reach the target state:")
            for state in reversed(path):
                print(state)
            return s

        # All possible actions (same as BFS)
        for x, y in [
            (m, b),  # Fill jug1
            (a, n),  # Fill jug2
            (0, b),  # Empty jug1
            (a, 0),  # Empty jug2
            (a - min(a, n - b), b + min(a, n - b)),  # Pour jug1 → jug2
            (a + min(b, m - a), b - min(b, m - a))   # Pour jug2 → jug1
        ]:
            if (x, y) not in visited:
                visited.add((x, y))
                prev[(x, y)] = (a, b)
                cost = s + 1
                h = heuristic(x, y, d)
                heappush(heap, (cost + h, x, y, cost))  # f = g + h

    return "No solution found"

# Example usage
print("Minimum steps:", minSteps_Astar(4, 3, 2))
