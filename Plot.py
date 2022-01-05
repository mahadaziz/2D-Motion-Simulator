## @file Plot.py
#  @author Mahad Aziz - azizm17
#  @brief Python module that implements the plot function that graphs data
#  @date February 16, 2021

import matplotlib.pyplot as plt


## @brief Function that will plot the graph of various data values
# @param w The window environment
# @param t The time values
# @throws ValueError when the length of the window environment
# is not equal to the length of the time values.
def plot(w, t):
    if len(w) != len(t):
        raise ValueError
    x = []
    y = []
    for i in range(len(w)):
        x += [w[i][0]]
        y += [w[i][1]]
    fig, axs = plt.subplots(3)
    fig.suptitle('Motion Simulation')
    axs[0].plot(t, x)
    axs[1].plot(t, y)
    axs[2].plot(x, y)

    axs.flat[0].set(xlabel='t(m)', ylabel='x(m)')
    axs.flat[1].set(xlabel='t(m)', ylabel='y(m)')
    axs.flat[2].set(xlabel='x(m)', ylabel='y(m)')
    plt.subplots_adjust(hspace=1)
    plt.show()
