#!/usr/bin/env python3.5
import os

P1 = "[X]"
P2 = "[O]"
empty = "[ ]"


class Game:
    def __init__(self, cells):
        self.cells = cells
        self.g_map = [['' for i in range(self.cells)] for i in range(self.cells)]
        self.grid = self.init_grid(self.cells)

    # Create the map for the game
    def init_grid(self, cells):
        grid = list()
        sub = list()
        for i in range(cells):
            for x in range(cells):
                sub.append(tuple((i, x)))
            grid.append(tuple(sub))
            sub = list()
        return grid

    def draw_table(self):
        for i in range(int(self.cells)):
            print()
            for x in range(int(self.cells)):
                position = tuple((i, x))
                if self.g_map[position[0]][position[1]] != '':
                    print(self.g_map[position[0]][position[1]], end='')
                else:
                    print(empty, end='')
        print()

    def map_move(self, p, px):
        try:
            if self.g_map[p[0]][p[1]] == '':
                self.g_map[p[0]][p[1]] = px
                self.last_move = p
                self.last_player = px
            else:
                return 1
        except Exception as e:
            print("Invalid value. Allowed values from 0 to {}".format(self.cells - 1))
            return 1
        return 0

    def check_win(self, table, last_move):
        if table[0][last_move[1]] == table[1][last_move[1]] == table[2][last_move[1]] != '':
            return 1
        elif table[last_move[0]][0] == table[last_move[0]][1] == table[last_move[0]][2] != '':
            return 1
        elif table[0][0] == table[1][1] == table[2][2] != '':
            return 1
        elif table[0][2] == table[1][1] == table[2][0] != '':
            return 1
        else:
            return 0

    def get_move(self, p):
        try:
            m = input("\nNext Move {}: ".format(p))
            m1 = int(m.split(',')[0])
            m2 = int(m.split(',')[1])
            return tuple((m1, m2))
        except Exception as e:
            return 1

    def cls(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


if __name__ == "__main__":
    start = 'y'
    while start == 'y':
        g = Game(3)
        turn = 1
        win = False
        while win == False:
            if turn % 2 != 0:
                g.draw_table()
                while g.map_move(g.get_move("P1"), P1):
                    print("Invalid move")
                if g.check_win(g.g_map, g.last_move):
                    print("P1 Won this game")
                    g.draw_table()
                    win = True
            else:
                g.draw_table()
                while g.map_move(g.get_move("P2"), P2):
                    print("Invalid Move")
                if g.check_win(g.g_map, g.last_move):
                    print("P2 Won this game")
                    g.draw_table()
                    win = True
            turn += 1
            g.cls()
    
        start  = input("\nWould you like to try again?[y/n]: ").lower()


    
