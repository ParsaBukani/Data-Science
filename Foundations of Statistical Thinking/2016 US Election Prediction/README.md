
# 2016 U.S. Election — Poll Aggregation & Confidence Intervals

_Data Science — University of Tehran_

This project reproduces a simplified version of poll aggregation used in election forecasting (e.g., FiveThirtyEight).  
Using the **2016 Trump vs. Clinton** polling dataset, we estimate voter support, compute **95% confidence intervals**, visualize **time trends**, and test whether the **spread** between candidates differs from zero.

## Tasks

1. **CLT-Based CI Derivation**
   - Model a single voter as a Bernoulli RV: $X_i=1$ if supports **Clinton** (Democrat), $X_i=0$ if supports **Trump** (Republican).
   - With large $N$, use CLT to derive the **95% CI** for the true proportion $p$ of Clinton supporters.

2. **Monte Carlo Coverage (Synthetic)**
   - Assume the true proportion $p=0.47$.
   - Simulate $N=30$ voters per trial, repeat $10^5$ trials.
   - Verify that the CI from Task 1 covers $p$ ≈ **95%** of the time.

3. **Data Preparation**
   - Load `2016-general-election-trump-vs-clinton.csv`.
   - Keep columns: `Trump`, `Clinton`, `Pollster`, `Start Date`, `Number of Observations`, `Mode`.
   - **Drop** rows with missing `Number of Observations` (subgroups).

4. **Time-Series Visualization**
   - Plot Trump vs. Clinton support over time with distinct colors.
   - Add smooth trend lines to highlight temporal patterns.

5. **Total Sample Size**
   - Sum `Number of Observations` across all valid polls to obtain the **aggregate N**.

6. **Pooled Support Estimates**
   - Compute pooled proportions $\hat{p}_{\text{Clinton}}$ and $\hat{p}_{\text{Trump}}$.
   - Show the estimates in a compact table.

7. **95% CIs for Support**
   - Using the aggregated data, compute **95% CIs** for $\hat{p}_{\text{Clinton}}$ and $\hat{p}_{\text{Trump}}$.

8. **Spread Analysis & Hypothesis Test**
   - Define spread $d = p - (1-p) = 2p - 1$.
   - Estimate spread via $\hat{d} \approx 2\hat{p} - 1$, where $\hat{p}$ is Clinton’s pooled support.
   - Note: $\text{SE}(\hat{d}) = 2\,\text{SE}(\hat{p})$, with $\text{SE}(\hat{p})=\sqrt{\hat{p}(1-\hat{p})/N}$.

   a) Compute the **95% CI** for $d$:  
   $$
   \hat{d} \pm 1.96 \times 2\,\text{SE}(\hat{p})
   $$

   b) Test $H_0: d=0$ vs. $H_a: d\neq 0$.  
   - Report the **test statistic** and **p-value** to assess whether the spread differs from zero.

