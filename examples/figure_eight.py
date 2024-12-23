import numpy as np

numRobots = 1

r = 0.3
height = 0.7
w = 2 * np.pi / numRobots
T = 2 * 2 * np.pi / w

# horizontal circles
for i in range(0, numRobots):
    phase = 2 * np.pi / numRobots * i

    with open(f"timed_waypoints_figure8_{i}.csv", "w") as f:
        f.write("t,x,y,z,yaw\n")

        for t in np.linspace(0, T, 1000):
            f.write("{},{},{},{},{}\n".format(
                t,
                r * np.sin(2 * w * t + phase),
                r * np.sin(w * t + phase),
                height,
                0
            ))