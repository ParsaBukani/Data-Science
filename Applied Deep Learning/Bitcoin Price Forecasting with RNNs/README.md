
# Bitcoin Price Forecasting with RNNs  

_Data Science — University of Tehran_  

This project applies **Recurrent Neural Networks (RNNs)** to forecast **Bitcoin prices** using historical OHLCV (Open, High, Low, Close, Volume) data.  
By transforming time series into supervised sequences, the model learns temporal dependencies and predicts future market movements.  

## Workflow  

1. **Dataset Loading**  
   - Load `BTC-USD.csv` containing daily Bitcoin prices.  
   - Columns: `Open`, `High`, `Low`, `Close`, `Volume`.  

2. **Exploratory Data Analysis (EDA)**  
   - Plot OHLCV features across time to observe price dynamics.  
   - Compute correlations between features.  
   - Generate summary statistics (min, max, mean, std).  

3. **Data Processing**  
   - Handle missing/anomalous values.  
   - Normalize features.  
   - Define a custom target feature (indicator of profit/loss).  
   - Transform time series into supervised sequences using different **lookback periods** (30, 60, 90 days).  
   - Split data into **train/validation/test** sets.  

4. **Model Architecture**  
   - Base **RNN layers** for temporal learning.  
   - Fully connected layers for output prediction.  
   - Dropout for regularization.  
   - Regression loss and an efficient optimizer (e.g., Adam).  

5. **Model Training**  
   - Train the RNN with historical sequences.  
   - Tune hyperparameters: hidden units, layers, batch size, learning rate.  
   - Monitor training and validation loss to detect overfitting.  

6. **Evaluation & Visualization**  
   - Report regression metrics: **MSE, RMSE, MAE, MAPE, Cumulative Error (CE)**.  
   - Plot predictions vs. actual values over time.  
   - Visualize error trends to identify weak intervals.  

