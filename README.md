# 🎵 Music Playlist Tracker

A full-stack music playlist management application built using Python, PostgreSQL, and Streamlit.

---

## Features

- ➕ Add Songs
- 🎶 View All Songs
- 🔍 Search Songs
- ⭐ Top Rated Songs
- 📊 Genre Statistics
- 📈 Genre Statistics Chart
- 📅 Songs Added This Month
- ✏️ Update Song Rating
- 🗑️ Delete Song
- 📂 PostgreSQL Database Integration
- 🖥️ Streamlit User Interface
- 📋 Sidebar Navigation

---

## Technologies Used

- Python
- PostgreSQL
- psycopg2
- Streamlit
- Pandas
- Matplotlib

---

## Project Structure

```text
music-playlist-tracker/

│── app.py
│── db.py
│── requirements.txt
│── README.md
│── setup.md
```

---

## Database Table

```sql
CREATE TABLE songs(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    artist VARCHAR(100),
    genre VARCHAR(50),
    rating INTEGER,
    date_added DATE
);
```

---

## Application Features

### ➕ Add Song
Allows users to add a song with title, artist, genre, rating, and date.

### 🎶 View Songs
Displays all songs stored in the PostgreSQL database.

### 🔍 Search Song
Searches songs by title using PostgreSQL queries.

### ⭐ Top Rated Songs
Displays the top 10 highest-rated songs.

### 📊 Genre Statistics
Displays the number of songs available in each genre.

### 📈 Genre Statistics Chart
Shows genre-wise song distribution using a bar chart.

### 📅 Songs Added This Month
Displays all songs added during the current month.

### ✏️ Update Song
Allows users to update the rating of an existing song using the song ID.

### 🗑️ Delete Song
Allows users to delete a song from the database using the song ID.

---

## CRUD Operations

| Operation | Feature |
|-----------|---------|
| Create | Add Song |
| Read | View Songs, Search Song, Top Songs, Songs This Month |
| Update | Update Song |
| Delete | Delete Song |

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## Author

Sahil Kumar Singh