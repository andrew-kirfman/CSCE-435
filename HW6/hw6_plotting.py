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

    # ----------------------------------------------------------------------- #
    # Question 3: Host-to-device and device-to-host times                     #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.0, 0.30])


    # Host-to-Device Time
    runtime = np.array([0.019200, 0.018976, 0.018976, 0.029024, 0.027456, 0.030528,\
        0.037952, 0.037600, 0.049024, 0.075488, 0.124544, 0.156832, 0.281632])
    p = np.array([16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65535])
    xnew = np.linspace(p.min(), p.max(), 300)
    runtime_smooth = interp1d(p, runtime, kind="slinear")
    ax.plot(xnew, runtime_smooth(xnew), linewidth=3, color="green", label="Host-to-Device")


    # Device-to-Host Time
    runtime = np.array([0.024192, 0.022016, 0.020512, 0.020736, 0.021504, 0.022176,\
        0.023392, 0.023808, 0.022272, 0.021888, 0.023072, 0.022336, 0.023168])
    p = np.array([16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65535])
    xnew = np.linspace(p.min(), p.max(), 300)
    runtime_smooth = interp1d(p, runtime, kind="slinear")
    ax.plot(xnew, runtime_smooth(xnew), linewidth=3, color="blue", label="Device-to-Host")


    ax.legend(loc="best")
    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Points")
    ax.set_ylabel("Runtime (ms)")

    import code; code.interact(local=locals())



    # ----------------------------------------------------------------------- #
    # Question 2: GPU vs. CPU time for k = 11, ..., 16                        #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.0, 1800.00])

    # GPU Time
    runtime = np.array([1.580032, 3.153792, 6.312320, 12.877216, 27.455296, 79.591953])
    p = np.array([2048, 4096, 8192, 16384, 32768, 65536])
    xnew = np.linspace(p.min(), p.max(), 300)
    runtime_smooth = interp1d(p, runtime, kind="slinear")
    ax.plot(xnew, runtime_smooth(xnew), linewidth=3, color="green", label="GPU Time")


    # CPU Time
    runtime = np.array([1.729494, 6.709263, 26.765841, 106.740486, 427.333282, 1725.874512])
    p = np.array([2048, 4096, 8192, 16384, 32768, 65535])
    xnew = np.linspace(p.min(), p.max(), 300)
    runtime_smooth = interp1d(p, runtime, kind="slinear")
    ax.plot(xnew, runtime_smooth(xnew), linewidth=3, color="blue", label="CPU Time")


    ax.legend(loc="best")
    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Points")
    ax.set_ylabel("Runtime (ms)")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 2: GPU vs. CPU time for k = 4, ..., 10                         #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.0, 0.80])

    # GPU Time
    runtime = np.array([0.077280, 0.062496, 0.088128, 0.132704, 0.224896, 0.405024, 0.789536])
    p = np.array([16, 32, 64, 128, 256, 512, 1024])
    xnew = np.linspace(p.min(), p.max(), 300)
    runtime_smooth = interp1d(p, runtime, kind="slinear")
    ax.plot(xnew, runtime_smooth(xnew), linewidth=3, color="green", label="GPU Time")


    # CPU Time
    runtime = np.array([0.001239, 0.001705, 0.003675, 0.009710, 0.031227, 0.113245, 0.436861])
    p = np.array([16, 32, 64, 128, 256, 512, 1024])
    xnew = np.linspace(p.min(), p.max(), 300)
    runtime_smooth = interp1d(p, runtime, kind="slinear")
    ax.plot(xnew, runtime_smooth(xnew), linewidth=3, color="blue", label="CPU Time")


    ax.legend(loc="best")
    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Points")
    ax.set_ylabel("Runtime (ms)")

    import code; code.interact(local=locals())



    # Stop here for HW6



    # ----------------------------------------------------------------------- #
    # Question 2: Weak Scalability Study (speedup redo)                       #
    # ----------------------------------------------------------------------- #

    """

    plt.ylim([0.00, 1.10])

    runtime = np.array([1.000, 0.489, 0.234, 0.113, 0.053, 0.013, 0.003])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Efficiency (Sp/p)")

    import code; code.interact(local=locals())

    """

    # ----------------------------------------------------------------------- #
    # Question 2: Weak Scalability Study (speedup redo)                       #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.00, 1.10])

    runtime = np.array([1.000, 0.977, 0.935, 0.904, 0.855, 0.403, 0.196])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Speedup (T1/Tp)")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 2: Weak Scalability Study (runtime redo)                       #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.00, 13.00])

    runtime = np.array([2.535, 2.594, 2.710, 2.801, 2.965, 6.298, 12.917])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Runtime (seconds)")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 3: Strong Scalability Study (efficiency redo)                  #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.00, 1.10])

    runtime = np.array([1.000, 1.004, 0.998, 0.972, 0.973, 0.406, 0.164])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Efficiency (Sp/p)")

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 3: Strong Scalability Study (speedup redo)                     #
    # ----------------------------------------------------------------------- #

    plt.ylim([0, 16.0])

    runtime = np.array([1.000, 2.007, 3.992, 7.776, 15.569, 13.000, 10.519])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Speedup (T1/Tp)")

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 3: Strong Scalability Study (runtime redo)                     #
    # ----------------------------------------------------------------------- #

    plt.ylim([0, 2.60])

    runtime = np.array([2.535, 1.263, 0.635, 0.326, 0.174, 0.195, 0.241])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processes (p)")
    ax.set_ylabel("Runtime (seconds)")

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 3: Strong Scalability Study (speedup)                          #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.00, 1.10])

    runtime = np.array([1.000, 0.945, 0.815, 0.622, 0.404, 0.146, 0.044])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Efficiency (Sp/p)")

    import code; code.interact(local=locals())

    # ----------------------------------------------------------------------- #
    # Question 3: Strong Scalability Study (speedup)                          #
    # ----------------------------------------------------------------------- #

    plt.ylim([0.00, 7.00])

    runtime = np.array([1.000, 1.890, 3.261, 4.972, 6.462, 4.684, 2.812])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Speedup (T1/Tp)")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 3: Strong Scalability Study (runtime)                          #
    # ----------------------------------------------------------------------- #

    plt.ylim([0, 3.2])

    runtime = np.array([3.147, 1.665, 0.965, 0.633, 0.487, 0.677, 1.119])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Runtime (seconds))")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 2: Weak Scalability Study (efficiency)                         #
    # ----------------------------------------------------------------------- #


    plt.ylim([0, 1.10])

    runtime = np.array([1.000, 0.531, 0.255, 0.122, 0.057, 0.014, 0.003])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Efficiency (Sp/p)")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 2: Weak Scalability Study (speedup)                            #
    # ----------------------------------------------------------------------- #


    plt.ylim([0, 1.10])

    runtime = np.array([1.000, 1.062, 1.018, 0.979, 0.914, 0.436, 0.210])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Speedup T1/Tp")

    import code; code.interact(local=locals())


    # ----------------------------------------------------------------------- #
    # Question 2: Weak Scalability Study (runtime)                            #
    # ----------------------------------------------------------------------- #

    plt.ylim([0, 16])

    runtime = np.array([3.362, 3.156, 3.293, 3.424, 3.667, 7.688, 15.974])

    p = np.array([1, 2, 4, 8, 16, 32, 64])

    xnew = np.linspace(p.min(), p.max(), 300)

    runtime_smooth = interp1d(p, runtime, kind="slinear")

    ax.plot(xnew, runtime_smooth(xnew), linewidth=3)

    ax.set_xscale("log", basex=2)
    ax.set_xlabel("Number of Processors (p)")
    ax.set_ylabel("Runtime (seconds)")

    import code; code.interact(local=locals())

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

    """
