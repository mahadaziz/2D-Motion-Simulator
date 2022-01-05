## @file CircleT.py
#  @author Mahad Aziz - azizm17
#  @brief Python module for CircleT that implements the CircleT class
#  @date February 16, 2021

from Shape import Shape


## @brief This class implements the CircleT module
# @details This class defines a circle using the x and y coordinate
# of the center of mass, the radius, and the mass
class CircleT(Shape):

    ## @brief Constructor for CircleT that initializes the x and
    # y coordinate of the center of mass, the radius, and the mass
    # of the circle
    # @param x X coordinate of the center of mass of the CircleT object
    # @param y Y coordinate of the center of mass of the CircleT object
    # @param r Radius of the CircleT object
    # @param m Mass of the CircleT object
    # @throws ValueError if the radius and mass are less than
    # zero
    # @details An assumption is that the arguments provided will be of
    # the correct type
    def __init__(self, x, y, r, m):
        if not(r > 0 and m > 0):
            raise ValueError
        self.x = x
        self.y = y
        self.r = r
        self.m = m

    ## @brief Getter function for the x coordinate of the center of mass
    # of the CircleT object
    # @return Returns the x coordinate of the center of mass of the CircleT
    # object
    def cm_x(self):
        return self.x

    ## @brief Getter function for the y coordinate of the center of mass
    # of the CircleT object
    # @return Returns the y coordinate of the center of mass of the CircleT
    # object
    def cm_y(self):
        return self.y

    ## @brief Getter function for the mass of the CircleT object
    # @return Returns the mass of the CircleT object
    def mass(self):
        return self.m

    ## @brief Getter function that calculates the moment of inertia
    # of the CircleT object
    # @return Returns the moment of inertia of the CircleT object
    def m_inert(self):
        return self.m * self.r ** 2 / 2
