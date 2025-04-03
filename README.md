# PDF Text to Speech Python Script

This program will read a PDF file and return the text contents of the PDF as an audio file.

## Installing libraries
1. Create and set up your [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
2. Run this line in the terminal to install the required libraries:
```
python -m pip install -r requirements.txt
```

## Reading the PDF file
**You need to move or paste your PDF file inside the folder titled "PDFtoTTS"**.

The PDF file you place inside the "PDFtoTTS" folder also **needs to be named "pdf_tts.pdf" in order to be read**.

The program will then read the contents of the file as a string when run. Contents with different encoding will also be read by the program, and may affect the listenability of the TTS file.

If you want to specify a different path for the PDF, change the following line of code:
```
with pdfplumber.open("./PDFtoTTS/pdf_tts.pdf") as pdf:
```

## Online TTS conversion with Voice RSS API
When running the script, it will first attempt to make a request to the [Voice RSS API](http://www.voicerss.org/api/) and return an audio file with the contents of the PDF ( the default format will be .MP3). The file will be saved in the root folder with the name "tts_api_audio".

In order to use the Voice RSS API, you will need to get an [API KEY](http://www.voicerss.org/login.aspx) by registering an account.
Your API KEY should be pasted in the "Parameter constants" section of the code, inside the quotation marks of the "API_KEY" variable.

You can change the parameters of the API by changing the variables in the "Parameter constants section". This will allow you to configure how you wish the TTS file to be generated, such as changing the file format, language, etc. A list of all parameters is available [here](http://www.voicerss.org/api/) in the "parameters" section.

## Offline TTS conversion with pyttsx3
If and when the request to the API raises an exception, the program will proceed to generate a TTS file in .MP3 format using the pyttsx3 library, and provide an error code for the API request.
The file will be saved in the root folder with the name "offline_tts_file.mp3".
