## @file test_All.py
#  @author Mahad Aziz - azizm17
#  @brief Python pytest module for test_All.py
#  @date February 16, 2021
#  @details This file tests functions from the CircleT.py, TriangleT.py,
# BodyT.py, and Scene.py using pytest and also tests Plot.py

import pytest
import math
from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene
from Plot import plot

g = 9.81


def Fx(t):
    return 0


def Fy(t):
    return -g * 1


def Fx2(t):
    return 0


def Fy2(t):
    return -g * 5


eps = 0.0000001


class TestCircleT:

    def setup_method(self, method):
        self.circle1 = CircleT(1, 1, 1, 1)
        self.circle2 = CircleT(1, 2, 3, 4)

    def teardown_method(self, method):
        self.circle1 = None
        self.circle2 = None

    def test_xcoord_are_equal(self):
        assert self.circle1.cm_x() == 1

    def test_ycoord_are_equal(self):
        assert self.circle1.cm_y() == 1

    def test_mass_are_equal(self):
        assert self.circle1.mass() == 1

    def test_m_inert_are_equal(self):
        assert self.circle1.m_inert() == 0.5

    def test_ValueError(self):
        with pytest.raises(ValueError):
            self.circle2 = CircleT(1, 1, 0, -1)


class TestTriangleT:

    def setup_method(self, method):
        self.triangle1 = TriangleT(1, 2, 3, 4)
        self.triangle2 = TriangleT(1, 1, 1, 1)

    def teardown_method(self, method):
        self.triangle1 = None
        self.triangle2 = None

    def test_xcoord_are_equal(self):
        assert self.triangle1.cm_x() == 1

    def test_ycoord_are_equal(self):
        assert self.triangle1.cm_y() == 2

    def test_mass_are_equal(self):
        assert self.triangle1.mass() == 4

    def test_m_inert_are_equal(self):
        assert self.triangle1.m_inert() == 3

    def test_ValueError(self):
        with pytest.raises(ValueError):
            self.triangle2 = TriangleT(1, 1, 0, -1)


class TestBodyT:

    def setup_method(self, method):
        self.body1 = BodyT([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1])
        self.body2 = BodyT([1], [1], [1])

    def teardown_method(self, method):
        self.body1 = None
        self.body2 = None

    def test_xcoord_are_equal(self):
        assert self.body1.cm_x() == 1

    def test_ycoord_are_equal(self):
        assert self.body1.cm_y() == 1

    def test_mass_are_equal(self):
        assert self.body1.mass() == 4

    def test_m_inert_are_equal(self):
        assert self.body1.m_inert() == 0

    def test_ValueError1(self):
        with pytest.raises(ValueError):
            self.body2 = BodyT([1], [1, 2], [1, 2, 3])

    def test_ValueError2(self):
        with pytest.raises(ValueError):
            self.body2 = BodyT([4, 5, 6], [7, 8, 9], [0, -1, 1])


class TestScene:

    def setup_method(self, method):
        self.circle1 = CircleT(1, 1, 1, 1)
        self.circle2 = CircleT(1, 2, 3, 4)
        self.scene1 = Scene(self.circle1, Fx, Fy, 1, 1)
        self.triangle1 = TriangleT(2, 2, 2, 2)
        self.triangle2 = TriangleT(5, 6, 7, 8)
        self.scene2 = Scene(self.triangle1, Fx, Fy, 3, 3)
        self.body1 = BodyT([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1])
        self.body2 = BodyT([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
        self.scene3 = Scene(self.body1, Fx, Fy, 5, 5)

    def teardown_method(self, method):
        self.circle1 = None
        self.circle2 = None
        self.scene1 = None
        self.triangle1 = None
        self.triangle2 = None
        self.scene2 = None
        self.body1 = None
        self.body2 = None
        self.scene3 = None

    def test_shape_are_equal_1(self):
        assert self.scene1.get_shape() == self.circle1

    def test_shape_are_equal_2(self):
        assert self.scene2.get_shape() == self.triangle1

    def test_shape_are_equal_3(self):
        assert self.scene3.get_shape() == self.body1

    def test_unbal_forces_are_equal_1(self):
        assert self.scene1.get_unbal_forces() == (Fx, Fy)

    def test_unbal_forces_are_equal_2(self):
        assert self.scene2.get_unbal_forces() == (Fx, Fy)

    def test_unbal_forces_are_equal_3(self):
        assert self.scene3.get_unbal_forces() == (Fx, Fy)

    def test_init_velo_are_equal_1(self):
        assert self.scene1.get_init_velo() == (1, 1)

    def test_init_velo_are_equal_2(self):
        assert self.scene2.get_init_velo() == (3, 3)

    def test_init_velo_are_equal_3(self):
        assert self.scene3.get_init_velo() == (5, 5)

    def test_set_shape_are_equal_1(self):
        self.scene1.set_shape(self.circle2)
        assert self.scene1.get_shape() == self.circle2

    def test_set_shape_are_equal_2(self):
        self.scene2.set_shape(self.triangle2)
        assert self.scene2.get_shape() == self.triangle2

    def test_set_shape_are_equal_3(self):
        self.scene3.set_shape(self.body2)
        assert self.scene3.get_shape() == self.body2

    def test_set_unbal_forces_are_equal_1(self):
        self.scene1.set_unbal_forces(Fx2, Fy2)
        assert self.scene1.get_unbal_forces() == (Fx2, Fy2)

    def test_set_unbal_forces_are_equal_2(self):
        self.scene2.set_unbal_forces(Fx2, Fy2)
        assert self.scene2.get_unbal_forces() == (Fx2, Fy2)

    def test_set_unbal_forces_are_equal_3(self):
        self.scene3.set_unbal_forces(Fx2, Fy2)
        assert self.scene3.get_unbal_forces() == (Fx2, Fy2)

    def test_set_init_velo_are_equal_1(self):
        self.scene1.set_init_velo(2, 2)
        assert self.scene1.get_init_velo() == (2, 2)

    def test_set_init_velo_are_equal_2(self):
        self.scene2.set_init_velo(4, 4)
        assert self.scene2.get_init_velo() == (4, 4)

    def test_set_init_velo_are_equal_3(self):
        self.scene3.set_init_velo(6, 6)
        assert self.scene3.get_init_velo() == (6, 6)

    def test_sim_are_equal_1(self):
        t, wsol = self.scene1.sim(5, 2)
        te, wsole = [0, 5], [[1, 1, 1, 1], [6, -239.25, 1, -97.1]]

        for i in range(len(t)):
            if te[i] == t[i]:
                assert t[i] == te[i]
            else:
                assert abs((t[i] - te[i]) / te[i]) < eps

        for i in range(len(wsol)):
            for j in range(len(wsol[i])):
                if wsol[i][j] == wsole[i][j]:
                    assert wsol[i][j] == wsole[i][j]
                else:
                    assert abs((t[i] - te[i]) / te[i]) < eps

    def test_sim_are_equal_2(self):
        t, wsol = self.scene2.sim(5, 2)
        te, wsole = [0, 5], [[2, 2, 3, 3], [17, -44.3125, 3, -21.525]]

        for i in range(len(t)):
            if te[i] == t[i]:
                assert t[i] == te[i]
            else:
                assert abs((t[i] - te[i]) / te[i]) < eps

        for i in range(len(wsol)):
            for j in range(len(wsol[i])):
                if wsol[i][j] == wsole[i][j]:
                    assert wsol[i][j] == wsole[i][j]
                else:
                    assert abs((t[i] - te[i]) / te[i]) < eps

    def test_sim_are_equal_3(self):
        t, wsol = self.scene3.sim(5, 2)
        te, wsole = [0, 5], [[1, 1, 5, 5], [26, -4.65625, 5, -7.2625]]

        for i in range(len(t)):
            if te[i] == t[i]:
                assert t[i] == te[i]
            else:
                assert abs((t[i] - te[i]) / te[i]) < eps

        for i in range(len(wsol)):
            for j in range(len(wsol[i])):
                if wsol[i][j] == wsole[i][j]:
                    assert wsol[i][j] == wsole[i][j]
                else:
                    assert abs((t[i] - te[i]) / te[i]) < eps


class TestPlot:

    def setup_method(self, method):
        self.circle = CircleT(1, 1, 1, 1)
        self.triangle = TriangleT(9, 8, 1, 1)
        self.body = BodyT([1, 2, 3, 4], [1, 2, 3, 4], [1, 1, 1, 1])
        self.scene = Scene(self.circle, Fx, Fy, 0, 0)

    def teardown_method(self, method):
        self.circle = None
        self.triangle = None
        self.body = None
        self.scene = None

    def test_plot(self):
        t, wsol = self.scene.sim(10, 100)
        plot(wsol, t)

        self.scene.set_shape(self.triangle)
        t, wsol = self.scene.sim(10, 100)
        plot(wsol, t)

        self.scene.set_shape(self.body)
        t, wsol = self.scene.sim(10, 100)
        plot(wsol, t)

        self.scene.set_init_velo(7 * math.cos(math.pi / 3), 7 * math.sin(math.pi / 3))
        self.scene.set_shape(self.circle)
        t, wsol = self.scene.sim(10, 100)
        plot(wsol, t)

        self.scene.set_shape(self.triangle)
        t, wsol = self.scene.sim(10, 100)
        plot(wsol, t)

        self.scene.set_shape(self.body)
        t, wsol = self.scene.sim(10, 100)
        plot(wsol, t)
