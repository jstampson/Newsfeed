from gtts import gTTS

def save_audio_with_gtts(text: str, filename: str = "output/briefing.mp3") -> str:
    """
    Convert the given text to speech and save it as an MP3 file.

    Args:
        text (str): The text to convert.
        filename (str): Name of the output file.

    Returns:
        str: Path to the saved audio file.
    """
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(filename)
    return filename
