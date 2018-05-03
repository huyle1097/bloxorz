#!/usr/bin/python

import sys

########################################################################################################################
# Map description:
# 1 is putable, 0 is abyss, 4 is goal (So far so well)
# LEVEL_ARRAY = np.array([
# [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
# ])
# State: (x0,y0), (x1,y1)
# Horizontal object: (x, y), (x+1, y) or (x, y), (x, y+1).
# Vertical object: (x,y),(x,y)
# Goal state: isStand and map(y,x) = 4
########################################################################################################################

# LEVEL_ARRAY = np.array([
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
#     [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
# ])

import time

LEVEL1_ARRAY = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
]
LEVEL2_ARRAY = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 3, 1, 0, 0, 1, 4, 1],
    [1, 1, -3, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
]
LEVEL3_ARRAY = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]
LEVEL4_ARRAY = [
    [0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0],
    [0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 5, 5, 5, 5, 5],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 5, 5, 5, 5, 5],
    [0, 0, 0, 0, 0, 1, 4, 1, 0, 0, 5, 5, 1, 5],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 5, 5, 5, 5]
]
LEVEL5_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, -3, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, -2, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, -3],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

LEVEL6_ARRAY = [
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 4, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]
LEVEL7_ARRAY = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
]


########################################################################################################################
# Function map_copy. (Because python's deepcopy is extremely slow so I implement my own deepcopy)
########################################################################################################################
def map_copy(map):
    return [list(x) for x in map]


########################################################################################################################
# Data structure to store object's place, as well as its previous place and the action (up, down, left, right) to achieve it
# data: tuple (place)
# prev: Node (previous place)
# action: string (up, down, left, right)
# Created: SonPhan 23/04/2018
########################################################################################################################
class Node:
    def __init__(self, data=(0, 0, 0, 0), prev_node=None, action="", map=[], xo_objects_states={}):
        if not ((data[0] < data[2]) or ((data[0] == data[2]) and data[1] < data[3])):
            temp_data = (data[2], data[3], data[0], data[1])
            self.data = temp_data
        else:
            self.data = data
        self.prev_node = prev_node
        self.action = action
        self.map = map_copy(map)
        self.xo_objects_states = dict(xo_objects_states)

    def is_stand(self):
        return self.data[0] == self.data[2] and self.data[1] == self.data[3]


########################################################################################################################

class State:
    def __init__(self, start, board=LEVEL1_ARRAY, xo_objects=None):
        if xo_objects is None:
            xo_objects = []
        self.x0, self.y0, self.x1, self.y1 = start.data
        self.board = map_copy(board)
        self.states = [start]
        self.xo_objects = xo_objects
        self.visited = [start]

    # self.all_moves = self.next_position()

    ####################################################################################################################
    # Function to find all moves which can be reach from prev_node's move
    ####################################################################################################################
    def next_position(self, prev_node):
        rv = []
        if self.is_stand():
            # rv.append(Node((self.x0, self.y0 + 1, self.x1, self.y1 + 2), prev_node, "down", prev_node.map))
            # rv.append(Node((self.x0, self.y0 - 1, self.x0, self.y0 - 2), prev_node, "up", prev_node.map))
            # rv.append(Node((self.x0 + 1, self.y0, self.x0 + 2, self.y0), prev_node, "right", prev_node.map))
            # rv.append(Node((self.x0 - 1, self.y0, self.x0 - 2, self.y1), prev_node, "left", prev_node.map))
            self.add_move(rv, (self.x0, self.y0 + 1, self.x1, self.y1 + 2), prev_node, "down")
            self.add_move(rv, (self.x0, self.y0 - 1, self.x0, self.y0 - 2), prev_node, "up")
            self.add_move(rv, (self.x0 + 1, self.y0, self.x0 + 2, self.y0), prev_node, "right")
            self.add_move(rv, (self.x0 - 1, self.y0, self.x0 - 2, self.y1), prev_node, "left")
        elif self.x0 == self.x1:
            # rv.append(Node((self.x0 + 1, self.y0, self.x1 + 1, self.y1), prev_node, "right", prev_node.map))
            # rv.append(Node((self.x0 - 1, self.y0, self.x1 - 1, self.y1), prev_node, "left", prev_node.map))
            # rv.append(Node((self.x0, self.y0 - 1, self.x1, self.y1 - 2), prev_node, "up", prev_node.map))
            # rv.append(Node((self.x0, self.y0 + 2, self.x1, self.y1 + 1), prev_node, "down", prev_node.map))
            self.add_move(rv, (self.x0 + 1, self.y0, self.x1 + 1, self.y1), prev_node, "right")
            self.add_move(rv, (self.x0 - 1, self.y0, self.x1 - 1, self.y1), prev_node, "left")
            self.add_move(rv, (self.x0, self.y0 - 1, self.x1, self.y1 - 2), prev_node, "up")
            self.add_move(rv, (self.x0, self.y0 + 2, self.x1, self.y1 + 1), prev_node, "down")
        elif self.y0 == self.y1:
            # rv.append(Node((self.x0, self.y0 + 1, self.x1, self.y1 + 1), prev_node, "down", prev_node.map))
            # rv.append(Node((self.x0, self.y0 - 1, self.x1, self.y1 - 1), prev_node, "up", prev_node.map))
            # rv.append(Node((self.x0 - 1, self.y0, self.x1 - 2, self.y1), prev_node, "left", prev_node.map))
            # rv.append(Node((self.x0 + 2, self.y0, self.x1 + 1, self.y1), prev_node, "right", prev_node.map))
            self.add_move(rv, (self.x0, self.y0 + 1, self.x1, self.y1 + 1), prev_node, "down")
            self.add_move(rv, (self.x0, self.y0 - 1, self.x1, self.y1 - 1), prev_node, "up")
            self.add_move(rv, (self.x0 - 1, self.y0, self.x1 - 2, self.y1), prev_node, "left")
            self.add_move(rv, (self.x0 + 2, self.y0, self.x1 + 1, self.y1), prev_node, "right")
        else:
            return []
        return rv

    def add_move(self, rv, data, prev_node, direction):
        for xo_object in self.xo_objects:
            if (data[0] == xo_object.position[0] and data[1] == xo_object.position[1]) or (
                    data[2] == xo_object.position[0] and data[3] == xo_object.position[1]):
                for m in xo_object.managed_position:
                    if (xo_object.type == XOObject.TYPE_O) or (
                            xo_object.type == XOObject.TYPE_X and data[0] == data[2] and data[1] == data[3]):
                        if m.type == ManagedPosition.BOTH:
                            xo_objects_states = dict(prev_node.xo_objects_states)
                            xo_objects_states[(m.x, m.y)] = not xo_objects_states[(m.x, m.y)]
                            rv.append(Node(data, prev_node, direction, prev_node.map, xo_objects_states))
                        elif m.type == ManagedPosition.ONLY_ENABLE:
                            xo_objects_states = dict(prev_node.xo_objects_states)
                            xo_objects_states[(m.x, m.y)] = True
                            rv.append(Node(data, prev_node, direction, prev_node.map, xo_objects_states))
                        elif m.type == ManagedPosition.ONLY_DISABLE:
                            xo_objects_states = dict(prev_node.xo_objects_states)
                            xo_objects_states[(m.x, m.y)] = False
                            rv.append(Node(data, prev_node, direction, prev_node.map, xo_objects_states))
                return
        rv.append(Node(data, prev_node, direction, prev_node.map, prev_node.xo_objects_states))

    ####################################################################################################################
    # Function to check if the object repeated previous move (which could lead to infinite loop)
    # Created: SonPhan 23/04/2018
    ####################################################################################################################
    # def notContain(self, node):
    #     while prev:
    #         if node.data[0] == prev.data[0] and node.data[1] == prev.data[1] and node.data[2] == prev.data[2] \
    #                 and node.data[3] == prev.data[3]:
    #             if node.xo_objects_states == prev.xo_objects_states:
    #                 end = time.time()
    #                 return False
    #         prev = prev.prev_node
    #     return True
    def notContain(self, node):
        for n in self.visited:
            if n.data[0] == node.data[0] and n.data[1] == node.data[1] and n.data[2] == node.data[2] \
                    and n.data[3] == node.data[3]:
                if n.xo_objects_states == node.xo_objects_states:
                    return False
        return True

    ####################################################################################################################
    # Function to check valid move
    ####################################################################################################################
    # @staticmethod
    def is_valid(self, node):
        height = len(self.board)
        width = len(self.board[0])
        if node.data[0] < 0 or node.data[0] >= width or node.data[1] < 0 or node.data[1] >= height \
                or node.data[2] < 0 or node.data[2] >= width or node.data[3] < 0 or node.data[3] >= height:
            return False
        if node.map[node.data[1]][node.data[0]] == 0 or node.map[node.data[3]][
            node.data[2]] == 0:
            return False
        if node.data[0] == node.data[2] and node.data[1] == node.data[3] and node.map[node.data[1]][node.data[0]] == 5:
            return False
        return True

    def add_state(self, node):
        if self.notContain(node):
            self.visited.append(node)
            self.states.append(node)
            return True
        return False

    def add_valid_state(self, prev_node):
        list_node = self.next_position(prev_node)
        if not list_node:
            return False
        else:
            for node in list_node:
                if self.is_valid(node):
                    self.add_state(node)

    def is_goal(self, x, y):
        return self.board[y][x] == 4

    def is_stand(self):
        return self.x0 == self.x1 and self.y0 == self.y1

    def check_goal(self):
        return self.is_stand() and self.is_goal(self.x0, self.y0)

    def set_player_position(self, node):
        self.x0, self.y0, self.x1, self.y1 = node.data
        for xo_object in self.xo_objects:
            if (self.x0 == xo_object.position[0] and self.y0 == xo_object.position[1]) or (
                    self.x1 == xo_object.position[0] and self.y1 == xo_object.position[1]):
                for m in xo_object.managed_position:
                    if xo_object.type == XOObject.TYPE_O or (xo_object.type == XOObject.TYPE_X and self.is_stand()):
                        if m.type == ManagedPosition.BOTH:
                            node.map[m.y][m.x] = abs(node.map[m.y][m.x] - 1)
                        elif m.type == ManagedPosition.ONLY_ENABLE:
                            node.map[m.y][m.x] = 1
                        elif m.type == ManagedPosition.ONLY_DISABLE:
                            node.map[m.y][m.x] = 0


class XOObject:
    TYPE_O = -1000
    TYPE_X = 1000

    def __init__(self, type, position=(0, 0), managed_position=[]):
        self.type = type
        self.position = position
        self.managed_position = managed_position


class ManagedPosition:
    ONLY_ENABLE = 123
    ONLY_DISABLE = -123
    BOTH = 12

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type


########################################################################################################################
# Function to solve by bfs
########################################################################################################################
def bfs(state):
    # start = time.time()
    current_state = Node
    # BFS operation
    while len(state.states) != 0:
        # print(len(state.states))
        current_state = state.states.pop(0)
        state.set_player_position(current_state)
        if state.check_goal():
            break
        state.add_valid_state(current_state)
    pointer = current_state
    path = []
    # Backtracking all the previous moves to reach this goal state
    while pointer:
        path.insert(0, pointer.action)
        pointer = pointer.prev_node
    # And print them out
    for action in path:
        print(action)
    # end = time.time()
    # print(end - start)


def main():
    # LEVEL1 SOLVER:
    # state = State(Node((1, 1, 1, 1), None, "", LEVEL1_ARRAY), LEVEL1_ARRAY)

    # LEVEL2 SOLVER:
    # xo_objects = [
    #     XOObject(XOObject.TYPE_O, (2, 2),
    #              [ManagedPosition(4, 4, ManagedPosition.BOTH), ManagedPosition(5, 4, ManagedPosition.BOTH)]),
    #     XOObject(XOObject.TYPE_X, (8, 1),
    #              [ManagedPosition(10, 4, ManagedPosition.BOTH), ManagedPosition(11, 4, ManagedPosition.BOTH)])]
    # state = State(
    #     Node((1, 4, 1, 4), None, "", LEVEL2_ARRAY, {(4, 4): False, (5, 4): False, (10, 4): False, (11, 4): False}),
    #     LEVEL2_ARRAY, xo_objects)

    # LEVEL3 SOLVER:
    # state = State(Node((1, 3, 1, 3), None, "", LEVEL3_ARRAY), LEVEL3_ARRAY)

    # LEVEL4 SOLVER:
    # state = State(Node((1, 5, 1, 5), None, "", LEVEL4_ARRAY), LEVEL4_ARRAY)

    # Level 5 Solver :
    xo_objects = [XOObject(XOObject.TYPE_O, (8, 1),
                           [ManagedPosition(5, 1, ManagedPosition.BOTH), ManagedPosition(6, 1, ManagedPosition.BOTH)]),
                  XOObject(XOObject.TYPE_O, (3, 3), [ManagedPosition(5, 8, ManagedPosition.ONLY_ENABLE),
                                                     ManagedPosition(6, 8, ManagedPosition.ONLY_ENABLE)]),
                  XOObject(XOObject.TYPE_O, (6, 5), [ManagedPosition(5, 8, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(6, 8, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_O, (14, 6), [
                      ManagedPosition(5, 8, ManagedPosition.BOTH), ManagedPosition(6, 8, ManagedPosition.BOTH)])]
    state = State(
        Node((13, 1, 13, 1), None, "", LEVEL5_ARRAY, {(5, 1): True, (6, 1): True, (5, 8): True, (6, 8): True}),
        LEVEL5_ARRAY, xo_objects)

    # LEVEL6 SOLVER:
    # state = State(Node((0, 3, 0, 3), None, "", LEVEL6_ARRAY), LEVEL6_ARRAY)

    bfs(state)


main()
