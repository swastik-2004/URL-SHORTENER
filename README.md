🔗 Simple URL Shortener (Flask)

A simple full-stack URL Shortener web application built using Flask, SQLAlchemy, and SQLite.
This application allows users to shorten long URLs, store them in a database, and view previously generated links.

🚀 Features

✅ Shorten long URLs

✅ URL validation before saving

✅ Persistent storage using SQLite

✅ Click counter tracking

✅ History page showing all shortened URLs

✅ Automatic redirection

✅ Clean modular Flask structure

🛠️ Tech Stack

Backend: Flask (Python)

ORM: SQLAlchemy

Database: SQLite

Frontend: HTML + CSS

Validation: validators library

⚙️ How It Works

User enters a long URL.

The application validates the URL.

A unique short code is generated.

The original URL + short code are stored in SQLite.

When the short link is visited:

The app queries the database.

Increments the click counter.

Redirects to the original URL.

🧠 Database Schema
Column	Type	Description
id	Integer	Primary Key
original_url	String	Long URL entered by user
short_code	String	Unique short identifier
clicks	Integer	Number of times link was visited
created_at	DateTime	Timestamp of creation
💻 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/url-shortener.git
cd url-shortener

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python run.py


Open in browser:

http://127.0.0.1:5000

📸 Application Pages
🏠 Home Page

Enter URL

Generate short link

Navigate to history

📜 History Page

View all previously shortened URLs

Click tracking displayed

Direct access to shortened links

🔍 URL Validation

The application uses the validators Python package to ensure:

Only valid HTTP/HTTPS URLs are accepted

Invalid inputs are rejected

📈 Future Improvements

Custom short aliases

User authentication

Expiry dates for links

REST API version

Deployment to cloud (Render / Railway)

PostgreSQL support

Rate limiting & security enhancements

🎯 What I Learned

Flask Application Factory Pattern

Blueprints for modular routing

Database modeling with SQLAlchemy

URL validation handling

HTTP redirection logic

Clean project structuring

🏁 Author

Swastik Dasgupta

