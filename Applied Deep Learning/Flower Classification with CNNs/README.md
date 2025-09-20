
# Flower Classification with CNNs  

_Data Science — University of Tehran_  

This project builds deep learning models to classify flowers using the **Flowers Multiclass Dataset** from Kaggle.  
Two approaches are compared: a **VGG-style CNN** built from scratch, and a **fine-tuned ResNet50** pretrained on ImageNet.  

## Workflow  

1. **Dataset Loading**  
   - Download and prepare the Flowers dataset from Kaggle.  
   - Split into train (70%), validation (10%), and test (20%).  

2. **Image Preprocessing**  
   - Resize images to $224 \times 224$ pixels.  
   - Normalize pixel values to $[0, 1]$.  
   - Encode labels using **one-hot** or **label encoding** depending on the loss function.  

3. **Data Augmentation**  
   - Apply random transformations (rotations, flips, crops, brightness/contrast adjustments) on training data only.  
   - Improves generalization and robustness.  

4. **Model Development**  
   - **VGG-style CNN (from scratch):**  
     - Stacked $3 \times 3$ convolution layers with ReLU.  
     - Max-pooling for downsampling.  
     - Fully connected dense layers at the end.  
   - **ResNet50 Fine-Tuning:**  
     - Stage 1: Train classifier head with frozen base.  
     - Stage 2: Unfreeze last convolutional block + head.  
     - Stage 3: Train entire network end-to-end.  

5. **Evaluation & Comparison**  
   - Metrics: Accuracy, Precision, Recall, F1-score.  
   - Visual tools: Confusion Matrix, ROC curves, AUC.  
   - Compare generalization ability of **VGG-style CNN vs. ResNet50**.  

