import psycopg2

# =========================
# Database Connection
# =========================
connection = psycopg2.connect(
    host="localhost",
    database="music_db",
    user="postgres",
    password="Sahil123",
    port="5432"
)

cursor = connection.cursor()

print("Database Connected Successfully!")

# =========================
# Add Song
# =========================
def add_song(title, artist, genre, rating, date):
    cursor.execute(
        """
        INSERT INTO songs
        (title, artist, genre, rating, date_added)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (title, artist, genre, rating, date)
    )
    connection.commit()


# =========================
# Show All Songs
# =========================
def get_all_songs():
    cursor.execute("SELECT * FROM songs")
    return cursor.fetchall()


# =========================
# Search Song
# =========================
def search_song(song_name):
    cursor.execute(
        """
        SELECT *
        FROM songs
        WHERE title ILIKE %s
        """,
        ('%' + song_name + '%',)
    )
    return cursor.fetchall()


# =========================
# Top Rated Songs
# =========================
def top_songs():
    cursor.execute(
        """
        SELECT *
        FROM songs
        ORDER BY rating DESC
        LIMIT 10
        """
    )
    return cursor.fetchall()


# =========================
# Genre Statistics
# =========================
def genre_stats():
    cursor.execute(
        """
        SELECT genre,
               COUNT(*)
        FROM songs
        GROUP BY genre
        """
    )
    return cursor.fetchall()


# =========================
# Delete Song
# =========================
def delete_song(song_id):
    cursor.execute(
        """
        DELETE FROM songs
        WHERE id = %s
        """,
        (song_id,)
    )

    connection.commit()


# =========================
# Update Song Rating
# =========================
def update_song(song_id, rating):
    cursor.execute(
        """
        UPDATE songs
        SET rating = %s
        WHERE id = %s
        """,
        (rating, song_id)
    )

    connection.commit()


# =========================
# Songs Added This Month
# =========================
def songs_this_month():

    cursor.execute(
        """
        SELECT *
        FROM songs
        WHERE EXTRACT(MONTH FROM date_added)
              = EXTRACT(MONTH FROM CURRENT_DATE)
        AND EXTRACT(YEAR FROM date_added)
              = EXTRACT(YEAR FROM CURRENT_DATE)
        """
    )

    return cursor.fetchall()