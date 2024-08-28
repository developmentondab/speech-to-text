import speech_recognition as sr

rec = sr.Recognizer()

# Set the microphone as the input source
with sr.Microphone() as mic:
    print("You can start talking")
    try:
        # Listen to the microphone input
        audio = rec.listen(mic, timeout=15)  # Adjust the timeout as needed
        print("time is over")
        
        # Recognize the speech using Google Web Speech API
        text = rec.recognize_google(audio)
        print("Text: " + text)
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
