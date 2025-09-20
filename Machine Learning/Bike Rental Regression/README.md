
# Bike Rental Regression

_Data Science — University of Tehran_

This project develops a regression model to predict the **daily number of bike rentals** based on weather, seasonal, and calendar-related features.  
The task is framed as a **supervised regression problem** and evaluated through a dedicated Kaggle competition.

## Workflow

1. **Data Exploration & Preprocessing**
   - Inspect how features such as `season`, `temperature`, `humidity`, and `day type` affect rental activity.
   - Handle categorical variables via **encoding** and apply **scaling** to numerical features.
   - Address missing values and perform statistical feature selection (e.g., correlation analysis, p-values).

2. **Model Development**
   - Train regression models to predict the target variable:  
     **`total_users = casual_users + registered_users`**.
   - Explore multiple algorithms:  
     *Linear Regression, Decision Trees, Random Forest, Gradient Boosting*.
   - Fine-tune hyperparameters to optimize predictive performance.

3. **Evaluation Metrics**
   - Predictions are assessed using:
     - Mean Squared Error (MSE)
     - Root Mean Squared Error (RMSE)
     - R² Score
     - Mean Absolute Percentage Error (MAPE)
     - Mean Absolute Error (MAE)

4. **Submission**
   - Submit predictions in a CSV file with format:
     ```
     id, label
     ```
     where:
     - `id`: unique identifier for each record
     - `label`: predicted total number of rentals

5. **Optional Enhancements**
   - Integrate **external data sources** (e.g., special events, detailed weather reports) to improve prediction accuracy.

## Resources
Submissions were made on Kaggle:  
- [Kaggle Competition Link](https://www.kaggle.com/t/cafa0ac99d2b4b72b6b2ef736a4a51a7)

