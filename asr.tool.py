import speech_recognition as sr
import tkinter as tk

def recognize():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        status.config(text="Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        result.config(text=text)
        status.config(text="Speech recognized!")
    except:
        result.config(text="Sorry, could not recognize speech.")
        status.config(text="Try again")

root = tk.Tk()
root.title("ASR - Speech Recognition")
root.geometry("600x350")

tk.Label(root, text="Automatic Speech Recognition",
         font=("Arial", 20, "bold")).pack(pady=30)

tk.Button(root, text="🎤 Start Speaking",
          command=recognize,
          font=("Arial", 14)).pack(pady=15)

status = tk.Label(root, text="Click the button and speak",
                  font=("Arial", 12))
status.pack(pady=10)

result = tk.Label(root, text="Your speech will appear here",
                  font=("Arial", 14), wraplength=500)
result.pack(pady=20)

root.mainloop()
