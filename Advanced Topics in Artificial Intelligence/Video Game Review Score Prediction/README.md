# Video Game Review Score Prediction  

_Data Science — University of Tehran_  

This project tackles the challenge of predicting **video game review scores (1–10)** using a limited labeled dataset and a much larger pool of unlabeled reviews. It demonstrates the use of **semi-supervised learning (SSL)** techniques — specifically **Pseudo-Labeling** and **Active Learning** — to reduce reliance on manual annotation and improve generalization.  

## Workflow  

1. **Text Vectorization**  
   - Generate embeddings for review summaries using:  
     - **SentenceTransformer** (`all-MiniLM-L6-v2`) for dense semantic embeddings.  
     - **Word2Vec** (trained on all reviews) for distributed word representations.  
   - Apply **PCA** for dimensionality reduction and visualize clustering patterns by score.  

2. **Supervised Baselines**  
   - Train baseline models on the small labeled dataset:  
     - **Classification** (Logistic Regression, SVM, Random Forest Classifier).  
     - **Regression** (Linear Regression, Random Forest Regressor, SVR).  
   - Evaluate performance using metrics such as Accuracy, F1-score, MAE, RMSE, and $R^2$.  

3. **Semi-Supervised Learning**  
   - **Pseudo-Labeling**: Iteratively expand the labeled dataset with high-confidence predictions from the unlabeled pool.  
   - **Active Learning**: Use uncertainty-based query strategies (Least Confidence, Margin, Entropy) to select the most informative samples for manual labeling.  

4. **Comparative Performance Analysis**  
   - Summarize evaluation metrics across all approaches (baseline, SSL rounds).  
   - Plot **ROC curves, AUC scores**, and **learning curves**.  
   - Discuss trade-offs: pseudo-label confirmation bias vs. labeling cost in active learning.  

## Dataset  

- **Labeled Dataset**: `labeled_reviews.csv` — small set with `review_text` and `review_score`.  
- **Unlabeled Dataset**: `unlabeled_reviews.csv` — large pool of unlabeled `review_text`.  

The deliberate imbalance between labeled and unlabeled sets simulates real-world low-resource scenarios.  

## Learning Objectives  

- Gain hands-on experience with **semi-supervised learning** techniques.  
- Compare classification vs. regression paradigms for ordinal text data.  
- Explore the balance between **manual annotation effort** and **model performance**.  
