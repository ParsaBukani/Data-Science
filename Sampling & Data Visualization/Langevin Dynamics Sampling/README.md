# Langevin Dynamics Sampling

_Data Science — University of Tehran_

This project introduces **Langevin Dynamics**, a stochastic sampling algorithm widely used in Bayesian inference and modern generative models.  
The method leverages the **score function** of a distribution to guide sampling, combining deterministic updates with Gaussian noise.

## Tasks

1. **Score Function**
   - Derive and implement the score function $S_\theta(x)$ for a chosen Gaussian distribution.

2. **Langevin Dynamics Implementation**
   - Initialize $X_0 \sim \pi(x)$.
   - Iteratively update:
     $$
     X_{t+1} \leftarrow X_t + \epsilon S_\theta(X_t) + \sqrt{2\epsilon}\,Z_t, \quad Z_t \sim \mathcal{N}(0, I)
     $$
   - Collect samples after a sufficient burn-in period.

3. **Comparison with Direct Sampling**
   - Compare distributions of:
     - Langevin Dynamics samples.
     - Samples from `numpy.random.multivariate_normal`.

4. **Visualization**
   - Quiver plots of the score function.
   - Trajectories of sampled points.
   - Heatmap/density comparison of the generated distributions.

5. **Bonus**
   - Extend to a **mixture of Gaussians**.
   - Analyze whether Langevin dynamics can still capture the multimodal structure.

