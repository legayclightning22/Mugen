# main_controller.py
# Author: Hemendra
# Main controller to run voice and vision concurrently

import threading
import time

from ai_engine.llama_voice_inference import run_voice_interface
from vision.object_detection import run_vision_system

def main():
    print("=== Starting Hemendra's Humanoid Robot Core Systems ===")
    voice_thread = threading.Thread(target=run_voice_interface)
    vision_thread = threading.Thread(target=run_vision_system)

    voice_thread.start()
    vision_thread.start()

    try:
        while voice_thread.is_alive() and vision_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down all systems.")

if __name__ == "__main__":
    main()
