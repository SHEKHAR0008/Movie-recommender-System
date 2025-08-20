# 📚🎬 Book and Movie Recommender System

## 📌 Project Overview
This project is a **content-based recommender system** that suggests the top 5 books and movies to users based on their input.  
It leverages **Natural Language Processing (NLP)** techniques to analyze content similarity between items.

---

## 🚀 Features
- Recommends **top 5 most similar books/movies** based on content.
- Uses **Bag-of-Words** representation with scikit-learn's `CountVectorizer`.
- Computes **cosine similarity** for ranking recommendations.
- Interactive **web application built with Streamlit**.
- Deployed on **Streamlit Cloud** for easy access.

---

## 🗂 Dataset
- Books and movies metadata (titles, descriptions, categories, authors, etc.).
- Preprocessed textual features for recommendation.

---

## 🛠️ Approach
1. **Data Preprocessing**  
   - Cleaned and structured book/movie metadata.  
   - Converted text into feature vectors using **Bag-of-Words** with `CountVectorizer` (max 5000 features, stop words removed).  

2. **Similarity Calculation**  
   - Applied **cosine similarity** to measure content similarity between items.  

3. **Recommendation Logic**  
   - Identified and ranked the top 5 most similar items for each user query.  

4. **Deployment**  
   - Developed UI with **Streamlit**.  
   - Hosted on **Streamlit Cloud** for public access.  

---

## 📊 Results
- Delivered **relevant recommendations** with high user satisfaction.  
- Achieved a **smooth user experience** with an intuitive interface.  
- Scalable solution that can be extended with additional data and features.  

---

## 💻 Tech Stack
- **Python 3**  
- **scikit-learn** – CountVectorizer, Cosine Similarity  
- **Streamlit** – Web app deployment  

---

