# -*- coding: utf-8 -*-
from copy import deepcopy

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
        return str(other) == self._name

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

    def move(self, angle):
        assert isinstance(angle, int)
        assert angle in self.valid_angle

        temp = deepcopy(self._face)

        if angle == self.valid_angle[0]:
            for i in range(3):
                for j in range(3):
                    self._face[j][2-i] = temp[i][j]
        elif angle == self.valid_angle[1]:
            for i in range(3):
                for j in range(3):
                    self._face[2-i][2-j] = temp[i][j]
        elif angle == self.valid_angle[2]:
            for i in range(3):
                for j in range(3):
                    self._face[2-j][i] = temp[i][j]
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

    def get_valid_command(self):
        return self._valid_command

    def move(self, command):
        assert isinstance(command, str)
        assert command in self._valid_command

        c1 = command[0]
        c2 = command[-1]

        face = self._faces.get(c1)
        u = self._faces.get("U").get_face()
        du = deepcopy(u)
        l = self._faces.get("L").get_face()
        dl = deepcopy(l)
        r = self._faces.get("R").get_face()
        dr = deepcopy(r)
        d = self._faces.get("D").get_face()
        dd = deepcopy(d)
        f = self._faces.get("F").get_face()
        df = deepcopy(f)
        b = self._faces.get("B").get_face()
        db = deepcopy(b)

        if c1 == "F":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    u[2][i] = dr[i][0]
                    r[i][0] = dd[0][2-i]
                    d[0][2-i] = dl[2-i][2]
                    l[2-i][2] = du[2][i]
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    u[2][i] = dd[0][2-i]
                    d[0][2-i] = du[2][i]
                    r[i][0] = dl[2-i][2]
                    l[2-i][2] = dr[i][0]
            else:
                face.move(90)
                for i in range(3):
                    u[2][i] = dl[2-i][2]
                    l[2-i][2] = dd[0][2-i]
                    d[0][2-i] = dr[i][0]
                    r[i][0] = du[2][i]
        elif c1 == "U":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    b[2][2-i] = dr[0][i]
                    r[0][i] = df[0][i]
                    f[0][i] = dl[0][i]
                    l[0][i] = db[2][2-i]
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    b[2][2-i] = df[0][i]
                    f[0][i] = db[2][2-i]
                    l[0][i] = dr[0][i]
                    r[0][i] = dl[0][i]
            else:
                face.move(90)
                for i in range(3):
                    b[2][2-i] = dl[0][i]
                    l[0][i] = df[0][i]
                    f[0][i] = dr[0][i]
                    r[0][i] = db[2][2-i]
        elif c1 == "D":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    f[2][i] = dr[2][i]
                    r[2][i] = db[0][2-i]
                    b[0][2-i] = dl[2][i]
                    l[2][i] = df[2][i]
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    f[2][i] = db[0][2-i]
                    b[0][2-i] = df[2][i]
                    l[2][i] = dr[2][i]
                    r[2][i] = dl[2][i]
            else:
                face.move(90)
                for i in range(3):
                    f[2][i] = dl[2][i]
                    l[2][i] = db[0][2-i]
                    b[0][2-i] = dr[2][i]
                    r[2][i] = df[2][i]
        elif c1 == "B":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    u[0][i] = dl[2-i][0]
                    l[2-i][0] = dd[2][2-i]
                    d[2][2-i] = dr[i][2]
                    r[i][2] = du[0][i]
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    u[0][i] = dd[2][2-i]
                    d[2][2-i] = du[0][i]
                    l[2-i][0] = dr[i][2]
                    r[i][2] = dl[2-i][0]
            else:
                face.move(90)
                for i in range(3):
                    u[0][i] = dr[i][2]
                    r[i][2] = dd[2][2-i]
                    d[2][2-i] = dl[2-i][0]
                    l[2-i][0] = du[0][i]
        elif c1 == "L":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    u[i][0] = df[i][0]
                    f[i][0] = dd[i][0]
                    d[i][0] = db[i][0]
                    b[i][0] = du[i][0]
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    u[i][0] = dd[i][0]
                    f[i][0] = db[i][0]
                    d[i][0] = du[i][0]
                    b[i][0] = df[i][0]
            else:
                face.move(90)
                for i in range(3):
                    u[i][0] = db[i][0]
                    f[i][0] = du[i][0]
                    d[i][0] = df[i][0]
                    b[i][0] = dd[i][0]
        elif c1 == "R":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(3):
                    u[i][2] = db[i][2]
                    b[i][2] = dd[i][2]
                    d[i][2] = df[i][2]
                    f[i][2] = du[i][2]
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(3):
                    u[i][2] = dd[i][2]
                    b[i][2] = df[i][2]
                    d[i][2] = du[i][2]
                    f[i][2] = db[i][2]
            else:
                face.move(90)
                for i in range(3):
                    u[i][2] = df[i][2]
                    b[i][2] = du[i][2]
                    d[i][2] = db[i][2]
                    f[i][2] = dd[i][2]
        else:
            assert False


    pass

if __name__ == "__main__":
    r = Color("red")
    g = Color("green")
    w = Color("white")
    b = Color("blue")
    y = Color("yellow")
    o = Color("orange")

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
    while True:
        string = raw_input()
        if string == 'q':
            break
        for ss in string.split():
            s.move(ss)
        print s


