# Spotify Track Analysis Project

This project analyzes Spotify track data by fetching metadata using the Spotify API, storing it in a MySQL database, and generating a CSV report and popularity chart.

## Features
✅ Fetches track details (name, artist, album, popularity, duration)  
✅ Stores data in a MySQL database  
✅ Exports data to CSV  
✅ Generates a bar chart of track popularity  

## Requirements
- Python 3.x
- MySQL Server
- Spotipy
- mysql-connector-python
- pandas
- matplotlib

## Setup & Run

### 📌 1️⃣ Create the MySQL database
```bash
mysql -u root -p < spotify.sql
