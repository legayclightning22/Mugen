# llama_voice_inference.py
# Author: Hemendra
# Refactored to provide run_voice_interface() function

import speech_recognition as sr
import pyttsx3
import time

class LlamaModel:
    def __init__(self):
        print("[LLaMA] Initialized compressed LLaMA 3.1 model")

    def generate_response(self, prompt: str) -> str:
        print(f"[LLaMA] Received prompt: {prompt}")
        if "clean" in prompt.lower():
            return "Starting cleaning sequence."
        elif "sort" in prompt.lower():
            return "Sorting objects by color."
        elif "write" in prompt.lower():
            return "Preparing to write as requested."
        else:
            return "Sorry, I didn't understand. Could you please repeat?"

def listen_to_speech(recognizer, mic):
    print("[Speech] Listening...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"[Speech] You said: {text}")
        return text
    except sr.UnknownValueError:
        print("[Speech] Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"[Speech] Request error: {e}")
        return ""

def speak_text(engine, text):
    print(f"[TTS] Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def run_voice_interface():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    tts_engine = pyttsx3.init()
    llama = LlamaModel()

    print("=== Hemendra's Humanoid Robot Voice Interface ===")
    print("Say 'exit' or 'quit' to stop.")

    while True:
        speech_text = listen_to_speech(recognizer, mic)
        if speech_text.lower() in ["exit", "quit"]:
            print("Exiting voice interface.")
            break
        if speech_text.strip() == "":
            continue

        response = llama.generate_response(speech_text)
        speak_text(tts_engine, response)
        time.sleep(1)

if __name__ == "__main__":
    run_voice_interface()
