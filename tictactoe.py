#!/usr/bin/env python3.5
import os
from random import randint

Player = "[X]"
Computer = "[O]"
empty = "[ ]"


class Game:
    def __init__(self, cells):
        self.cells = cells
        self.g_map = [['' for i in range(self.cells)] for i in range(self.cells)]

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

    def check_table_full(self):
        for i in range(len(self.g_map)):
            for x in range(len(self.g_map[i])):
                if self.g_map[i][x] == '':
                    return False

        return True

    def gen_move(self, table):
        for priority in Computer,Player:
            for i in range(self.cells):
                # Give priority to first player in list (try to win)
                print("{} - {}".format(i,priority))
                # Chech horizontally
                if table[i][0] == table[i][2] == priority and table[i][1] == '':
                    return tuple((i,1))
                if table[i][0] == table[i][1] == priority and table[i][2] == '':
                    return tuple((i,2))
                if table[i][1] == table[i][2] == priority and table[i][0] == '':
                    return tuple((i,0))
                # Check vertically
                if table[0][i] == table[1][i] == priority and table[2][i] == '':
                    return tuple((2,i))
                if table[0][i] == table[2][i] == priority and table[1][i] == '':
                    return tuple((1,i))
                if table[1][i] == table[2][i] == priority and table[0][i] == '':
                    return tuple((0,i))
            # Check diagonals
            if table[0][0] == table[1][1] == priority and table[2][2] == '':
                return tuple((2,2))
            if table[0][0] == table[2][2] == priority and table[1][1] == '':
                return tuple((1,1))
            if table[1][1] == table[2][2] == priority and table[0][0] == '':
                return tuple((0,0))
            if table[0][2] == table[1][1] == priority and table[2][0] == '':
                return tuple((2,0))
            if table[1][1] == table[2][0] == priority and table[0][2] == '':
                return tuple((0,2))
            if table[0][2] == table[2][0] == priority and table[1][1] == '':
                return tuple((1,1))
        if table[1][1] == '':
            return ((1,1))
        else:
            return tuple((randint(0, 2), randint(0, 2)))

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
        TableFull = PlayerWins = ComputerWins = False
        g.cls()

        while PlayerWins == False and ComputerWins == False and TableFull == False:
            if turn % 2 != 0:
                g.draw_table()
                while g.map_move(g.get_move("Player"), Player):
                    print("Invalid move")
                if g.check_win(g.g_map, g.last_move):
                    PlayerWins = True
                TableFull = g.check_table_full()
            else:
                g.draw_table()
                while g.map_move(g.gen_move(g.g_map), Computer):
                    pass
                if g.check_win(g.g_map, g.last_move):
                    ComputerWins = True
                TableFull = g.check_table_full()
            turn += 1
            #g.cls()

        g.draw_table()
        if PlayerWins:
            print("You won this game")
        elif ComputerWins:
            print("Computer won this game")
        elif TableFull:
            print("No luck this time")
        start = input("\nWould you like to play again?[y/n]: ").lower()
