## @file TriangleT.py
#  @author Mahad Aziz - azizm17
#  @brief Python module for TriangleT that implements the TriangleT class
#  @date February 16, 2021

from Shape import Shape


## @brief This class implements the TriangleT module
# @details This class defines an equilateral triangle using the x and
# y coordinate of the center of mass, a side length, and the mass
class TriangleT(Shape):

    ## @brief Constructor for TriangleT that initializes the x and
    # y coordinate of the center of mass, a side length, and the mass
    # of the circle
    # @param x X coordinate of the center of mass of the TriangleT object
    # @param y Y coordinate of the center of mass of the TriangleT object
    # @param s Side length of the TriangleT object
    # @param m Mass of the TriangleT object
    # @throws ValueError if the side length and mass are less
    # than zero
    # @details An assumption is that the arguments provided will be of
    # the correct type
    def __init__(self, x, y, s, m):
        if not(s > 0 and m > 0):
            raise ValueError
        self.x = x
        self.y = y
        self.s = s
        self.m = m

    ## @brief Getter function for the x coordinate of the center of mass
    # of the TriangleT object
    # @return Returns the x coordinate of the center of mass of the
    # TriangleT object
    def cm_x(self):
        return self.x

    ## @brief Getter function for the y coordinate of the center of mass
    # of the TriangleT object
    # @return Returns the y coordinate of the center of mass of the
    # TriangleT object
    def cm_y(self):
        return self.y

    ## @brief Getter function for the mass of the TriangleT object
    # @return Returns the mass of the TriangleT object
    def mass(self):
        return self.m

    ## @brief Getter function that calculates the moment of inertia
    # of the TriangleT object
    # @return Returns the moment of inertia of the TriangleT object
    def m_inert(self):
        return self.m * self.s ** 2 / 12
