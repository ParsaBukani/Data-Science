
# Drug Safety Trial — Hypothesis Testing

_Data Science — University of Tehran_

This project analyzes data from a randomized controlled **drug vs. placebo trial**, focusing on **adverse effects** and blood cell counts. Using **independent t-tests**, we test whether the drug group differs significantly from the placebo group.

## Tasks

1. **Load & Clean Data**
   - Import `drug_safety.csv` into a Pandas DataFrame.
   - Drop rows with missing values where necessary.

2. **Exploratory Statistics**
   - Display summary statistics (mean, std, etc.) for numeric columns.
   - Group by treatment (`trx`: Drug vs. Placebo) and compare `wbc`, `rbc`, and `num_effects`.

3. **Preprocessing**
   - Convert `adverse_effects` (Yes/No) into numeric (1/0) for analysis.
   - Compute group means to enable comparisons.

4. **Hypothesis Testing (Independent t-tests)**  
   For each metric:
   - **White Blood Cell Count (wbc)**
   - **Red Blood Cell Count (rbc)**
   - **Number of Effects (num_effects)**
   - **Adverse Effects (adverse_effects)**

   Steps:
   - Formulate hypotheses:  
     $H_0$: No difference between Drug and Placebo groups.  
     $H_1$: Significant difference exists.  
   - Perform independent **t-test** using `scipy.stats.ttest_ind`.
   - Report **test statistic** and **p-value**.

5. **Significance Levels**
   - Compare results at $\alpha=0.05$ and $\alpha=0.10$.
   - State which tests reject/fail to reject $H_0$.
   - Interpret what significance levels mean in this context.

6. **Methodological Notes**
   - **`alternative`** argument in `ttest_ind`:  
     Specify `"two-sided"`, `"greater"`, or `"less"`.  
     Choose based on whether expecting directional or general difference.
   - **`equal_var`** argument:  
     Controls whether variances are assumed equal (pooled t-test) or not (Welch’s t-test).  
     Document which choice was made and why (e.g., based on variance checks).


