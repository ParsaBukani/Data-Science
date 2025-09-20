
# LLM for Multiple-Choice Reasoning (SWAG)

_Data Science — University of Tehran_

This project explores the application of **Large Language Models (LLMs)** to solve complex **multiple-choice reasoning tasks** using the **SWAG dataset**.  
Unlike traditional models, LLMs capture **context and semantics**, making them well-suited for nuanced inference.

## Workflow

1. **Dataset Loading & Exploration**  
   - Use the **SWAG dataset** (~113k multiple-choice questions).  
   - Perform exploratory analysis to understand the meaning of key fields (`sent1`, `sent2`, `ending0–3`).  

2. **Preprocessing**  
   - Replicate context sentences and combine with candidate endings.  
   - Tokenize using **BERT tokenizer** (`bert-base-uncased`).  
   - Apply **dynamic padding** for efficiency.  

3. **Baseline Model**  
   - Load `AutoModelForMultipleChoice` with **BERT-base**.  
   - Evaluate performance on the validation set using accuracy and confusion matrix.  

4. **In-Context Learning (ICL)**  
   - Implement **few-shot prompting** and **step-by-step reasoning prompts**.  
   - Compare zero-shot vs. ICL performance.  

5. **Fine-Tuning with LoRA**  
   - Fine-tune BERT on the SWAG dataset using **LoRA (Low-Rank Adaptation)**.  
   - Use gradient accumulation to handle limited GPU memory.  
   - Evaluate with **Accuracy**, **Perplexity**, and **Confusion Matrix**.  

6. **Combined Approach**  
   - Apply ICL on top of the fine-tuned model.  
   - Compare results across:  
     - Zero-shot baseline  
     - ICL baseline  
     - Fine-tuned model  
     - Fine-tuned + ICL  

---

_**Note:** This project has two independent implementations (drafts), one developed by **Parsa Bukani** and the other by **Erfan Falahati**._

