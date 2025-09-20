
# Image Segmentation Using Clustering Methods

_Data Science — University of Tehran_

This project explores **unsupervised image segmentation** using clustering techniques. The dataset consists of **football player images**, and the objective is to automatically segment players from the background by grouping pixels into meaningful regions.

## Workflow

1. **Understanding Segmentation**  
   - Review types of segmentation: **semantic, instance, and panoptic**.  
   - Focus of this project: **semantic segmentation** (all pixels of players labeled as "player").

2. **Dataset Loading**  
   - Load 50 sampled images from the [Football Player Segmentation Dataset](https://www.kaggle.com/datasets/ihelon/football-player-segmentation).  
   - Downscale images (1/8 or 1/16 resolution) to reduce computational cost.

3. **Feature Creation**  
   - Experiment with different pixel-level features:  
     - Color values only.  
     - Color + spatial coordinates.  
   - Compare and evaluate how features affect clustering quality.

4. **Pixel Clustering**  
   - Apply clustering methods: **K-Means, DBSCAN, Agglomerative Clustering**.  
   - Tune parameters (e.g., number of clusters $K$ in K-Means).  
   - Evaluate clustering with metrics such as **Silhouette Score** and **inertia**.  

5. **Filtering & Merging**  
   - Remove irrelevant clusters (e.g., ground, background).  
   - Merge smaller, adjacent clusters into larger player regions.

6. **Binary Mask & Post-Clustering**  
   - Generate binary masks (player = 1, background = 0).  
   - Re-cluster masks to identify connected components.  
   - Compute centroids and visualize masks with labeled components.

7. **Advanced Features (Bonus)**  
   - Use pretrained CNNs (e.g., **ResNet, HRNet**) to generate richer feature representations.  
   - Apply DBSCAN on extracted features and refine player segmentation.

8. **Evaluation**  
   - Compare predicted binary masks with **ground-truth annotations**.  
   - Metrics:  
     - **Dice Coefficient**  
     - **Intersection over Union (IoU)**  

