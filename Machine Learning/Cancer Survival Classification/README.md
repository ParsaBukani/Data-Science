
# Cancer Survival Classification

_Data Science — University of Tehran_

This project builds a **binary classification model** to predict the survival status of cancer patients, using demographic, diagnostic, and treatment-related features. The task was hosted as a **private Kaggle competition**.

## Objective
Predict whether a cancer patient is **alive (1)** or **deceased (0)** based on patient characteristics and medical history.

## Workflow

1. **Data Exploration**
   - Analyze demographics (e.g., age, weight, height).  
   - Examine cancer-specific attributes (cancer type, tumor size, stage at diagnosis).  
   - Review treatment history (chemotherapy, surgery, radiation sessions).

2. **Preprocessing & Feature Engineering**
   - Handle missing values.  
   - Encode categorical variables (e.g., Occupation, Insurance_Type).  
   - Normalize/scale continuous features.  
   - Extract new features (e.g., time between diagnosis and treatment).  

3. **Model Development**
   - Classical ML algorithms: Logistic Regression, SVM, Decision Trees, Random Forests, etc.  
   - Optimize hyperparameters using validation splits.  

4. **Evaluation**
   - Primary metric: **Accuracy** (as per Kaggle competition).  
   - Secondary metrics: Precision, Recall, and F1-score for balanced insight.  
   - Submission format:  
     ```csv
     id,label
     1,0
     2,1
     ...
     ```

## Dataset
- Features include:  
  - Demographics: Birth date, Height, Weight, Urban/Rural.  
  - Diagnosis: Cancer type, Tumor size, Stage.  
  - Treatment: Surgery date, Radiation sessions, Chemotherapy drugs.  
- Target variable: **Survival_Status (0/1)**.

## Competition
Submissions were made on Kaggle:  
🔗 [Competition Link](https://www.kaggle.com/t/f6a3b0cdf6a84341bc1c60d639866a24)

