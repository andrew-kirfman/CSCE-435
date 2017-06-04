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


