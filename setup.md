# Project Setup Guide

## Step 1: Install PostgreSQL

Download PostgreSQL and install it.

Remember:

- Username: postgres
- Password: Your Password
- Port: 5432

Verify:

```bash
psql --version
```

---

## Step 2: Create Database

Open SQL Shell:

```sql
CREATE DATABASE music_db;
```

Connect:

```sql
\c music_db
```

---

## Step 3: Create Table

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

## Step 4: Install Python Libraries

```bash
pip install streamlit
pip install psycopg2-binary
pip install pandas
pip install matplotlib
```

---

## Step 5: Run Application

```bash
python -m streamlit run app.py
```


## Project Features

- Add Song
- View Songs
- Search Song
- Top Rated Songs
- Genre Statistics
- Genre Statistics Chart
- Songs Added This Month
- Update Song
- Delete Song

## CRUD Operations

- Create → Add Song
- Read → View Songs, Search Song, Top Songs, Songs This Month
- Update → Update Song
- Delete → Delete Song
