
# Movie Recommendation System

_Data Science — University of Tehran_

This project designs and evaluates a **movie recommendation system** to predict the ratings users would assign to movies they have not yet rated. The task was framed as a **supervised learning problem** and hosted as a Kaggle competition.

## Workflow

1. **Data Exploration & Preprocessing**
   - Datasets:
     - `train_data_movie_rate.csv`: user–movie ratings (`user_id`, `item_id`, `label`).
     - `train_data_movie_trust.csv`: trust relationships between users (`trustor`, `trustee`, `trust_value`).
   - Handle missing or inconsistent data.  
   - Normalize ratings if required (e.g., scale between 0 and 1).

2. **Model Development**
   - Build the recommendation system using **traditional ML algorithms** (no deep learning).  
   - Incorporate **user–item interactions** and **trust relationships** into features.  
   - Train models and optimize hyperparameters for best performance.

3. **Evaluation**
   - Metrics used:
     - Root Mean Squared Error (RMSE)
     - Mean Absolute Error (MAE)
     - Mean Squared Error (MSE)
     - $R^2$ Score
   - Compare multiple approaches to identify the most effective.

4. **Submission**
   - Predictions generated for `test_data.csv` containing (`user_id`, `item_id`) pairs.  
   - Submission format:
     ```csv
     id,label
     1,3.7
     2,4.1
     ...
     ```

## Competition
Submissions were made on Kaggle:  
🔗 [Competition Link](https://www.kaggle.com/t/a9cad5c235754b26ab87cee8c53e06b8)

