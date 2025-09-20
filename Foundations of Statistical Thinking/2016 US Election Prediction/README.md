# 2016 U.S. Election — Poll Aggregation & Confidence Intervals

_Data Science — University of Tehran_

This project reproduces a simplified version of **poll aggregation** methods often used in election forecasting (e.g., FiveThirtyEight).  
Using the **2016 Trump vs. Clinton polling dataset**, we estimate voter support, compute **95% confidence intervals**, visualize **time trends**, and test whether the **spread** between candidates is statistically different from zero.

## Tasks

1. **CLT-Based CI Derivation**
   - Model a voter as a Bernoulli random variable: $X_i = 1$ if supports Clinton (Democrat), $X_i = 0$ if supports Trump (Republican).
   - For large $N$, use the Central Limit Theorem (CLT) to derive the 95% confidence interval (CI) for the true proportion $p$ of Clinton supporters.

2. **Monte Carlo Coverage (Synthetic)**
   - Assume $p = 0.47$ as the true population proportion.
   - Simulate $N = 30$ voters per trial, repeat $10^5$ trials.
   - Show that the CI from Task 1 captures $p$ approximately 95% of the time.

3. **Data Preparation**
   - Load `2016-general-election-trump-vs-clinton.csv`.
   - Retain only: `Trump`, `Clinton`, `Pollster`, `Start Date`, `Number of Observations`, `Mode`.
   - Drop rows with missing `Number of Observations`.

4. **Time-Series Visualization**
   - Plot Trump vs. Clinton support over time using distinct colors.
   - Add smooth trend lines to highlight patterns.

5. **Total Sample Size**
   - Sum `Number of Observations` across polls to compute the aggregate $N$.

6. **Pooled Support Estimates**
   - Compute pooled proportions $\hat{p}_{\text{Clinton}}$ and $\hat{p}_{\text{Trump}}$.
   - Present results in a compact table.

7. **95% CIs for Support**
   - Based on aggregated data, compute 95% CIs for $\hat{p}_{\text{Clinton}}$ and $\hat{p}_{\text{Trump}}$.

8. **Spread Analysis & Hypothesis Test**
   - Define the spread as  
     $d = p - (1-p) = 2p - 1$.
   - Estimate: $\hat{d} \approx 2\hat{p} - 1$, where $\hat{p}$ is Clinton’s pooled support.  
   - Standard error: $\text{SE}(\hat{d}) = 2\,\text{SE}(\hat{p})$, with  
     $\text{SE}(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{N}}$.

   a) Compute the 95% CI for $d$:  

   $$
   \hat{d} \pm 1.96 \times 2\,\text{SE}(\hat{p})
   $$

   b) Perform a hypothesis test: $H_0: d=0$ vs. $H_a: d \neq 0$.  
   - Report the test statistic and p-value.  
   - Conclude whether the spread is significantly different from zero.
