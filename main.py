from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Data
books = pd.read_csv("clean_books.csv")

# Compute TF-IDF matrix for content-based recommendations
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['text'])
cosine_sim = cosine_similarity(tfidf_matrix)

# Initialize FastAPI app
app = FastAPI(title="📚 BookBazar API")

# Enable CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utility Functions
def recommend_books(title: str, n: int = 10):
    """Return top n similar books based on content similarity."""
    if title not in books['title'].values:
        return None
    idx = books[books['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    indices = [i[0] for i in sim_scores]
    return books.iloc[indices][['title', 'author', 'average_rating', 'year', 'image_url']].to_dict(orient='records')


def search_books(query: str, n: int = 20):
    """Search books by title or author (case-insensitive)."""
    mask = books['title'].str.contains(query, case=False, na=False) | \
           books['author'].str.contains(query, case=False, na=False)
    results = books[mask].head(n)
    if results.empty:
        return None
    return results[['title','author','average_rating','year','image_url']].to_dict(orient='records')


def top_books(n: int = 30):
    """Return top n books sorted by average_rating (popularity)."""
    top = books.sort_values(by='average_rating', ascending=False).head(n)
    return top[['title','author','average_rating','year','image_url']].to_dict(orient='records')

# API Endpoints
@app.get("/api/books")
def api_top_books():
    """Return top books for homepage."""
    return top_books()


@app.get("/api/books/search")
def api_search_books(query: str = Query(..., description="Search query string")):
    """Search books by title or author."""
    results = search_books(query)
    if not results:
        return {"message": f"No books found for '{query}'"}
    return results


@app.get("/api/books/recommend")
def api_recommend_books(title: str = Query(..., description="Book title to base recommendations on"),
                        n: int = Query(6, description="Number of recommendations")):
    """Return content-based recommendations for a book."""
    recs = recommend_books(title, n)
    if not recs:
        return {"message": f"No recommendations found for '{title}'"}
    return recs

