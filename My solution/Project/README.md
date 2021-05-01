# Science-2 Project Part A

## Lennard Jones Argon Atom-Normal Analysis

* Ayush Sharma
* 2019101004

Table of Content:

* Requirements & code Execution & File structure
* Random initial configuration generation.
* Calculating `LJ Potential` of the generated System.
* Finding  minimum energy configuration of generated system.
* Hessian Matrix calculation with Eigen vectors & Eigen values
* Plotting Vibrational Frequencies


## Requirements & code Execution & File structure

**Requirements :**

```
    numpy
    matplotlib
    tqdm
    autograd
    multiprocessing
    functools
```

**Code Execution :**

**Note:** Move to `codes` folder before executing any command.

For each part of the project (total 5), a file has been written (nammed for same) with one other `configuration.py` file.

| Part |  Execute command    | Files Required     | Output                         |
| -    | -                   | -                  | -                              |
| 1 | python3 q1.py | `q1.py`, `configuration.py` | File `init_conf.xyz` |
| 2 | python3 q2.py | `q2.py`, `configuration.py`, `init_conf.xyz` | Prints LJ Potential |
| 3 | python3 q3.py | `q3.py`, `configuration.py`, `init_conf.xyz` | File `gradient_descent_log.txt`, `final_conf.xyz` |
| 4 | python3 q4.py | `q4.py`, `configuration.py`, `final_conf.xyz`| File `hessian.dat`, `eigen_value.dat`, `eigen_vectors.dat` |
| 5 | python3 q5.py | `q5.py`, `hessian.dat` | Image for Histogram for vibrational Frequency and File `modes.xyz` |


**File Structure :**

```
├── codes
│   ├── checker_files.py
│   ├── configuration.py
│   ├── outputs
│   │   ├── eigen_values.dat
│   │   ├── eigen_vectors.dat
│   │   ├── final_conf.xyz
│   │   ├── gradient_descent_log.txt
│   │   ├── hessian.dat
│   │   ├── init_conf.xyz
│   │   ├── modes.xyz
│   │   └── vibration_frequency.png
│   ├── q1.py
│   ├── q2.py
│   ├── q3.py
│   ├── q4.py
│   └── q5.py
├── README.md
├── README.pdf
├── Report.pdf
└── Requirements.txt
```