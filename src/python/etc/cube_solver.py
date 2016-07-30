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
    def __init__(self, colors=()):
        assert isinstance(colors, tuple)
        assert len(colors) == 9

        self._face = [[], [], []]
        for idx, item in enumerate(colors):
            assert isinstance(item, Color)
            self._face[idx % 3].append(item)

    def __str__(self):
        s = ""
        for r in range(3):
            for c in range(3):
                s += "%s" % str(self._face[r][c])
            s += "\n"
        return s.rstrip("\n")

    pass


class State:
    """A state of the Cube"""
    def __init__(self, faces=()):
        assert isinstance(faces, tuple)
        assert len(faces) == 6

        self._faces = []
        for item in faces:
            assert isinstance(item, Face)
            self._faces.append(item)

    def __str__(self):
        tab = " "*8*3
        s = ""
        for row in str(self._faces[0]).split("\n"):
            s += "%s%s\n" % (tab, row)

        temp = str(self._faces[1]).split("\n")
        for idx, item in enumerate(str(self._faces[2]).split("\n")):
            temp[idx] += "%s" % item
        for idx, item in enumerate(str(self._faces[3]).split("\n")):
            temp[idx] += "%s" % item
        for t in temp:
            s += "%s\n" % t

        for row in str(self._faces[4]).split("\n"):
            s += "%s%s\n" % (tab, row)

        for row in str(self._faces[5]).split("\n"):
            s += "%s%s\n" % (tab, row)

        return s
    pass

if __name__ == "__main__":
    r = Color("yellow")
    lst = []
    for i in range(9):
        lst.append(deepcopy(r))
    lst = tuple(lst)
    f = Face(lst)
    lst = []
    for i in range(6):
        lst.append(deepcopy(f))
    lst = tuple(lst)
    s = State(lst)

    print r
    print
    print f
    print
    print s


