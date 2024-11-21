from gtts import gTTS
import os
from playsound import playsound
import tempfile


def text_to_speech(text, language="en"):
    tts = gTTS(text=text, lang=language)

    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        tts.save(f"{temp_file.name}.mp3")
        playsound(f"{temp_file.name}.mp3")  # Play the sound directly
