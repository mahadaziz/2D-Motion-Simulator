## @file Scene.py
#  @author Mahad Aziz - azizm17
#  @brief Python module for Scene.py that implements the Scene interface for type Shape
#  @date February 16, 2021

from scipy.integrate import odeint


## @brief This class implements the Scene module
# @details This class simulates the physics of a scene where a shape moves through 2D space
# using the directional components of the force and velocity of the shape
class Scene():

    ## @brief Constructor for Scene that initializes the x and
    # y coordinate of the center of mass and the mass of the body
    # @param s A Shape object
    # @param fx Unbalanced force function in the x direction for the Shape
    # @param fy Unbalanced force function in the y direction for the Shape
    # @param vx Initial velocity of the Shape in the x direction
    # @param vy Initial velocity of the Shape in the y direction
    # @details An assumption is that the arguments provided will be of
    # the correct type
    def __init__(self, s, fx, fy, vx, vy):
        self.s = s
        self.fx = fx
        self.fy = fy
        self.vx = vx
        self.vy = vy

    ## @brief Getter function for the Shape object in the Scene object
    # @return Returns the Shape object in the Scene object
    def get_shape(self):
        return self.s

    ## @brief Getter function for the unbalanced force functions in the x
    # and y direction in the Scene object
    # @return Returns the unbalanced force function in the x and y direction
    # in the Scene object
    def get_unbal_forces(self):
        return self.fx, self.fy

    ## @brief Getter function for the initial velocity in the x and y
    # direction in the Scene object
    # @return Returns the initial velocity in the x and y direction
    # in the Scene object
    def get_init_velo(self):
        return self.vx, self.vy

    ## @brief Setter function for the Shape object in the Scene object
    # @param s A Shape object
    def set_shape(self, s):
        self.s = s

    ## @brief Setter function for the unbalanced force functions in the
    # Scene object
    # @param fx Unbalanced force function in the x direction for the Shape
    # @param fy Unbalanced force function in the y direction for the Shape
    def set_unbal_forces(self, fx, fy):
        self.fx = fx
        self.fy = fy

    ## @brief Setter function for the initial velocity in the Scene object
    # @param vx Initial velocity of the Shape in the x direction
    # @param vy Initial velocity of the Shape in the y direction
    def set_init_velo(self, vx, vy):
        self.vx = vx
        self.vy = vy

    ## @brief Simulation function that simulates the motion of the object
    # @param tfinal The final value of the simulation
    # @param nsteps The amount of steps that the scene is being simulated for
    # @return The time and position data for the Scene object
    def sim(self, tfinal, nsteps):
        t = []
        for i in range(nsteps):
            t += [i * tfinal / (nsteps - 1)]
        ode = odeint(self.__ode__, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t)
        return (t, ode)

    def __ode__(self, w, t):
        return [w[2], w[3], self.fx(t) / self.s.mass(), self.fy(t) / self.s.mass()]
