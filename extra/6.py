import random
import matplotlib.pyplot as plt
import numpy as np

#  I1 = ∫ 3x^2 dx
#  I2 = ∫ ∫ x^2 y dxdy


def func1(x):
    return 3 * (x ** 2)


def func2(x, y):
    return (x ** 2) * y


def part1(N, T, graph=True):
    diff = 1  # (b-a) = 1 - 0 = 1
    act_val = 1
    if graph:
        I_plot0 = []
        N_plot0 = []
        for N1 in range(1, 100):
            s = 0
            for n in range(N1):
                r = random.random()
                v = func1(r)
                s += v * diff
            val = s / N1
            I_plot0.append(val)
            N_plot0.append(N1)
        plt.plot(N_plot0, I_plot0)
        plt.plot(N_plot0, [act_val for i in range(N1)])
        plt.show()
    T_plot = []
    I_plot = []
    for t in range(T):
        s = 0
        for n in range(N):
            r = random.random()
            v = func1(r)
            s += v * diff
        val = s / N
        I_plot.append(val)
        T_plot.append(t)
    std_dev = np.std(np.array(I_plot))
    mean = np.mean(np.array(I_plot))
    print(f"STD_DEV - {std_dev} MEAN - {mean}")
    if graph:
        plt.plot(T_plot, I_plot)
        plt.plot(T_plot, [1 for i in range(T)])
        plt.legend(["Simulated Value", "Actual Value"])
        plt.show()
    else:
        return std_dev


def part2(N, T, graph=True):
    diff = 1  # (b-a) = 1 - 0 = 1
    act_val = 1 / 6
    if graph:
        I_plot0 = []
        N_plot0 = []
        for N1 in range(1, 100):
            s = 0
            for n in range(N1):
                r1 = random.random()
                r2 = random.random()
                v = func2(r1, r2)
                s += v * diff
            val = s / N1
            I_plot0.append(val)
            N_plot0.append(N1)
        plt.plot(N_plot0, I_plot0)
        plt.plot(N_plot0, [act_val for i in range(N1)])
        plt.show()
    act_val = 1 / 6
    T_plot = []
    I_plot = []
    for t in range(T):
        s = 0
        for n in range(N):
            r1 = random.random()
            r2 = random.random()
            v = func2(r1, r2)
            s += v * diff
        val = s / N
        I_plot.append(val)
        T_plot.append(t)
    std_dev = np.std(np.array(I_plot))
    mean = np.mean(np.array(I_plot))
    print(f"STD_DEV - {std_dev} MEAN - {mean}")
    if graph:
        plt.plot(T_plot, I_plot)
        plt.plot(T_plot, [1 / 6 for i in range(T)])
        plt.legend(["Simulated Value", "Actual Value"])
        plt.show()
    else:
        return std_dev


if __name__ == "__main__":
    part1(20, 100)
    part1(1000, 100)
    part2(20, 100)
    part2(1000, 100)
    std_dev1 = []
    std_dev2 = []
    n_l = []
    sq_n = []
    for n in range(1, 100):
        std_dev1.append(part1(n, 1000, graph=False))
        std_dev2.append(part2(n, 1000, graph=False))
        n_l.append(n)
        sq_n.append(1 / (n ** (0.5)))
    plt.plot(n_l, std_dev1)
    plt.plot(n_l, sq_n)
    plt.legend(["Simulated Value", "Actual Value"])
    plt.show()
    plt.plot(n_l, std_dev2)
    plt.plot(n_l, sq_n)
    plt.legend(["Simulated Value", "Actual Value"])
    plt.show()
