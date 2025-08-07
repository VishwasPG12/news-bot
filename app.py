import requests
from transformers import pipeline
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import schedule
import time

load_dotenv()

SMTP_SERVER = "smtp.ethereal.email"
SMTP_PORT = 587
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def send_email(news_summary):
    """Send summarized news via email."""
    msg = MIMEText(news_summary, "plain")
    msg["Subject"] = "📰 Daily News Update"
    msg["From"] = EMAIL_USER
    msg["To"] = RECIPIENT_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        print("EMAIL_USER:", EMAIL_USER)
        print("EMAIL_PASS:", EMAIL_PASS)
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        print("✅ Email sent successfully!")

def job():
    """Fetch news and send summarized version."""
    print("🔄 Fetching and summarizing news...")

    url = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])[:5]  # Top 5 articles
    summarizer = pipeline("summarization")

    all_summaries = ""

    for article in articles:
        title = article.get("title", "No Title")
        url = article.get("url", "No URL")
        text = article.get("description") or title

        summary = summarizer(text, max_length=15, min_length=5, do_sample=False)
        summarized_text = summary[0]['summary_text']

        all_summaries += f"📌 Title: {title}\n📝 Summary: {summarized_text}\n🔗 URL: {url}\n\n"

    print(all_summaries)
    send_email(all_summaries)

# Schedule task
# schedule.every().day.at("08:00").do(job)

# print("✅ Scheduler is running. Waiting for next job...")

# while True:
#     schedule.run_pending()
#     time.sleep(60)
job()
