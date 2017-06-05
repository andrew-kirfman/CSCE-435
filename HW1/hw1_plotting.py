#!/usr/bin/env python

# --------------------------------------------------------------------------- #
# Developer: Andrew Kirfman                                                   #
# Project: CSCE-435 Homework #1                                               #
#                                                                             #
# File: ./hw1_plotting.py                                                     #
# --------------------------------------------------------------------------- #

import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Declare the plot itself
    fig = plt.figure()
    ax = fig.add_subplot(111)

    MARKER_SIZE = 15

    # ----------------------------------------------------------------------- #
    # Question 5 Part 3: p vs. efficiency                                     #
    # ----------------------------------------------------------------------- #

    plt.ylim([0, 1.2])

    ax.plot(1, 1, '*', markersize=MARKER_SIZE)
    ax.plot(2, 1, '*', markersize=MARKER_SIZE)
    ax.plot(4, 1, '*', markersize=MARKER_SIZE)
    ax.plot(8, 1, '*', markersize=MARKER_SIZE)
    ax.plot(16, 1, '*', markersize=MARKER_SIZE)
    ax.plot(32, 0.588, '*', markersize=MARKER_SIZE)
    ax.plot(64, 0.303, '*', markersize=MARKER_SIZE)
    ax.plot(128, 0.155, '*', markersize=MARKER_SIZE)
    ax.plot(256, 0.078, '*', markersize=MARKER_SIZE)
    ax.plot(512, 0.039, '*', markersize=MARKER_SIZE)
    ax.plot(1024, 0.019, '*', markersize=MARKER_SIZE)

    ax.set_xscale('log')

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 5 Part 2: p vs. speedup                                        #
    # ----------------------------------------------------------------------- #

    ax.plot(1, 1, '*', markersize=MARKER_SIZE)
    ax.plot(2, 2, '*', markersize=MARKER_SIZE)
    ax.plot(4, 4, '*', markersize=MARKER_SIZE)
    ax.plot(8, 8, '*', markersize=MARKER_SIZE)
    ax.plot(16, 16, '*', markersize=MARKER_SIZE)
    ax.plot(32, 18.816, '*', markersize=MARKER_SIZE)
    ax.plot(64, 19.376, '*', markersize=MARKER_SIZE)
    ax.plot(128, 19.899, '*', markersize=MARKER_SIZE)
    ax.plot(256, 20.003, '*', markersize=MARKER_SIZE)
    ax.plot(512, 19.951, '*', markersize=MARKER_SIZE)
    ax.plot(1024, 19.917, '*', markersize=MARKER_SIZE)

    ax.set_xscale('log')

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 5 Part 1: p vs. runtime                                        #
    # ----------------------------------------------------------------------- #

    ax.plot(1, 15.2763, '*', markersize=MARKER_SIZE)
    ax.plot(2, 7.5929, '*', markersize=MARKER_SIZE)
    ax.plot(4, 3.7970, '*', markersize=MARKER_SIZE)
    ax.plot(8, 1.8988, '*', markersize=MARKER_SIZE)
    ax.plot(16, 0.9501, '*', markersize=MARKER_SIZE)
    ax.plot(32, 0.8119, '*', markersize=MARKER_SIZE)
    ax.plot(64, 0.7884, '*', markersize=MARKER_SIZE)
    ax.plot(128, 0.7677, '*', markersize=MARKER_SIZE)
    ax.plot(256, 0.7637, '*', markersize=MARKER_SIZE)
    ax.plot(512, 0.7657, '*', markersize=MARKER_SIZE)
    ax.plot(1024, 0.7670, '*', markersize=MARKER_SIZE)

    ax.set_xscale('log')

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 4 Part 1: Minimum Points                                       #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.07, 0.08])
    #plt.xlim([125, 255])

    ax.plot(130, 0.0790, '*', markersize=MARKER_SIZE)
    ax.plot(135, 0.0775, '*', markersize=MARKER_SIZE)
    ax.plot(140, 0.0782, '*', markersize=MARKER_SIZE)
    ax.plot(145, 0.0780, '*', markersize=MARKER_SIZE)
    ax.plot(150, 0.0782, '*', markersize=MARKER_SIZE)
    ax.plot(200, 0.0786, '*', markersize=MARKER_SIZE)
    ax.plot(250, 0.0791, '*', markersize=MARKER_SIZE)

    ax.set_xscale('log')

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 3: Efficiency Plot                                             #
    # ----------------------------------------------------------------------- #

    ax.plot(1, 1.000, '*', markersize=MARKER_SIZE)
    ax.plot(2, 0.999, '*', markersize=MARKER_SIZE)
    ax.plot(4, 0.999, '*', markersize=MARKER_SIZE)
    ax.plot(8, 0.999, '*', markersize=MARKER_SIZE)
    ax.plot(16, 0.998, '*', markersize=MARKER_SIZE)
    ax.plot(32, 0.550, '*', markersize=MARKER_SIZE)
    ax.plot(64, 0.295, '*', markersize=MARKER_SIZE)
    ax.plot(128, 0.150, '*', markersize=MARKER_SIZE)
    ax.plot(256, 0.076, '*', markersize=MARKER_SIZE)
    ax.plot(512, 0.036, '*', markersize=MARKER_SIZE)
    ax.plot(1024, 0.016, '*', markersize=MARKER_SIZE)

    # Set the axis to be a log scale
    ax.set_xscale('log')

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 2: Speedup plot                                                #
    # ----------------------------------------------------------------------- #

    ax.plot(1, 1.000, '*', markersize=MARKER_SIZE)
    ax.plot(2, 1.998, '*', markersize=MARKER_SIZE)
    ax.plot(4, 3.997, '*', markersize=MARKER_SIZE)
    ax.plot(8, 7.994, '*', markersize=MARKER_SIZE)
    ax.plot(16, 15.964, '*', markersize=MARKER_SIZE)
    ax.plot(32, 17.613, '*', markersize=MARKER_SIZE)
    ax.plot(64, 18.907, '*', markersize=MARKER_SIZE)
    ax.plot(128, 19.145, '*', markersize=MARKER_SIZE)
    ax.plot(256, 19.340, '*', markersize=MARKER_SIZE)
    ax.plot(512, 18.336, '*', markersize=MARKER_SIZE)
    ax.plot(1024, 16.776, '*', markersize=MARKER_SIZE)

    # Set the axis to be a log scale
    ax.set_xscale('log')

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 1: Simple plot of data points                                  #
    # ----------------------------------------------------------------------- #

    ax.plot(1, 1.5182, '*', markersize=MARKER_SIZE)
    ax.plot(2, 0.7595, '*', markersize=MARKER_SIZE)
    ax.plot(4, 0.3798, '*', markersize=MARKER_SIZE)
    ax.plot(8, 0.1899, '*', markersize=MARKER_SIZE)
    ax.plot(16, 0.0951, '*', markersize=MARKER_SIZE)
    ax.plot(32, 0.0862, '*', markersize=MARKER_SIZE)
    ax.plot(64, 0.0803, '*', markersize=MARKER_SIZE)
    ax.plot(128, 0.0793, '*', markersize=MARKER_SIZE)
    ax.plot(256, 0.0785, '*', markersize=MARKER_SIZE)
    ax.plot(512, 0.0828, '*', markersize=MARKER_SIZE)
    ax.plot(1024, 0.0905, '*', markersize=MARKER_SIZE)

    # Set the axis to be a log scale
    ax.set_xscale('log')

    import code; code.interact(local=locals())

    # Show the plot
    fig.show()


