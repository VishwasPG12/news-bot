# News Bot

A simple Python automation bot that fetches the latest news using NewsAPI and sends it to your email inbox daily using Gmail's SMTP service.

---

## Features

- Fetches top headlines using the NewsAPI
- Formats the news in a clean email layout
- Sends the email through Gmail with app password
- Environment variables are used for secure credentials

---

## Technologies Used

- Python 3
- NewsAPI (https://newsapi.org)
- Gmail SMTP Server
- `smtplib`, `requests`, `dotenv`

---

## Setup Instructions
```bash
 1. Clone the repository

git clone https://github.com/<your-username>/news-bot.git
cd news-bot

 2. Install dependencies

Ensure you have Python installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
3. Create a .env file
In the root folder, create a .env file and add:

env
Copy
Edit
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_16_digit_app_password
EMAIL_USER: The Gmail address used to send the news

EMAIL_PASS: The 16-digit app password generated from your Google account (used instead of your Gmail password)

4. Run the bot
bash
Copy
Edit
python app.py
You will receive an email with the top headlines.

🛡️ Safety Tips
⚠️ Do NOT share your .env file
 .env is already added to .gitignore

Sample Output
The email contains:

Title

Source

Description

URL to full article

Example:

yaml
Copy
Edit
1. NASA plans new lunar mission 🌕
Source: BBC
Desc: NASA announces its next lunar rover...
Read more: https://www.bbc.com/news/xyz
