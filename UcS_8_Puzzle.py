import heapq

# Cari 0
def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i, j)

# Tuker
def swap(board, pos1, pos2):
    new_board = [row[:] for row in board]  # Buat salinan papan
    x1, y1 = pos1
    x2, y2 = pos2
    new_board[x1][y1], new_board[x2][y2] = new_board[x2][y2], new_board[x1][y1]
    return new_board

# Cek Valid + gerak
def get_neighbors(board):
    neighbors = []
    blank_pos = find_blank(board)
    x, y = blank_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = swap(board, blank_pos, (new_x, new_y))
            neighbors.append(new_board)

    return neighbors

def is_goal(board, goal):
    return board == goal

def UcS(start, goal):
    queue = [(0, start, [])]  # (biaya, papan saat ini, Path)
    visited = set()  
    visited.add(tuple(map(tuple, start)))

    while queue:
        cost, current_board, path = heapq.heappop(queue)

        if is_goal(current_board, goal):
            return path

        # Semua kemungkinan gerakan
        for neighbor in get_neighbors(current_board):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                heapq.heappush(queue, (cost + 1, neighbor, path + [neighbor]))  # +1 Cost not visited

    return None

def print_board(board):
    for row in board:
        print(row)
    print()

def input_board(board_type):
    print(f"Masukkan {board_type} state (9 angka, 0 untuk ruang kosong):")
    board = []
    numbers = list(map(int, input().split()))  
    for i in range(0, 9, 3):
        board.append(numbers[i:i+3])
    return board

if __name__ == "__main__":
    start_board = input_board("starting")
    goal_board = input_board("goal")

    print("Start Board:")
    print_board(start_board)

    print("Goal Board:")
    print_board(goal_board)

    solution_path = UcS(start_board, goal_board)

    if solution_path:
        print("Solusi ditemukan dalam", len(solution_path), "langkah.")
        for step in solution_path:
            print_board(step)
    else:
        print("Tidak ada solusi.")
