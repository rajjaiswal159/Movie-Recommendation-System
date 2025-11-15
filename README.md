# 📚 BookBazar — Book Recommendation System

BookBazar is a web-based **Book Recommendation System** built using **FastAPI**, **Pandas**, and **Scikit-learn**. It provides both **popularity-based** and **content-based** recommendations. Users can search for books by title or author and get personalized book suggestions.

---

## 📂 Project Features

- **Top Books Section**: Displays top-rated books based on average rating.  
- **Search Functionality**: Search books by title or author (case-insensitive).  
- **Content-Based Recommendations**: Suggests similar books based on title and author using **TF-IDF** and **cosine similarity**.  
- **Responsive UI**: Clean and modern frontend built with **HTML, CSS, and JavaScript**.  
---

## ⚙️ Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, FastAPI, Uvicorn |
| Frontend | HTML, CSS, JavaScript |
| Data | Pandas, Cleaned CSV (`clean_books.csv`) |
| Machine Learning | Scikit-learn (TF-IDF, Cosine Similarity) |

---

## 📝 Dataset

- **Books Dataset**: `clean_books.csv` containing the following columns:  
year, author, title, average_rating, image_url, text

yaml
Copy code
- The `text` column is a combination of `title + author` used for content-based recommendations.

---

## 🚀 Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/BookBazar.git
cd BookBazar
Create and activate a virtual environment:

bash
Copy code
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the FastAPI backend:

bash
Copy code
uvicorn backend:app --reload
Open the frontend:

Open index.html in your browser.

Make sure the backend is running at http://127.0.0.1:8000.

🛠️ API Endpoints
Endpoint	Method	Description
/api/books	GET	Returns top books for homepage (popularity-based)
/api/books/search?query=QUERY	GET	Search books by title or author
/api/books/recommend?title=BOOK_TITLE&n=6	GET	Return content-based recommendations (default 6 books)

📸 Screenshots
(Optional: Add screenshots of your UI here)

💡 Usage
View Top Books on the homepage.

Search a book using the search bar.

Get Recommendations based on the first search result.

Click on book cards to explore more details (author, year, rating).

📈 Future Improvements
Integrate user ratings for collaborative filtering.

Add book descriptions or genres for better content-based recommendations.

Implement a hybrid model combining popularity + content similarity.

Add pagination for search results.

Deploy on Heroku / Vercel for live access.

📌 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute.

🤝 Authors
Raj Jaiswal
