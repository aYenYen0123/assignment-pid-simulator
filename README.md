# iSpace
For assignments of iSapce

----------------------------------------------------------------------------------------------------------------------------------------
I would like you to write a python script(s) to solve a problem.

Please define classes or functions as needed, and write at least a unit test (pytest) per object.

I am not looking for a complex implementation (actually a simple implementation is ok), but I want to see a good understanding of encapsulation (organization of classes and functions) and a few examples of how you would test in pytest.

Consider sharing the output by github.

----------------------------------------------------------------

Consider the following one dimensional problem:

You have a 1 kg vehicle with an initial velocity of 10 m/s,
subject to a force which is a function of its velocity:

- f [N]: -sign(velocity_mps) * k_kgpm * (velocity_mps)^2 

- with k_kgpm = 0.05 [kg/m].

- Sampling time is 1s.

1. Plot the velocity as a function of time
2. Apply a PID controller to fix the speed to 5 m/s with a 1% error under 30s. Plot the result.
3. Explain how you selected the gains. Are these robust with respect changes in the initial velocity
