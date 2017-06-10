#!/usr/bin/env python

# --------------------------------------------------------------------------- #
# Developer: Andrew Kirfman                                                   #
# Project: CSCE-435 Homework #1                                               #
#                                                                             #
# File: ./hw1_plotting.py                                                     #
# --------------------------------------------------------------------------- #

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from scipy.interpolate import interp1d


if __name__ == "__main__":
    # Declare the plot itself
    fig = plt.figure()
    ax = fig.add_subplot(111)

    MARKER_SIZE = 15

    """

    # ----------------------------------------------------------------------- #
    # Question 6, part 2: p vs. Runtime for tv_sec = 0 (linear)               #
    # ----------------------------------------------------------------------- #

    plt.ylim([-0.1, 0.4859])

    runtime = np.array([0.0003, 0.0002, 0.0003, 0.0005, 0.0008, 0.0014, 0.0027,\
            0.0053, 0.0112, 0.0224, 0.0463, 0.0972, 0.1970, 0.3859])

    p = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xlabel("Number of Threads (p)")
    ax.set_ylabel("Runtime (seconds)")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 6, Part 1: p vs. Runtime for tv_sec = 0 (log scale)            #
    # ----------------------------------------------------------------------- #

    plt.ylim([-0.1, 0.4859])

    runtime = np.array([0.0003, 0.0002, 0.0003, 0.0005, 0.0008, 0.0014, 0.0027,\
            0.0053, 0.0112, 0.0224, 0.0463, 0.0972, 0.1970, 0.3859])

    p = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale('log', basex=2)
    ax.set_xlabel("Number of Threads (p)")
    ax.set_ylabel("Runtime (seconds)")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 5: p vs. runtime for barrier data                              #
    # ----------------------------------------------------------------------- #

    plt.ylim([1.9165, 2.5])

    runtime = np.array([2.0004, 2.0003, 2.0003, 2.0006, 2.0008, 2.0015, 2.0034, 2.0062,\
            2.0112, 2.0235, 2.0480, 2.1002, 2.2085, 2.4165])

    p = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale('log', basex=2)
    ax.set_xlabel("Number of Threads (p)")
    ax.set_ylabel("Runtime (seconds)")

    import code; code.interact(local=locals())

    """

    # ----------------------------------------------------------------------- #
    # Question 1 Part 2: p vs. speedup                                        #
    # ----------------------------------------------------------------------- #

    plt.ylim([0, 6])

    runtime = np.array([1.00, 1.940, 3.268, 4.075, 5.630, 4.058, 4.041, 4.008, 3.865,\
            3.648, 3.152, 1.902, 0.963, 0.499])

    p = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale('log', basex=2)
    ax.set_xlabel("Number of Threads (p)")
    ax.set_ylabel("Speedup (T1/Tp)")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 1 Part 1: p vs. runtime                                        #
    # ----------------------------------------------------------------------- #

    plt.ylim([0, 0.2])

    runtime = np.array([0.0974, 0.0502, 0.0298, 0.0239, 0.0173, 0.0240, 0.0241, 0.0243,\
            0.0252, 0.0267, 0.0309, 0.0512, 0.1011, 0.1949])

    p = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale('log', basex=2)
    ax.set_xlabel("Number of Threads (p)")
    ax.set_ylabel("Runtime (seconds)")

    import code; code.interact(local=locals())

    # Show the plot
    fig.show()

