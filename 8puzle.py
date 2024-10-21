import heapq

# Define el estado objetivo del puzzle
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 representa el espacio vacío
]

# Función para obtener las coordenadas de una loseta
def find_position(state, tile):
    for i, row in enumerate(state):
        if tile in row:
            return (i, row.index(tile))
    return None

# Función para calcular el costo heurístico (distancia de Manhattan)
def heuristic(state):
    cost = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                goal_i, goal_j = find_position(goal_state, state[i][j])
                cost += abs(i - goal_i) + abs(j - goal_j)
    return cost

# Función para generar los posibles movimientos
def generate_moves(state):
    moves = []
    x, y = find_position(state, 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, derecha
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(state) and 0 <= ny < len(state[0]):
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

# Algoritmo de ramificación y poda usando una cola de prioridad (A*)
def solve_puzzle(initial_state):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(initial_state), 0, initial_state, []))
    visited = set()

    while priority_queue:
        _, moves, current_state, path = heapq.heappop(priority_queue)

        if current_state == goal_state:
            return path + [current_state]

        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for next_state in generate_moves(current_state):
            new_path = path + [current_state]
            heapq.heappush(priority_queue, (heuristic(next_state) + len(new_path), len(new_path), next_state, new_path))

    return None

# Estado inicial del puzzle (puedes cambiarlo según el problema)
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Resuelve el puzzle
solution = solve_puzzle(initial_state)

# Imprime los pasos de la solución
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No se encontró solución.")
