import speech_recognition as sr

class Speech_Engine:
    def __init__(self) -> None:
        # create a speech recognition object
        self.r = sr.Recognizer()

    def record_speech(self):
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            audio_data = self.r.record(source, duration=5)
            print("[+] Recognizing...")
            # convert speech to text
            text = self.r.recognize_google(audio_data)
            print(text)
    
    def main(self):
        print("[+] Human Speech Engine Test")

if __name__ == "__main__":
    hse = Speech_Engine()
    hse.main()