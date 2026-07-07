import streamlit as st
import pandas as pd

from db import (
    add_song,
    get_all_songs,
    search_song,
    top_songs,
    genre_stats,
    delete_song,
    update_song,
    songs_this_month
)

# ==================================
# Title
# ==================================
st.title("🎵 Music Playlist Tracker")

# ==================================
# Sidebar Menu
# ==================================
menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Add Song",
        "View Songs",
        "Search Song",
        "Top Songs",
        "Genre Statistics",
        "Songs This Month",
        "Update Song",
        "Delete Song"
    ]
)

# ==================================
# Add Song
# ==================================
if menu == "Add Song":

    st.header("➕ Add Song")

    title = st.text_input("Song Name")
    artist = st.text_input("Artist")
    genre = st.text_input("Genre")
    rating = st.slider("Rating", 1, 5)

    if st.button("Add Song"):

        add_song(
            title,
            artist,
            genre,
            rating,
            "2026-07-05"
        )

        st.success("✅ Song Added Successfully!")

# ==================================
# View Songs
# ==================================
elif menu == "View Songs":

    st.header("🎶 All Songs")

    songs = get_all_songs()

    if songs:

        df = pd.DataFrame(
            songs,
            columns=[
                "ID",
                "Title",
                "Artist",
                "Genre",
                "Rating",
                "Date Added"
            ]
        )

        st.dataframe(df)

    else:
        st.warning("No songs available.")

# ==================================
# Search Song
# ==================================
elif menu == "Search Song":

    st.header("🔍 Search Song")

    song = st.text_input(
        "Enter Song Name"
    )

    if st.button("Search"):

        result = search_song(song)

        if result:

            df = pd.DataFrame(
                result,
                columns=[
                    "ID",
                    "Title",
                    "Artist",
                    "Genre",
                    "Rating",
                    "Date Added"
                ]
            )

            st.dataframe(df)

        else:
            st.warning("Song Not Found")

# ==================================
# Top Songs
# ==================================
elif menu == "Top Songs":

    st.header("⭐ Top Rated Songs")

    top = top_songs()

    if top:

        df = pd.DataFrame(
            top,
            columns=[
                "ID",
                "Title",
                "Artist",
                "Genre",
                "Rating",
                "Date Added"
            ]
        )

        st.dataframe(df)

    else:
        st.warning("No songs available.")

# ==================================
# Genre Statistics
# ==================================
elif menu == "Genre Statistics":

    st.header("📊 Genre Statistics")

    stats = genre_stats()

    if stats:

        df = pd.DataFrame(
            stats,
            columns=[
                "Genre",
                "Number of Songs"
            ]
        )

        st.dataframe(df)

        st.bar_chart(
            df.set_index("Genre")
        )

    else:
        st.warning("No songs available.")

# ==================================
# Songs Added This Month
# ==================================
elif menu == "Songs This Month":

    st.header("📅 Songs Added This Month")

    songs = songs_this_month()

    if songs:

        df = pd.DataFrame(
            songs,
            columns=[
                "ID",
                "Title",
                "Artist",
                "Genre",
                "Rating",
                "Date Added"
            ]
        )

        st.dataframe(df)

    else:
        st.warning(
            "No songs added this month."
        )

# ==================================
# Update Song
# ==================================
elif menu == "Update Song":

    st.header("✏️ Update Song Rating")

    song_id = st.number_input(
        "Song ID",
        min_value=1,
        step=1
    )

    rating = st.slider(
        "New Rating",
        1,
        5
    )

    if st.button("Update"):

        update_song(
            song_id,
            rating
        )

        st.success(
            "✅ Song Updated Successfully!"
        )

# ==================================
# Delete Song
# ==================================
elif menu == "Delete Song":

    st.header("🗑️ Delete Song")

    song_id = st.number_input(
        "Enter Song ID",
        min_value=1,
        step=1
    )

    if st.button("Delete"):

        delete_song(song_id)

        st.success(
            "✅ Song Deleted Successfully!"
        )