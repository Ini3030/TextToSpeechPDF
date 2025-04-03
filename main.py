import pdfplumber
import pyttsx3
import requests


# Parameter constants
API_KEY = ""
ONLINE_TTS_LANGUAGE = "en-us"
AUDIO_FORMAT = "MP3"


def main():
    # PDF Reader
    try:
        with pdfplumber.open("./PDFtoTTS/pdf_tts.pdf") as pdf:
            output: str = ""
            for page in pdf.pages:
                output += page.extract_text()
    except FileNotFoundError:
        print("PASTE YOUR .PDF FILE INTO THE 'PDFtoTTS' DIRECTORY "
              "AND NAME IT AS 'pdf_tts.pdf' IN ORDER TO BE READ PROPERLY."
              "OTHERWISE, CHANGE THE FILE PATH INSIDE THE CODE.")


    # Online TTS API conversion
    parameters = {
        "key": API_KEY,
        "hl": ONLINE_TTS_LANGUAGE,
        "src": output,
        "c": AUDIO_FORMAT,
    }
    try:
        api_response = requests.post(url="https://api.voicerss.org/", params=parameters)
        api_response.raise_for_status()
        with open("tts_api_audio.mp3", 'wb') as audio_file:
            audio_file.write(api_response.content)


    # Offline TTS conversion
    except requests.exceptions.RequestException or ValueError as error:
        engine = pyttsx3.init()
        engine.setProperty('rate', 135)
        engine.save_to_file(output, "offline_tts_file.mp3")
        engine.runAndWait()
        print(f"API UNREACHABLE — ERROR:{error}\nAN OFFLINE VERSION OF THE TTS FILE WAS GENERATED")


    else:
        print("TTS GENERATED FROM API REQUEST")


if __name__ == "__main__":
    main()
