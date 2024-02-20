import pyttsx3

from langdetect import detect

from Backend.switching import separation_words, separation_translates


def text_language_detect(text):
    """
    text_language_detect:
        Separates the language of the word.
    """
    # separation_words output a successively list of words.
    words = separation_words()
    # separation_translates output a successively list of translations.
    translates = separation_translates()
    if text in words:
        lang_words = detect(str(words))
        return lang_words
    elif text in translates:
        lang_translates = detect(str(translates))
        return lang_translates
    else:
        print("function text_language_detect: Error")
        pass


def text_speach(text):
    """
    text_speach:
        Performs voiceover of the text in the language in which the word appears.
    """
    text_language = text_language_detect(text)
    match text_language:
        case "en":
            speech_english(text)
        case "uk":
            speech_ukrainian(text)
        case "pl":
            print("pl")
        case "es":
            print("es")
        case "fr":
            print("fr")
        case "de":
            print("de")
        case "ja":
            print("ja")
        case "ko":
            print("ko")
        case "pt":
            print("pt")
        case "zh":
            print("zh")
        case "hi":
            print("hi")
        case _:
            print(f"Error: {text_language} language not found")


def speech_english(text, rate=180, volume=0.6):
    """
    speech_english:
        Speaks the entered text in English.
    """
    engine = pyttsx3.init()
    voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty("voice", voice_id)
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    engine.say(text)
    engine.runAndWait()


def speech_ukrainian(text, rate=180, volume=0.3):
    """
    speech_ukrainian:
        Speaks the entered text in Ukrainian.
    """
    engine = pyttsx3.init()
    voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Natalia"
    engine.setProperty("voice", voice_id)
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    engine.say(text)
    engine.runAndWait()


def detect_voice():
    """
    detect_voice:
        Output the available voices for the pyttsx3 library.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for voice in voices:
        print(f"id: {voice.id}")
        print(f"Ім'я: {voice.name}")
        print("\n")
