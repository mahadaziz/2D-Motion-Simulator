## @file BodyT.py
#  @author Mahad Aziz - azizm17
#  @brief Python module for BodyT that implements the BodyT class
#  @date February 16, 2021

from Shape import Shape


## @brief This class implements the BodyT module
# @details This class defines a body using the x and y coordinates of the center of
# mass and the mass of the body itself
class BodyT(Shape):

    ## @brief Constructor for BodyT that initializes the x and
    # y coordinate of the center of mass and the mass of the body
    # @param x List of x coordinates of the center of mass for the body
    # in the BodyT object
    # @param y List of y coordinates of the center of mass for the body
    # in the BodyT object
    # @param m List of the mass of the body in the BodyT object
    # @throws ValueError if the length of the x coordinates,
    # y coordinates, and mass lists are not the same
    # @throws ValueError if any value from the list of masses is less than
    # or equal to 0
    # @details An assumption is that the arguments provided will be of
    # the correct type
    def __init__(self, x, y, m):
        if not(len(x) == len(y) == len(m)):
            raise ValueError
        for i in m:
            if not i > 0:
                raise ValueError
        self.cmx = self.__cm__(x, m)
        self.cmy = self.__cm__(y, m)
        self.m = self.__sum__(m)
        z = self.__mmom__(x, y, m)
        self.moment = z - self.__sum__(m) * (self.__cm__(x, m) ** 2 + self.__cm__(y, m) ** 2)

    ## @brief Getter function for the list of x coordinates for the center of
    # mass of the body in the BodyT object
    # @return Returns the list of x coordinates for the center of mass of
    # the body in the BodyT object
    def cm_x(self):
        return self.cmx

    ## @brief Getter function for the list of y coordinates for the center of
    # mass of the body in the BodyT object
    # @return Returns the list of y coordinates for the center of mass of
    # the body in the BodyT object
    def cm_y(self):
        return self.cmy

    ## @brief Getter function for the list of mass of the body in
    # the BodyT object
    # @return Returns the list of mass of the body in the BodyT object
    def mass(self):
        return self.m

    ## @brief Getter function for the moment of inertia of the BodyT object
    # @return Returns the moment of inertia of the BodyT object
    def m_inert(self):
        return self.moment

    def __sum__(self, ms):
        return sum(ms)

    def __cm__(self, z, m):
        temp = 0
        for i in range(len(m)):
            temp += (z[i] * m[i])
        return temp / self.__sum__(m)

    def __mmom__(self, x, y, m):
        temp = 0
        for i in range(len(m)):
            temp += (m[i] * (x[i] ** 2 + y[i] ** 2))
        return temp
