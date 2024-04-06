# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (
    """
    CREATE TABLE IF NOT EXISTS songplays
    (songplay_id INT PRIMARY KEY,
    start_time DATE REFERENCES time(start_time),
    user_id INT NOT NULL REFERENCES users(user_id),
    level TEXT,
    song_id TEXT REFERENCES songs(song_id),
    artist_id TEXT REFERENCES artists(artist_id),
    session_id INT,
    location TEXT,
    user_agent TEXT)
    """)

user_table_create = (
    """
    CREATE TABLE IF NOT EXISTS users
    (user_id INT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    level TEXT)
    """)

song_table_create = (
    """
    CREATE TABLE IF NOT EXISTS songs
    (song_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    duration FLOAT NOT NULL,
    artist_id TEXT NOT NULL REFERENCES artist(artist_id),
    year INT NOT NULL 
    )
    """)

artist_table_create = (
    """
    CREATE TABLE IF NOT EXISTS artists
    (artist_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    location TEXT NOT NULL)
    """)

time_table_create = (
    """
    CREATE TABLE IF NOT EXISTS time
    (start_time DATE PRIMARY KEY,
    hour INT NOT NULL,
    day INT NOT NULL,
    week INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    weekday TEXT NOT NULL)
    """)

# INSERT RECORDS

songplay_table_insert = (
    """
    INSERT INTO songplays
    (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING;
    """)

user_table_insert = (
    """
    INSERT INTO users
    (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING;
    """)

song_table_insert = (
    """
    INSERT INTO songs
    (song_id, title, duration, artist_id, year)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
    """)

artist_table_insert = (
    """
    INSERT INTO artists
    (artist_id, name, latitude, longitude, location)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
    """)

time_table_insert = (
    """
    INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
    """)

# FIND SONGS

song_select = (
    """
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.durtion = %s
    """)

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, 
                        time_table_create, songplay_table_create]

drop_table_queries = [user_table_drop, artist_table_drop, song_table_drop, 
                      time_table_drop, songplay_table_drop]