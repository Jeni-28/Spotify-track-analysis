# 🎵 Spotify Track Analysis Project

A Python-based project that analyzes Spotify track data by fetching metadata using the Spotify Web API, storing it in a MySQL database, exporting it to a CSV file, and visualizing track popularity using charts. The project supports both single and bulk track processing.

---

## 🔍 Features

- ✅ Fetches track metadata (Track Name, Artist, Album, Popularity, Duration)
- ✅ Supports both single and multiple track URL input
- ✅ Stores track details in a MySQL database
- ✅ Exports results to a CSV file (`spotify_track_data.csv`)
- ✅ Generates a bar chart of track popularity using Matplotlib

---

## 🛠️ Tools & Technologies

- **Python 3.x**
- **Spotify Web API (Spotipy)**
- **MySQL**
- **Pandas**
- **Matplotlib**
- **mysql-connector-python**
- **VS Code**
- **Git & GitHub**

---

## 📦 Project Structure

Spotify-track-analysis/
├── spotify.sql # MySQL schema (database + table)
├── track_urls.txt # List of Spotify track URLs
├── spotify_mysql.py # Single track analysis script
├── spotify_mysql_urls.py # Multiple track analysis script
├── spotify_track_data.csv # Auto-generated CSV output
├── track_popularity_chart.png # Auto-generated bar chart
├── README.md # Project documentation
└── .gitignore

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jeni-28/Spotify-track-analysis.git
cd Spotify-track-analysis

2️⃣ (Optional) Create a Virtual Environment
bash
Copy code
python -m venv .venv
.\.venv\Scripts\activate     # On Windows

3️⃣ Install Required Python Packages
bash
Copy code
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copy code
pip install spotipy mysql-connector-python pandas matplotlib
4️⃣ Set Up the MySQL Database
Run this command to create the database and table:

bash
Copy code
mysql -u root -p < spotify.sql

🚀 Running the Project
▶️ For Single Track Analysis
Use this to analyze one track at a time.

Open spotify_mysql.py and replace the default track_url with any Spotify track link.

Run the script:

bash
Copy code
python spotify_mysql.py
This script:

Extracts metadata from the given Spotify track.

Stores it in the MySQL database under the spotify_tracks table.

▶️ For Multiple Track Analysis
Add multiple Spotify track URLs in track_urls.txt (one per line).

Run the script:

bash
Copy code
python spotify_mysql_urls.py
This script:

Reads all URLs from track_urls.txt

Extracts metadata for each track

Inserts each track into the MySQL database

📊 Output Files
spotify_track_data.csv – CSV file generated from collected track data

track_popularity_chart.png – Bar chart showing track popularity (if included in the script)

✅ Outcome
This project demonstrates how to integrate third-party APIs, work with relational databases, automate data extraction and transformation, and visualize insights using Python tools. It gave me practical experience with real-world data workflows in the music domain.
