Movie Recommendation System — CodSoft AI Internship

Task 2 — AI Project by Taushin Syed

This project is part of my CodSoft Artificial Intelligence Internship.  
It’s a content-based movie recommendation system that suggests similar movies based on textual descriptions (overviews) using *TF-IDF vectorization* and *cosine similarity*.

---

Features
- Suggests top 5 similar movies for any title entered by the user  
- Uses natural language processing on movie descriptions  
- Lightweight, fast, and fully reproducible  
- Implemented using Python, Pandas, Scikit-learn

---

Technologies Used
- Python  
- Pandas  
- Scikit-learn (TF-IDF, Cosine Similarity)  
- NumPy  

---

Folder Structure:
CODSOFT/
└── Task2_RecommendationSystem/
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
├── recommender.py
├── demo_cli.py
├── requirements.txt
├── README.md
└── .gitignore

---

How It Works
1. Loads the TMDB 5000 Movies Dataset (tmdb_5000_movies.csv)
2. Uses the *overview* text of each movie as content features  
3. Converts text to *TF-IDF vectors*
4. Calculates *cosine similarity* between movies  
5. Returns top 5 most similar movies for any given title  

---

Usage
Run this in your terminal:
```bash
python demo_cli.py

Then try:
You: Inception
You: Titanic
You: The Dark Knight

License

This project is for educational purposes under the CodSoft AI Internship Program.

⸻

Developed by:
Taushin Sayed
#codsoft #AI #MachineLearning #PythonSS