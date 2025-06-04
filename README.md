# Humanoid Robot Project

This is a budget-built humanoid robot project designed by a 16-year-old passionate about machines, robots, engines, and tech. The robot is built using a Raspberry Pi 5 and is capable of performing real-world tasks like writing, cleaning, and sorting objects. It integrates computer vision, voice recognition, and a compressed version of Meta's LLaMA 3.1 language model to function autonomously.

## Features
- Voice command interpretation
- Object detection using camera
- Basic task automation (e.g., sorting, writing, dish cleaning)
- Runs on Raspberry Pi 5
- Local AI inference using compressed LLaMA 3.1

## Current Limitations
- Uses wheels instead of legs due to budget constraints
- Hand mechanism is unoptimized and needs regular maintenance

## Progress and Capabilities
- Integrated LLaMA 3.1 for voice-based conversation
- Working object detection
- Working task queue management with AI response

## Directory Structure
```
robot_project/
├── ai_engine/
│   ├── llama_voice_inference.py
│   ├── voice_command_handler.py
├── vision/
│   ├── object_detection.py
├── main_controller.py
├── README.md
```

## Getting Started (FIRST ***** REINSTALL RASBERRY OS YOU GUYS CORRUPT IT WAY TO MANY TIMES AND STOP TINKERING AND DOING THINGS YOU GUYS DONT KNOW JUST DO WHAT I SAID AND ASKED FOR pls😭😭😭😭😭)

### Requirements
- Raspberry Pi 5
- USB microphone
- Pi camera or USB webcam
- Python 3.10+
- Installed dependencies: `torch`, `transformers`, `openai-whisper`, `opencv-python`, `speechrecognition`

### Setup Instructions
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip ffmpeg libportaudio2 -y
pip3 install torch torchvision torchaudio
pip3 install transformers opencv-python speechrecognition openai-whisper
```

### Run Voice + AI Interaction
```bash
python3 ai_engine/llama_voice_inference.py
```

### Run Object Detection
```bash
python3 vision/object_detection.py
```

---

## CONTEXT FOR DUMBASSES LIKE MAYANK AND ALL MY OTHER FRIENDS READING THIS TO HELP ME AND MAKE IT BE READY BEFORE I ***** COME TO AUDITORIUM WITH THE HANDS

### Voice Recognition using LLaMA
- `llama_voice_inference.py` listens to the mic, converts speech to text using Whisper, feeds it to a compressed LLaMA 3.1 model, and speaks back the response using TTS.

### Object Detection
- `object_detection.py` runs a YOLOv5 model and identifies common objects in real-time using OpenCV and the camera feed.(IF RC NN doesnt work which ik it wont cuz you are dumb idiots)

---
