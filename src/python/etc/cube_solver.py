# -*- coding: utf-8 -*-
from copy import deepcopy
from sys import getsizeof

# 코딩 중
# state 바꿀 때 이전 행동의 역행동은 하지 않기
# tree 타고 올라가면서 parents 중에 하나랑 같으면 지워버리기


class Color:
    """One of the color of the Cube"""
    valid_colors = ("red", "blue", "yellow", "green", "white", "orange")

    def __init__(self, name=""):
        assert name in self.valid_colors
        self._name = name

    def __eq__(self, other):
        assert isinstance(other, Color)
        return str(other).strip() == self._name

    def __str__(self):
        return "%-8s" % self._name

    pass


class Face:
    """The color distribution of a face of the Cube"""

    valid_angle=[90, 180, 270]

    def __init__(self, colors=()):
        assert isinstance(colors, tuple)
        assert len(colors) == 9

        for idx, item in enumerate(colors):
            assert isinstance(item, Color)

        self._face = []
        self._face.append(list(colors[:3]))
        self._face.append(list(colors[3:6]))
        self._face.append(list(colors[6:9]))

    def __str__(self):
        s = ""
        for r in range(3):
            for c in range(3):
                s += "%s" % str(self._face[r][c])
            s += "\n"
        return s.rstrip("\n")

    def get_face(self):
        return self._face

    def get_center_color(self):
        return self._face[1][1]

    def is_matched(self):
        temp = self.get_center_color()
        flag = True
        for row in self._face:
            for color in row:
                flag = flag and (color == temp)
        return flag

    def move(self, angle):
        assert isinstance(angle, int)
        assert angle in self.valid_angle

        # temp = deepcopy(self._face)
        t = self._face

        if angle == self.valid_angle[0]:
            c = t[0][0]
            e = t[0][1]
            t[0][0] = t[2][0]
            t[2][0] = t[2][2]
            t[2][2] = t[0][2]
            t[0][2] = c
            t[0][1] = t[1][0]
            t[1][0] = t[2][1]
            t[2][1] = t[1][2]
            t[1][2] = e
        elif angle == self.valid_angle[1]:
            t[0][0], t[2][2] = t[2][2], t[0][0]
            t[0][2], t[2][0] = t[2][0], t[0][2]
            t[0][1], t[2][1] = t[2][1], t[0][1]
            t[1][0], t[1][2] = t[1][2], t[1][0]
        elif angle == self.valid_angle[2]:
            c = t[0][0]
            e = t[0][1]
            t[0][0] = t[0][2]
            t[0][2] = t[2][2]
            t[2][2] = t[2][0]
            t[2][0] = c
            t[0][1] = t[1][2]
            t[1][2] = t[2][1]
            t[2][1] = t[1][0]
            t[1][0] = e
        else:
            assert False

    pass


class State:
    """A state of the Cube"""

    valid_face = "UuLlFfRrDdBb"
    valid_command0 = "ULFRDB"
    valid_command1 = "'2"

    def __init__(self, faces=()):
        assert isinstance(faces, tuple)
        assert len(faces) == 6

        self._faces = {}
        for idx, item in enumerate(faces):
            assert isinstance(item, Face)
            self._faces[self.valid_face[idx*2]] = item

        self._valid_command = []
        for v1 in self.valid_command0:
            self._valid_command.append(v1)
            for v2 in self.valid_command1:
                self._valid_command.append(v1+v2)

    def __str__(self):
        tab = " "*8*3
        s = ""

        for row in str(self._faces.get("U")).split("\n"):
            s += "%s%s\n" % (tab, row)

        temp = str(self._faces.get("L")).split("\n")
        for idx, item in enumerate(
                str(self._faces.get("F")).split("\n")):
            temp[idx] += "%s" % item
        for idx, item in enumerate(
                str(self._faces.get("R")).split("\n")):
            temp[idx] += "%s" % item
        for t in temp:
            s += "%s\n" % t

        for row in str(self._faces.get("D")).split("\n"):
            s += "%s%s\n" % (tab, row)

        for row in str(self._faces.get("B")).split("\n"):
            s += "%s%s\n" % (tab, row)

        return s

    def get_face(self, face="F"):
        assert isinstance(face, str)
        assert face in self.valid_face
        assert len(face) == 1

        face = face.capitalize()
        return str(self._faces[face])

    def is_solved(self):
        """each face has the same color."""
        flag = True
        for face in self._faces.itervalues():
            # print face
            flag = flag and face.is_matched()
        return flag

    def get_valid_command(self):
        return self._valid_command

    def inverse_move(self, command):
        assert isinstance(command, str)
        assert command in self._valid_command, command

        c1 = command[0]
        c2 = command[-1]

        if c2 == self.valid_command1[0]:
            c2 = ""
        elif c2 in self.valid_command0:
            c2 = "'"
        self.move(c1+c2)

    def move(self, command):
        assert isinstance(command, str)
        assert command in self._valid_command, command

        c1 = command[0]
        c2 = command[-1]

        face = self._faces.get(c1)
        u = self._faces.get("U").get_face()
        # du = deepcopy(u)
        l = self._faces.get("L").get_face()
        # dl = deepcopy(l)
        r = self._faces.get("R").get_face()
        # dr = deepcopy(r)
        d = self._faces.get("D").get_face()
        # dd = deepcopy(d)
        f = self._faces.get("F").get_face()
        # df = deepcopy(f)
        b = self._faces.get("B").get_face()
        # db = deepcopy(b)

        if c1 == "F":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    temp = u[2][i]
                    u[2][i] = r[i][0]
                    r[i][0] = d[0][2-i]
                    d[0][2-i] = l[2-i][2]
                    l[2-i][2] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    u[2][i], d[0][2-i] = d[0][2-i], u[2][i]
                    r[i][0], l[2-i][2] = l[2-i][2], r[i][0]
            else:
                face.move(90)
                for i in range(3):
                    temp = u[2][i]
                    u[2][i] = l[2-i][2]
                    l[2-i][2] = d[0][2-i]
                    d[0][2-i] = r[i][0]
                    r[i][0] = temp
        elif c1 == "U":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    temp = b[2][2-i]
                    b[2][2-i] = r[0][i]
                    r[0][i] = f[0][i]
                    f[0][i] = l[0][i]
                    l[0][i] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    b[2][2-i], f[0][i] = f[0][i], b[2][2-i]
                    l[0][i], r[0][i] = r[0][i], l[0][i]
            else:
                face.move(90)
                for i in range(3):
                    temp = b[2][2-i]
                    b[2][2-i] = l[0][i]
                    l[0][i] = f[0][i]
                    f[0][i] = r[0][i]
                    r[0][i] = temp
        elif c1 == "D":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    temp = f[2][i]
                    f[2][i] = r[2][i]
                    r[2][i] = b[0][2-i]
                    b[0][2-i] = l[2][i]
                    l[2][i] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    f[2][i], b[0][2-i] = b[0][2-i], f[2][i]
                    l[2][i], r[2][i] = r[2][i], l[2][i]
            else:
                face.move(90)
                for i in range(3):
                    temp = f[2][i]
                    f[2][i] = l[2][i]
                    l[2][i] = b[0][2-i]
                    b[0][2-i] = r[2][i]
                    r[2][i] = temp
        elif c1 == "B":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    temp = u[0][i]
                    u[0][i] = l[2-i][0]
                    l[2-i][0] = d[2][2-i]
                    d[2][2-i] = r[i][2]
                    r[i][2] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    u[0][i], d[2][2-i] = d[2][2-i], u[0][i]
                    l[2-i][0], r[i][2] = r[i][2], l[2-i][0]
            else:
                face.move(90)
                for i in range(3):
                    temp = u[0][i]
                    u[0][i] = r[i][2]
                    r[i][2] = d[2][2-i]
                    d[2][2-i] = l[2-i][0]
                    l[2-i][0] = temp
        elif c1 == "L":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    temp = u[i][0]
                    u[i][0] = f[i][0]
                    f[i][0] = d[i][0]
                    d[i][0] = b[i][0]
                    b[i][0] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    u[i][0], d[i][0] = d[i][0], u[i][0]
                    f[i][0], b[i][0] = b[i][0], f[i][0]
            else:
                face.move(90)
                for i in range(3):
                    temp = u[i][0]
                    u[i][0] = b[i][0]
                    b[i][0] = d[i][0]
                    d[i][0] = f[i][0]
                    f[i][0] = temp
        elif c1 == "R":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    temp = u[i][2]
                    u[i][2] = b[i][2]
                    b[i][2] = d[i][2]
                    d[i][2] = f[i][2]
                    f[i][2] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    u[i][2], d[i][2] = d[i][2], u[i][2]
                    f[i][2], b[i][2] = b[i][2], f[i][2]
            else:
                face.move(90)
                for i in range(3):
                    temp = u[i][2]
                    u[i][2] = f[i][2]
                    f[i][2] = d[i][2]
                    d[i][2] = b[i][2]
                    b[i][2] = temp

        else:
            assert False
    pass


class Solver:
    """Cube Solver"""

    def __init__(self, state=None):
        assert isinstance(state, State) or state is None

        self._cube = state
        self._valid_command = state.get_valid_command()
        self._ans = ""
        self._U = self._valid_command[:3]
        self._L = self._valid_command[3:6]
        self._F = self._valid_command[6:9]
        self._R = self._valid_command[9:12]
        self._D = self._valid_command[12:15]
        self._B = self._valid_command[15:18]
        self._UD = self._U + self._D
        self._FB = self._F + self._B
        self._LR = self._L + self._R
        self._UD_after = self._L + self._F + self._R + self._B
        self._LR_after = self._U + self._F + self._D + self._B
        self._FB_after = self._L + self._U + self._R + self._D
        print self._UD_after
        print self._LR_after
        print self._FB_after

    def __str__(self):
        return str(self._cube)

    def get_answer(self):
        if self._ans == "":
            return self.solve_without_memory()
        assert self._cube.is_solved()
        return self._ans

    def solve_without_memory(self):
        sequence = [None]
        cube = self._cube
        while True:
            temp = []
            for t in sequence:
                # cube = deepcopy(self._cube)
                if t:
                    for command in t:
                        cube.move(command)

                last_command = ""
                second_last_command = ""
                if t and len(t) > 0:
                    last_command = t[-1]
                    if len(t) > 1:
                        second_last_command = t[-2]

                if last_command in self._UD:
                    try_command = self._UD_after[:]
                    if last_command in self._U:
                        if second_last_command not in self._UD:
                            try_command += self._D
                    else:
                        if second_last_command not in self._UD:
                            try_command += self._U
                elif last_command in self._FB:
                    try_command = self._FB_after[:]
                    if last_command in self._F:
                        if second_last_command not in self._FB:
                            try_command += self._B
                    else:
                        if second_last_command not in self._FB:
                            try_command += self._F
                elif last_command in self._LR:
                    try_command = self._LR_after[:]
                    if last_command in self._L:
                        if second_last_command not in self._LR:
                            try_command += self._R
                    else:
                        if second_last_command not in self._LR:
                            try_command += self._L
                else:
                    try_command = self._valid_command

                for command in try_command:
                    # temp_cube = deepcopy(cube)
                    cube.move(command)
                    if t:
                        tried = t+[command]
                    else:
                        tried = [command]
                    temp.append(tried)
                    # print "tried: ", tried
                    if cube.is_solved():
                        self._ans = " ".join(tried)
                        print "finish", len(sequence), len(try_command)
                        return self._ans
                    elif tried == ['U2', 'D', 'R']:
                        print cube
                        return
                    cube.inverse_move(command)
                if t:
                    for command in t:
                        cube.inverse_move(command)
            sequence = temp

    def solve_with_memory(self):
        sequence = [None]
        while True:
            temp = []
            for t in sequence:
                if t:
                    cube = t[0]
                else:
                    cube = deepcopy(self._cube)

                last_command = ""
                second_last_command = ""
                if t and len(t[1]) > 0:
                    last_command = t[1][-1]
                    if len(t[1]) > 1:
                        second_last_command = t[1][-2]

                if last_command in self._UD:
                    try_command = self._UD_after[:]
                    if last_command in self._U:
                        if second_last_command not in self._UD:
                            try_command += self._D
                    else:
                        if second_last_command not in self._UD:
                            try_command += self._U
                elif last_command in self._FB:
                    try_command = self._FB_after[:]
                    if last_command in self._F:
                        if second_last_command not in self._FB:
                            try_command += self._B
                    else:
                        if second_last_command not in self._FB:
                            try_command += self._F
                elif last_command in self._LR:
                    try_command = self._LR_after[:]
                    if last_command in self._L:
                        if second_last_command not in self._LR:
                            try_command += self._R
                    else:
                        if second_last_command not in self._LR:
                            try_command += self._L
                else:
                    try_command = self._valid_command

                for command in try_command:
                    temp_cube = deepcopy(cube)
                    if t:
                        tried = t[1] + [command]
                    else:
                        tried = [command]
                    temp_cube.move(command)
                    temp.append((temp_cube, tried))
                    # print "tried: ", tried
                    if temp_cube.is_solved():
                        self._ans = " ".join(tried)
                        print "finish", len(sequence), len(try_command)
                        return self._ans
                    elif tried == ['R2', 'L', 'U2', 'D', 'R']:
                        print temp_cube
                        return
                    # del temp_cube
                # print "fail"
                del cube
            del sequence
            sequence = temp
            # print sequence


def user_test(state=None):
    assert state is not None
    while True:
        string = raw_input("input sequence >>> ")
        if string == 'q':
            break
        for s in string.split():
            state.move(s)
        print state

if __name__ == "__main__":
    r = Color("red")
    g = Color("green")
    w = Color("white")
    b = Color("blue")
    y = Color("yellow")
    o = Color("orange")

    lst = []
    for i in range(9):
        lst.append(deepcopy(r))
    lst = tuple(lst)
    r_all = Face(lst)

    lst = []
    for i in range(9):
        lst.append(deepcopy(g))
    lst = tuple(lst)
    g_all = Face(lst)

    lst = []
    for i in range(9):
        lst.append(deepcopy(w))
    lst = tuple(lst)
    w_all = Face(lst)

    lst = []
    for i in range(9):
        lst.append(deepcopy(b))
    lst = tuple(lst)
    b_all = Face(lst)

    lst = []
    for i in range(9):
        lst.append(deepcopy(y))
    lst = tuple(lst)
    y_all = Face(lst)

    lst = []
    for i in range(9):
        lst.append(deepcopy(o))
    lst = tuple(lst)
    o_all = Face(lst)

    lst = []
    lst.append(deepcopy(w))
    lst.append(deepcopy(o))
    lst.append(deepcopy(o))
    lst.append(deepcopy(g))
    lst.append(deepcopy(r))
    lst.append(deepcopy(w))
    lst.append(deepcopy(w))
    lst.append(deepcopy(o))
    lst.append(deepcopy(g))
    lst = tuple(lst)
    F = Face(lst)

    lst = []
    lst.append(deepcopy(w))
    lst.append(deepcopy(o))
    lst.append(deepcopy(b))
    lst.append(deepcopy(g))
    lst.append(deepcopy(y))
    lst.append(deepcopy(y))
    lst.append(deepcopy(r))
    lst.append(deepcopy(g))
    lst.append(deepcopy(g))
    lst = tuple(lst)
    U = Face(lst)

    lst = []
    lst.append(deepcopy(o))
    lst.append(deepcopy(r))
    lst.append(deepcopy(b))
    lst.append(deepcopy(r))
    lst.append(deepcopy(b))
    lst.append(deepcopy(w))
    lst.append(deepcopy(g))
    lst.append(deepcopy(y))
    lst.append(deepcopy(g))
    lst = tuple(lst)
    L = Face(lst)

    lst = []
    lst.append(deepcopy(y))
    lst.append(deepcopy(r))
    lst.append(deepcopy(r))
    lst.append(deepcopy(b))
    lst.append(deepcopy(g))
    lst.append(deepcopy(g))
    lst.append(deepcopy(r))
    lst.append(deepcopy(o))
    lst.append(deepcopy(b))
    lst = tuple(lst)
    R = Face(lst)

    lst = []
    lst.append(deepcopy(r))
    lst.append(deepcopy(y))
    lst.append(deepcopy(y))
    lst.append(deepcopy(b))
    lst.append(deepcopy(w))
    lst.append(deepcopy(w))
    lst.append(deepcopy(o))
    lst.append(deepcopy(r))
    lst.append(deepcopy(y))
    lst = tuple(lst)
    D = Face(lst)

    lst = []
    lst.append(deepcopy(w))
    lst.append(deepcopy(b))
    lst.append(deepcopy(o))
    lst.append(deepcopy(w))
    lst.append(deepcopy(o))
    lst.append(deepcopy(y))
    lst.append(deepcopy(b))
    lst.append(deepcopy(b))
    lst.append(deepcopy(y))
    lst = tuple(lst)
    B = Face(lst)

    lst = (U, L, F, R, D, B)
    s = State(lst)

    lst = (w_all, g_all, r_all, b_all, y_all, o_all)
    cube = State(lst)

    """
    print r
    print
    print s
    print
    print F
    print
    F.move(90)
    print F
    print "asdf"
    print
    F.move(180)
    print F
    print "asdf"
    print
    F.move(270)
    print F
    print "asdf"
    F.move(180)
    print s.get_face("F")
    print s.get_face("U")
    print s.get_face("B")
    print s.get_face("L")
    print s.get_face("R")
    print s
    print
    """
    # user_test(s)

    print "start"
    print cube
    string = "R' D' U2"
    for ss in string.split():
        cube.move(ss)
    print cube
    # user_test(cube)

    solver = Solver(cube)
    print solver
    print getsizeof(cube)
    print getsizeof(solver)

    print solver.get_answer()
    """
    for i in range(10000):
        cc = deepcopy(cube)
        cube.move('R')
    print 'done'
    """

