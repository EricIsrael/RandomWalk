# RandomWalk


The following project accomplishes two tasks.

1: Performs an individual example random walk.

Runs simulation once for a 100 steps.
Shows the example trajectory (as if we were looking at the agent’s path from above) using Matplotlib. 
Shows a plot of the distance between the agent and its starting origin as a function of time using Matplotlib.

2: Created a second Method for taking a step. 

Instead of choosing a random new angle and moving, the current orientation of the agent should change by a random amount chosen from a normal distribution with mean 0 and standard deviation Sigma=1 (self.orientation = self.orientation + np.random.normal(0,Sigma)). 

Runs simulation once for a 100 steps.
Shows the example trajectory (as if we were looking at the agent’s path from above) using Matplotlib. 
Shows a plot of the distance between the agent and its starting origin as a function of time using Matplotlib.
