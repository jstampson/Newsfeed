@echo off
cd /d C:\Users\stemp\Documents\projects\NewsFeed
call venv\Scripts\activate
python daily_run.py >> log.txt 2>&1