from sys import getsizeof
from random import choice
from time import time

class Color:
    """One of the colors of the Cube"""
    valid_colors = ("red", "blue", "yellow", "green", "white", "orange")

    def __init__(self, name):
        assert name in self.valid_colors, "color name:[%s] is not valid" % str(name)
        self._name = name

    def __eq__(self, other):
        assert isinstance(other, Color), "color:[%s] is not class Color" % other.__class__.__name__
        return self._name == str(other).strip()

    def __str__(self):
        return self._name

    pass


class Face2:
    """The color allocation of a face of 2x2x2 Cube"""

    valid_angle=[90, 180, 270]

    def __init__(self, colors=()):
        assert isinstance(colors, tuple)
        assert len(colors) == 4
        for idx, item in enumerate(colors):
            assert isinstance(item, Color)

        self._face = []
        self._face.append(list(colors[:2]))
        self._face.append(list(colors[2:4]))

    def __str__(self):
        s = ""
        for r in range(2):
            for c in range(2):
                s += "%-8s" % str(self._face[r][c])
            s += "\n"
        return s.rstrip("\n")

    def get_face(self):
        return self._face

    def is_matched(self):
        temp = self._face[0][0]
        flag = True
        for row in self._face:
            for color in row:
                flag = flag and (color == temp)
        return flag

    def move(self, angle):
        assert isinstance(angle, int)
        assert angle in self.valid_angle

        t = self._face

        if angle == self.valid_angle[0]:
            c = t[0][0]
            t[0][0] = t[1][0]
            t[1][0] = t[1][1]
            t[1][1] = t[0][1]
            t[0][1] = c
        elif angle == self.valid_angle[1]:
            t[0][0], t[1][1] = t[1][1], t[0][0]
            t[0][1], t[1][0] = t[1][0], t[0][1]
        elif angle == self.valid_angle[2]:
            c = t[0][0]
            t[0][0] = t[0][1]
            t[0][1] = t[1][1]
            t[1][1] = t[1][0]
            t[1][0] = c
        else:
            assert False
    pass


class Face3:
    """The color distribution of a face of the 3x3x3 Cube"""

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
                s += "%-8s" % str(self._face[r][c])
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


class State2:
    """A state of the 2x2x2 Cube"""

    valid_face = "UuLlFfRrDdBb"
    valid_command0 = "UFR"
    valid_command1 = "'2"

    def __init__(self, faces=()):
        assert isinstance(faces, tuple)
        assert len(faces) == 6

        self._faces = {}
        for idx, item in enumerate(faces):
            assert isinstance(item, Face2), "Face2 is required"
            self._faces[self.valid_face[idx*2]] = item

        self._valid_command = []
        for v1 in self.valid_command0:
            self._valid_command.append(v1)
            for v2 in self.valid_command1:
                self._valid_command.append(v1+v2)

    def __str__(self):
        tab = " "*8*2
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
        return str(self._faces.get(face))

    def is_solved(self):
        """Each face must have the same color."""
        flag = True
        for face in self._faces.itervalues():
            flag = flag and face.is_matched()
        return flag

    def get_valid_command(self):
        return self._valid_command

    def inverse_move(self, command):
        assert isinstance(command, str)
        assert command in self._valid_command, "%s is not vaild" % command

        c1 = command[0]
        c2 = command[-1]

        if c2 == self.valid_command1[0]:
            c2 = ""
        elif c2 in self.valid_command0:
            c2 = "'"
        self.move(c1+c2)

    def move(self, command):
        assert isinstance(command, str)
        assert command in self._valid_command, "%s is not vaild" % command

        c1 = command[0]
        c2 = command[-1]

        face = self._faces.get(c1)
        u = self._faces.get("U").get_face()
        l = self._faces.get("L").get_face()
        r = self._faces.get("R").get_face()
        d = self._faces.get("D").get_face()
        f = self._faces.get("F").get_face()
        b = self._faces.get("B").get_face()

        if c1 == "F":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(2):
                    temp = u[1][i]
                    u[1][i] = r[i][0]
                    r[i][0] = d[0][1-i]
                    d[0][1-i] = l[1-i][1]
                    l[1-i][1] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(2):
                    u[1][i], d[0][1-i] = d[0][1-i], u[1][i]
                    r[i][0], l[1-i][1] = l[1-i][1], r[i][0]
            else:
                face.move(90)
                for i in range(2):
                    temp = u[1][i]
                    u[1][i] = l[1-i][1]
                    l[1-i][1] = d[0][1-i]
                    d[0][1-i] = r[i][0]
                    r[i][0] = temp
        elif c1 == "U":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(2):
                    temp = b[1][1-i]
                    b[1][1-i] = r[0][i]
                    r[0][i] = f[0][i]
                    f[0][i] = l[0][i]
                    l[0][i] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(2):
                    b[1][1-i], f[0][i] = f[0][i], b[1][1-i]
                    l[0][i], r[0][i] = r[0][i], l[0][i]
            else:
                face.move(90)
                for i in range(2):
                    temp = b[1][1-i]
                    b[1][1-i] = l[0][i]
                    l[0][i] = f[0][i]
                    f[0][i] = r[0][i]
                    r[0][i] = temp
        elif c1 == "R":
            if c2 == self.valid_command1[0]:
                face.move(270)
                for i in range(2):
                    temp = u[i][1]
                    u[i][1] = b[i][1]
                    b[i][1] = d[i][1]
                    d[i][1] = f[i][1]
                    f[i][1] = temp
            elif c2 == self.valid_command1[1]:
                face.move(180)
                for i in range(2):
                    u[i][1], d[i][1] = d[i][1], u[i][1]
                    f[i][1], b[i][1] = b[i][1], f[i][1]
            else:
                face.move(90)
                for i in range(2):
                    temp = u[i][1]
                    u[i][1] = f[i][1]
                    f[i][1] = d[i][1]
                    d[i][1] = b[i][1]
                    b[i][1] = temp
        else:
            assert False
    pass


class State3:
    """A state of the 3x3x3 Cube"""

    valid_face = "UuLlFfRrDdBb"
    valid_command0 = "ULFRDB"
    valid_command1 = "'2"

    def __init__(self, faces=()):
        assert isinstance(faces, tuple)
        assert len(faces) == 6

        self._faces = {}
        for idx, item in enumerate(faces):
            assert isinstance(item, Face3)
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
        l = self._faces.get("L").get_face()
        r = self._faces.get("R").get_face()
        d = self._faces.get("D").get_face()
        f = self._faces.get("F").get_face()
        b = self._faces.get("B").get_face()

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


class Solver2:
    """2x2x2 Cube Solver"""

    def __init__(self, state):
        assert isinstance(state, State2), "State2 is required"

        self._cube = state
        self._valid_command = state.get_valid_command()
        self._ans = ""
        self._U = self._valid_command[:3]
        self._F = self._valid_command[3:6]
        self._R = self._valid_command[6:9]
        self._U_after = self._F + self._R
        self._F_after = self._U + self._R
        self._R_after = self._U + self._F

    def __str__(self):
        return str(self._cube)

    def get_answer(self):
        if self._ans == "":
            return self.solve_without_memory()
        assert self._cube.is_solved()
        return self._ans

    def solve_without_memory(self):
        sequence = [False]
        cube = self._cube
        while True:
            temp = []
            for t in sequence:
                if t:
                    for command in t:
                        cube.move(command)

                last_command = ""
                second_last_command = ""
                if t and len(t) > 0:
                    last_command = t[-1]

                if last_command in self._U:
                    try_command = self._U_after
                elif last_command in self._F:
                    try_command = self._F_after
                elif last_command in self._R:
                    try_command = self._R_after
                else:
                    try_command = self._valid_command

                for command in try_command:
                    cube.move(command)
                    if t:
                        tried = t+[command]
                    else:
                        tried = [command]
                    temp.append(tried)
                    if cube.is_solved():
                        self._ans = " ".join(tried)
                        print "finish", len(sequence), len(try_command)
                        return self._ans
                    cube.inverse_move(command)
                if t:
                    t.reverse()
                    for command in t:
                        cube.inverse_move(command)
            sequence = temp

    def scremble(self, num=20):
        assert isinstance(num, int)
        sequence = [choice(self._valid_command)]    # random.choice
        cube = self._cube
        for i in range(num-1):
            if sequence[-1] in self._U:
                sequence.append(choice(self._U_after))
            elif sequence[-1] in self._F:
                sequence.append(choice(self._F_after))
            elif sequence[-1] in self._R:
                sequence.append(choice(self._R_after))
            else:
                sequence.append(choice(self._valid_command))
        
        for t in sequence:
            cube.move(t)

        return " ".join(sequence)
    pass


class Solver3:
    """3x3x3 Cube Solver"""

    def __init__(self, state):
        assert isinstance(state, State), "State3 is required"

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
        sequence = [False]
        cube = self._cube
        while True:
            temp = []
            for t in sequence:
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
                    cube.move(command)
                    if t:
                        tried = t+[command]
                    else:
                        tried = [command]
                    temp.append(tried)
                    if cube.is_solved():
                        self._ans = " ".join(tried)
                        print "finish", len(sequence), len(try_command)
                        return self._ans
                    elif tried == ['B', 'R2', 'L', 'U2', 'D', 'R']:
                        print cube
                        return 
                    cube.inverse_move(command)
                if t:
                    t.reverse()
                    for command in t:
                        cube.inverse_move(command)
            sequence = temp

    """
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
    """

def user_test(state):
    assert isinstance(state, State3) or isinstance(state, State2), "State2 or State3 is required"
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
    for i in range(4):
        lst.append(r)
    lst = tuple(lst)
    r_all = Face2(lst)

    lst = []
    for i in range(4):
        lst.append(g)
    lst = tuple(lst)
    g_all = Face2(lst)

    lst = []
    for i in range(4):
        lst.append(w)
    lst = tuple(lst)
    w_all = Face2(lst)

    lst = []
    for i in range(4):
        lst.append(b)
    lst = tuple(lst)
    b_all = Face2(lst)

    lst = []
    for i in range(4):
        lst.append(y)
    lst = tuple(lst)
    y_all = Face2(lst)

    lst = []
    for i in range(4):
        lst.append(o)
    lst = tuple(lst)
    o_all = Face2(lst)

    lst = (w_all, g_all, r_all, b_all, y_all, o_all)
    cube222 = State2(lst)

    lst = []
    lst.append(w)
    lst.append(o)
    lst.append(w)
    lst.append(g)
    lst = tuple(lst)
    F = Face2(lst)

    lst = []
    lst.append(w)
    lst.append(b)
    lst.append(r)
    lst.append(g)
    lst = tuple(lst)
    U = Face2(lst)

    lst = []
    lst.append(o)
    lst.append(b)
    lst.append(g)
    lst.append(g)
    lst = tuple(lst)
    L = Face2(lst)

    lst = []
    lst.append(y)
    lst.append(r)
    lst.append(r)
    lst.append(b)
    lst = tuple(lst)
    R = Face2(lst)

    lst = []
    lst.append(r)
    lst.append(y)
    lst.append(o)
    lst.append(y)
    lst = tuple(lst)
    D = Face2(lst)

    lst = []
    lst.append(w)
    lst.append(o)
    lst.append(b)
    lst.append(y)
    lst = tuple(lst)
    B = Face2(lst)

    lst = (U, L, F, R, D, B)
    s2 = State2(lst)

    lst = []
    for i in range(9):
        lst.append(r)
    lst = tuple(lst)
    r_all = Face3(lst)

    lst = []
    for i in range(9):
        lst.append(g)
    lst = tuple(lst)
    g_all = Face3(lst)

    lst = []
    for i in range(9):
        lst.append(w)
    lst = tuple(lst)
    w_all = Face3(lst)

    lst = []
    for i in range(9):
        lst.append(b)
    lst = tuple(lst)
    b_all = Face3(lst)

    lst = []
    for i in range(9):
        lst.append(y)
    lst = tuple(lst)
    y_all = Face3(lst)

    lst = []
    for i in range(9):
        lst.append(o)
    lst = tuple(lst)
    o_all = Face3(lst)

    lst = []
    lst.append(w)
    lst.append(o)
    lst.append(o)
    lst.append(g)
    lst.append(r)
    lst.append(w)
    lst.append(w)
    lst.append(o)
    lst.append(g)
    lst = tuple(lst)
    F = Face3(lst)

    lst = []
    lst.append(w)
    lst.append(o)
    lst.append(b)
    lst.append(g)
    lst.append(y)
    lst.append(y)
    lst.append(r)
    lst.append(g)
    lst.append(g)
    lst = tuple(lst)
    U = Face3(lst)

    lst = []
    lst.append(o)
    lst.append(r)
    lst.append(b)
    lst.append(r)
    lst.append(b)
    lst.append(w)
    lst.append(g)
    lst.append(y)
    lst.append(g)
    lst = tuple(lst)
    L = Face3(lst)

    lst = []
    lst.append(y)
    lst.append(r)
    lst.append(r)
    lst.append(b)
    lst.append(g)
    lst.append(g)
    lst.append(r)
    lst.append(o)
    lst.append(b)
    lst = tuple(lst)
    R = Face3(lst)

    lst = []
    lst.append(r)
    lst.append(y)
    lst.append(y)
    lst.append(b)
    lst.append(w)
    lst.append(w)
    lst.append(o)
    lst.append(r)
    lst.append(y)
    lst = tuple(lst)
    D = Face3(lst)

    lst = []
    lst.append(w)
    lst.append(b)
    lst.append(o)
    lst.append(w)
    lst.append(o)
    lst.append(y)
    lst.append(b)
    lst.append(b)
    lst.append(y)
    lst = tuple(lst)
    B = Face3(lst)

    lst = (U, L, F, R, D, B)
    s3 = State3(lst)

    lst = (w_all, g_all, r_all, b_all, y_all, o_all)
    cube333 = State3(lst)

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

    """
    print "start"
    print cube333
    string = "R' D' U2 L' R2 B'"
    for ss in string.split():
        cube.move(ss)
    print cube
    # user_test(cube)

    solver = Solver(cube)
    print solver
    print getsizeof(cube)
    print getsizeof(solver)

    print solver.get_answer()

    print "222 start"
    print "BEFORE >>> "
    # print cube222
    print s2
    string = "R' U' R' F'"
    for ss in string.split():
        cube222.move(ss)
    print "AFTER >>> "
    # print cube222
    print s2
    print "solve start"
    # solver222 = Solver2(cube222)
    solver222s = Solver2(s2)
    print solver222s.get_answer()
    print "end"
    """

    for i in range(1):
        print
        print "random scremble"
        print "BEFORE >>> "
        print cube222
        solve2 = Solver2(cube222)
        print solve2.scremble()
        print "solve start"
        print "AFTER >>> "
        print solve2
        t = time()
        print solve2.get_answer()
        t = time() - t
        print "running time: %s" % t

