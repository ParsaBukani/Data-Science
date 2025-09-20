# Roulette Simulation & Profit Analysis  

_Introduction to Data Science — University of Tehran_  

In this project, we simulate the **American Roulette** game and analyze the statistical properties of betting strategies.  
The focus is on **Monte Carlo simulations** to evaluate expected earnings, distribution behavior, and the application of the **Central Limit Theorem (CLT)**.  

## Tasks  

1. **Game Simulation**  
   - Implement a function to simulate betting $1 on black for `N` rounds.  
   - Track total earnings `S_N` after repeated trials.  

2. **Monte Carlo Analysis**  
   - Run 100,000 simulations for `N = 10, 25, 100, 1000`.  
   - Plot and analyze distributions of total earnings.  
   - Compare empirical results with the **normal distribution**.  

3. **Average Winnings**  
   - Extend the analysis to average winnings `S_N / N`.  
   - Observe changes in expected values and standard errors with increasing `N`.  

4. **Theoretical Validation**  
   - Compute theoretical expected values and standard errors for each `N`.  
   - Compare against simulation results and discuss discrepancies.  

5. **Casino Loss Probability**  
   - Using the CLT, approximate the probability that the casino loses money when `N = 25`.  
   - Verify this result with Monte Carlo simulation.  

6. **Probability vs. Number of Rounds**  
   - Plot the probability of casino losses for `N = 25` to `N = 1000`.  
   - Discuss why casinos encourage players to continue betting.  

