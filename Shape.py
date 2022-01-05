## @file Shape.py
#  @author Mahad Aziz - azizm17
#  @brief Python interface module that implements the Shape class
#  @date February 16, 2021

from abc import ABC, abstractmethod


## @brief This class implements the Shape interface module
# @details This class implements the interface that other modules
# will use to create specific shapes.
class Shape(ABC):

    ## @brief Abstract method of the Shape class that will return
    # the x-coordinate of the center of mass of the shape
    @abstractmethod
    def cm_x(self):
        pass

    ## @brief Abstract method of the Shape class that will return
    # the y-coordinate of the center of mass of the shape
    @abstractmethod
    def cm_y(self):
        pass

    ## @brief Abstract method of the Shape class that will return
    # the mass of the shape
    @abstractmethod
    def mass(self):
        pass

    ## @brief Abstract method of the Shape class that will return
    # the moment of inertia of the shape
    @abstractmethod
    def m_inert(self):
        pass
