# daily_run.py

from news_fetcher import fetch_news
from summarizer import summarize_news_items, compose_morning_briefing
from tts import save_audio_with_gtts

import os
from subprocess import run
from datetime import date
from whatsapp_sender import send_whatsapp_message

# Pfade
REPO_PATH = os.path.abspath(".")
AUDIO_PATH = os.path.join(REPO_PATH, "audio_outputs", "briefing.mp3")

# MP3-Dateiname im pushbaren Ordner
if not os.path.exists(os.path.dirname(AUDIO_PATH)):
    os.makedirs(os.path.dirname(AUDIO_PATH))

def file_has_changed():
    result = run(["git", "diff", "--quiet", AUDIO_PATH])
    return result.returncode != 0

def commit_and_push():
    today = date.today().isoformat()
    run(["git", "add", AUDIO_PATH])
    run(["git", "commit", "-m", f"Update daily briefing MP3 for {today}"])
    run(["git", "push", "origin", "main"])
    print("✅ MP3 gepusht.")

def send_mp3():
    # WICHTIG: Anpassen an dein echtes GitHub-Repo
    mp3_url = "https://github.com/jstampson/Newsfeed/raw/refs/heads/main/audio_outputs/briefing.mp3"
    send_whatsapp_message("🎧 Here is your daily AI news briefing", media_url=mp3_url)

if __name__ == "__main__":
    print("📡 Fetching news...")
    news_items = fetch_news()

    if not news_items:
        print("❌ Keine News gefunden. Skript wird beendet.")
        exit()

    print("🧠 Summarizing news...")
    summarized_items = summarize_news_items(news_items)

    print("📝 Composing full text for TTS...")
    full_text = compose_morning_briefing(news_items)

    print("🔊 Converting text to MP3...")
    save_audio_with_gtts(full_text, AUDIO_PATH)

    if file_has_changed():
        print("📤 MP3 hat sich geändert, wird gepusht...")
        commit_and_push()
        print("📲 Sende über WhatsApp...")
        send_mp3()
    else:
        print("🟡 Keine Änderung an MP3 – kein Push oder WhatsApp-Versand.")
