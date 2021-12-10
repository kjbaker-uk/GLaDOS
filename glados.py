import os, random
from playsound import playsound

class GLaDOS:
    def __init__(self) -> None:
        self.play_intro = False

    def loading(self):
        print("Connecting to GLaDOS, Please wait.")
        playsound("audio/music/loading.mp3")

    def user_text_input(self):
        while True:
            try:
                command = input("[GLaDOS] Enter command: ")
                if "who are you" in command:
                    playsound("audio/GLaDOS-intro-1.wav")
                if "joke" in command:
                    playsound(f"audio/jokes/GLaDOS-joke-{random.randint(1, 14)}.wav")
                if "what is my name" in command:
                    playsound(f"audio/names/GLaDOS-keith.wav")
            except:
                playsound("audio/GLaDOS-ctrlc.wav")
                exit(0)

    
    def main(self):
        os.system('clear')
        if self.play_intro:
            self.loading()
        playsound(os.path.abspath("audio/greetings/GLaDOS-greeting-keith-1.wav"))
        self.user_text_input()

        
if __name__ == "__main__":
    glados = GLaDOS()
    glados.main()