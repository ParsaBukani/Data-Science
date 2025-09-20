
# Semantic Search on NiniSite

_Data Science — University of Tehran_

This project develops a **semantic search engine** for Persian-language Q&A data from the **NiniSite forum**.  
The goal is to go beyond keyword search by building an **embedding-based retrieval system** that ranks answers by meaning, using state-of-the-art multilingual models and a vector database.

## Workflow

1. **Preprocessing**
   - Normalize **Persian vs. Arabic characters**.  
   - Remove **diacritics**, unwanted characters, and punctuation noise.  
   - Apply **tokenization**, **stopword removal**, and **stemming/lemmatization**.  
   - Handle **informal repetition/slang**.  

2. **Exploratory Data Analysis (EDA)**
   - Inspect sample Q&A pairs.  
   - Compute and visualize **length distributions** (words & characters).  
   - Analyze **engagement patterns** (most-answered questions, active hours).  
   - Identify **top contributors** and perform **linguistic analysis**: word frequencies, n-grams, and word clouds.

3. **Semantic Retrieval**
   - Use **BAAI/bge-m3** multilingual embedding model from Hugging Face.  
   - Store embeddings in **LanceDB**, a vector database optimized for semantic search.  
   - Implement retrieval of top-5 similar results for different queries.  
   - Compare semantic retrieval with **classical full-text search**.

4. **Hybrid Search & Evaluation**
   - Research **hybrid search techniques** (semantic + keyword).  
   - Discuss evaluation metrics such as **precision@k, recall, NDCG**.  
   - Manually evaluate queries to compare approaches.

5. **Answer Reranking**
   - Apply a **cross-encoder reranker** (e.g., `bge-reranker` or `sentence-transformers` model).  
   - Re-rank retrieved answers for better semantic alignment.  
   - Compare before vs. after reranking.

