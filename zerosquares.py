import msvcrt  
import copy  
from algorithms import BFS
from algorithms import DFSRecursion
from algorithms import UCS

class Square:
    def __init__(self, x, y, type) -> None:
        self.x = x
        self.y = y
        self.type = type  

    def __str__(self) -> str:
        return str(self.type)

class State:
    def __init__(self, rows, cols, board) -> None:
        self.rows = rows
        self.cols = cols
        self.board = board

    def __str__(self) -> str:
        result = ""
        for row in self.board:
            for square in row:
                result += str(square)  
            result += '\n'  
        return result 

    def __eq__(self, other):
        if isinstance(other, State):
            if self.rows != other.rows or self.cols != other.cols:
                return False
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j].type != other.board[i][j].type:
                        return False
            return True
        return False

    def __hash__(self):
        board_tuple = tuple(tuple(square.type for square in row) for row in self.board)
        return hash(board_tuple)  

class Game:
    def __init__(self, init_state) -> None:
        self.init_state = init_state

    def getPCoords(self, state):
        for row in state.board:
            for square in row:
                if square.type == 2:  
                    return square.x, square.y

    def move(self, direction):
        x, y = self.getPCoords(self.init_state)

        if direction == 'w':  
            dx, dy = -1, 0
        elif direction == 's':  
            dx, dy = 1, 0
        elif direction == 'a':  
            dx, dy = 0, -1
        elif direction == 'd':  
            dx, dy = 0, 1
        else:
            return  

        while True:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < self.init_state.rows and 0 <= new_y < self.init_state.cols:
                if self.init_state.board[new_x][new_y].type == 0: 
                    self.init_state.board[x][y].type = 0  
                    self.init_state.board[new_x][new_y].type = 2  
                    x, y = new_x, new_y 
                elif self.init_state.board[new_x][new_y].type == 'p':  
                    self.init_state.board[x][y].type = 0  
                    self.init_state.board[new_x][new_y].type = 2  
                    print("Congratulations! You've reached the goal!")
                    return True  
                else:
                    break  
            else:
                break  

        return False  

    def check_game_over(self):
        x, y = self.getPCoords(self.init_state)

        if self.init_state.board[x][y].type == 'p':
            return True
        return False


    def generate_possible_states(self):
        x, y = self.getPCoords(self.init_state)  
        
        directions = [('w', -1, 0), ('s', 1, 0), ('a', 0, -1), ('d', 0, 1)]  
        
        possible_states = []
        for directions, dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.init_state.rows and 0 <= new_y < self.init_state.cols:
                if self.init_state.board[new_x][new_y].type == 0 or self.init_state.board[new_x][new_y].type == 'p':
                    new_state = copy.deepcopy(self.init_state)  
                    new_state.board[x][y].type = 0  
                    new_state.board[new_x][new_y].type = 2  
                    possible_states.append(new_state)  
        return possible_states    

def draw_board(game):
    print(game.init_state)  

def main():
    init_board = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 1],  
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 'p', 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 0, 0],
        
    ]
    
    rows = len(init_board)
    cols = len(init_board[0])

    board = [[None for _ in range(cols)] for _ in range(rows)]


    for i in range(rows):
        for j in range(cols):
            square_type = init_board[i][j]  
            board[i][j] = Square(i, j, square_type)

    init_state = State(rows, cols, board)
    game = Game(init_state)

    draw_board(game)
    
    

    algorithm = input("Enter (BFS/DFS/UCS): ")
    if algorithm == 'bfs':
        bfs = BFS(game)
        bfs.bfs_move()
    elif algorithm == 'dfs':
        # dfs = DFS(game)
        # dfs.dfs_move()
        # dfs.dfsr(0,0)
        dfs=DFSRecursion(game)
        dfs.dfs_move()
        dfs.dfs_move_recursive(0,0,0)
    elif algorithm=='ucs':
        ucs = UCS(game)
        ucs.ucs_move()
        
    else:
        print("Invalid")

    # while True:
    #     print("Use 'w' for Up, 'a' for Left, 's' for Down, 'd' for Right, 'q' to quit.")
    #     key = msvcrt.getch().decode('utf-8')  

    #     if key == 'q':  
    #         print("Exiting game...")
    #         break

    #     if game.move(key):  
    #         draw_board(game)  
    #         break  

    #     draw_board(game)  

    #     if game.check_game_over():
    #         print("Congratulations! You've reached the goal!")
    #         break  

    #     possible_states = game.generate_possible_states()
    #     print(f"\nPossible states after your move (4 directions):")
    #     for i, state in enumerate(possible_states, 1):
    #         print(f"Possible state {i}:")
    #         print(state)
    #         print("-" * 30)

    #     if game.init_state == possible_states[0]:
    #         print("The first possible state is the same as the current state.")
    #     else:
    #         print("The first possible state is different from the current state.")

if __name__ == '__main__':
    main()
