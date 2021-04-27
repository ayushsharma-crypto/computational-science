# Observations regarding the nature of trajectory

* We can observe early stable N<sub>1</sub> - N<sub>2</sub> equilibrium if β is small enoughi.e. β  < 10<sup>-4</sup>>. For example `Figure_1`.

* We can observe that for less value of α, the difference bwteen number of prey & predators is more as compared to those in higher α-value before convergence.

* We can observe N<sub>2</sub> → 0 if β too large where  β=0.8 . For example `Figure_3`

* The growth trajectories seem to follow the rationale that
* More Prey  ⟹ More Predator ⟹ Less Prey ⟹ Less Predator ⟹ More Prey

* This reasoning yields two oscialltory curves describing the two species, with the prey population curve leading to the predator population curve, as seen in the map.

* The populations' trajectories are therefore convergent, meaning that the amplitudes of the oscillations seem to decrease as time progresses. This is a direct result of the logistical essence of the prey population's development.

* We can observe in `Figure_4` that when `r=1` that means prey grows logistically with intrinsic growth rate of 1, the predator consumes all the preys & get almost extinct , then again preys grow in number & predator consumes them & so on infinite cycle.

* All the images have been stored in images folder.

**Figure 1**

![text](.\images\Figure_1.png)

**Figure 2**

![text](.\images\Figure_2.png)

**Figure 3**

![text](.\images\Figure_3.png)

**Figure 4**

![text](.\images\Figure_4.png)

**Different Values used to run code:**

```python3
initial_N1 =  [20, 20, 20,  10]
initial_N2 =  [5, 5, 5, 3]
initial_r = [1.5, 2.1, 2.5, 1]
initial_α = [0.2, 0.27, 0.8,  0.8]
initial_β = [0.0001, 0.15, 0.8, 0.8]
initial_c = [0.4, 0.5, 0.45,  0.45]
initial_k = [20, 25, 25, 25]
initial_t = [100, 100, 100, 100]
initial_i = [500, 500 ,500, 500]
```