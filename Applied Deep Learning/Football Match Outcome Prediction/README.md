# Football Match Outcome Prediction (MLP)

_Data Science — University of Tehran_

This project uses a **Multi-Layer Perceptron (MLP)** to predict the outcomes of football matches.  
The dataset combines qualifiers and the **Qatar 2022 FIFA World Cup**. After training on qualifiers, the model is applied to forecast the entire tournament.

## Workflow

1. **Dataset Loading**
   - Attributes include team names, goals scored, match history differences, and a flag for World Cup matches (`wcm`).
   - Target variable (`status`):  
     - 1 = Home Win  
     - 2 = Tie  
     - 3 = Away Win  

2. **Exploratory Data Analysis (EDA)**
   - Investigated dataset structure, missing values, and feature distributions.  
   - Visualized class balance, feature correlations, and team-level performance.  
   - Excluded goal columns (`home_goals`, `away_goals`) and team names to avoid **data leakage**.

3. **Data Preparation**
   - Encoded categorical variables using label encoding.  
   - Split into **train/test sets** (70/30).  
   - Standardized numerical features with `StandardScaler` (fit only on train set).  
   - Converted features to PyTorch tensors.

4. **Model Development**
   - Defined an **MLP classifier** with fully connected layers in PyTorch.  
   - Activation functions: ReLU for hidden layers, Softmax for output.  
   - Loss function: **CrossEntropyLoss**.  
   - Optimizer: **SGD/Adam** with tuned learning rates.  

5. **Model Training & Evaluation**
   - Trained over multiple epochs, updating weights via backpropagation.  
   - Evaluated on the test set: accuracies >50% were acceptable, recognizing the unpredictability of football.

6. **World Cup Simulation**
   - Applied the trained MLP to predict:  
     - **Group stage rankings** (top 2 teams advance).  
     - **Knockout rounds** leading to a predicted champion.  
   - Tournament brackets were simulated using Qatar 2022 group configurations.

