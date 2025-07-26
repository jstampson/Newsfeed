# 🔊 Daily AI News Briefing via WhatsApp

This project is a fully automated pipeline that fetches daily news from leading AI and tech sources, summarizes them using a Large Language Model, converts the summary to speech, and sends it as an audio message via WhatsApp.

The goal: Build a personal AI news podcast, delivered straight to your phone — every day.

---

## 🧠 What It Does

1. **Fetches AI news** from curated RSS feeds (e.g. Google AI, MIT, Berkeley, VentureBeat).
2. **Summarizes the articles** using Google's Gemini 2.5 model via the Generative AI API.
3. **Composes a coherent daily briefing** with smooth transitions and structure.
4. **Converts the text to speech** using `gTTS` and saves it as an `.mp3`.
5. **Pushes the audio to GitHub** to make it accessible via raw link.
6. **Sends the `.mp3` to WhatsApp** using Twilio's API.

---

## ⚙️ Tech Stack

- **Python**
- `feedparser` – RSS feed reading  
- `google.generativeai` – LLM summarization (Gemini 2.5)  
- `gTTS` – Text-to-speech conversion  
- `Twilio` – WhatsApp message delivery  
- `Git / GitHub` – Hosting the audio file for public access  
- `.env` – Secure API credential handling  

---

## 🕒 Automation

A daily script (`daily_run.py`) orchestrates the entire process. It can be scheduled using:

- **Windows Task Scheduler** (on Windows)
- `cron` (on Linux/macOS)

This script:
- Runs the pipeline
- Checks if the `.mp3` has changed
- Pushes changes to GitHub
- Sends the new audio briefing via WhatsApp

---

## 🔐 Security Notes

API keys and credentials are managed securely using a `.env` file and **never exposed in the public repo**. The `.gitignore` excludes the `.env` file.

---

## 💡 Why I Built This

This started as a fun automation project, but became a robust daily news briefing system. It’s a great demonstration of:
- LLM integration into real workflows
- Automation using Python and APIs
- End-to-end product thinking (fetching → summarizing → converting → delivering)

---

## 📦 Folder Structure

Newsfeed/
├── audio_outputs/ # Output MP3s
├── daily_run.py # Main orchestration script
├── news_fetcher.py # RSS parsing logic
├── summarizer.py # LLM summarization
├── tts.py # Text-to-speech
├── whatsapp_sender.py # Twilio WhatsApp logic
├── .env # API keys (excluded from Git)
└── README.md



---

## 🚀 Future Improvements

- Switch from Twilio sandbox to a verified business number
- Add support for multiple recipients
- Deploy to cloud for 24/7 uptime
- Add language options for briefing

---

## 📱 Sample Output

Here’s what you receive daily:

> *"Good morning. Here's your AI news briefing. From MIT: Researchers unveil a new method for robot learning using human feedback..."*  
> *(Audio attached as WhatsApp voice message)*

---

## 🤝 License

MIT — feel free to use, remix, and build upon it.

---

## 🙋‍♂️ Author

**@jstampson**  
Let’s connect on [GitHub](https://github.com/jstampson)

