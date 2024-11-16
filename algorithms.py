from collections import deque

def draw_board(game):
    for row in game.init_state.board:
        print(' '.join(str(square.type) for square in row))  

class BFS:
    def __init__(self, game):
        self.game = game
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    def bfs_move(self):
        start_x, start_y = self.game.getPCoords(self.game.init_state)
        goal_x, goal_y = None, None
        
        for row in self.game.init_state.board:
            for square in row:
                if square.type == 'p':
                    goal_x, goal_y = square.x, square.y
                    break
            if goal_x is not None:
                break
        
        queue = deque([(start_x, start_y, [])])  
        visited = set()
        visited.add((start_x, start_y))

        while queue:
            x, y, path = queue.popleft()

            if (x, y) == (goal_x, goal_y):
                self._apply_move(path)
                print("BFS: Found a path to the goal")
                return True

            for dx, dy in self.directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.game.init_state.rows and 0 <= new_y < self.game.init_state.cols:
                    if (new_x, new_y) not in visited and (self.game.init_state.board[new_x][new_y].type == 0 or self.game.init_state.board[new_x][new_y].type == 'p'):
                        visited.add((new_x, new_y))
                        new_path = path + [(new_x, new_y)]  
                        queue.append((new_x, new_y, new_path))

        print("***BFS***")
        return False

    def _apply_move(self, path):
        current_state = self.game.init_state
        x, y = self.game.getPCoords(current_state)
        
        print("BFS: ")
        for new_x, new_y in path:
            print(f"Moving to ({new_x}, {new_y})")
            current_state.board[x][y].type = 0  
            current_state.board[new_x][new_y].type = 2  
            x, y = new_x, new_y
        
        draw_board(self.game)


def draw_board(game):
    for row in game.init_state.board:
        print(' '.join(str(square.type) for square in row))  

class DFS:
    def __init__(self, game):
        self.game = game
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    def dfs_move(self):
        start_x, start_y = self.game.getPCoords(self.game.init_state)
        goal_x, goal_y = None, None
        
        for row in self.game.init_state.board:
            for square in row:
                if square.type == 'p':
                    goal_x, goal_y = square.x, square.y
                    break
            if goal_x is not None:
                break
        
        stack = [(start_x, start_y, [])]  
        visited = set()  
        visited.add((start_x, start_y))

        while stack:
            x, y, path = stack.pop()  

            if (x, y) == (goal_x, goal_y):
                self._apply_move(path)
                print("DFS: Found a path to the goal")
                return True

            for dx, dy in self.directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.game.init_state.rows and 0 <= new_y < self.game.init_state.cols:
                    if (new_x, new_y) not in visited and (self.game.init_state.board[new_x][new_y].type == 0 or self.game.init_state.board[new_x][new_y].type == 'p'):
                        visited.add((new_x, new_y))
                        new_path = path + [(new_x, new_y)]  
                        stack.append((new_x, new_y, new_path))  

        print("***DFS***")
        return False

    def _apply_move(self, path):
        current_state = self.game.init_state
        x, y = self.game.getPCoords(current_state)
        
        print("DFS :")
        for new_x, new_y in path:
            print(f"Moving to ({new_x}, {new_y})")
            current_state.board[x][y].type = 0  
            current_state.board[new_x][new_y].type = 2  
            x, y = new_x, new_y
        
        draw_board(self.game)


