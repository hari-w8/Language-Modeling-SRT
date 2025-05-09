# Language-Modeling-SRT
A Python-based real-time speech-to-text system with grammar correction using a Transformer model, noise robustness, auto-saving, and voice-command control.
Absolutely! Based on your updated program (which includes **grammar correction, continuous listening, countdowns**, and **exit command via voice**), here's a tailored `README.md` content for your GitHub repository:

---

#  Speech-to-Text with Grammar Correction and Voice Control

This project is a **Python-based real-time speech recognition system** that not only transcribes speech to text but also performs **grammar correction using a Transformer model**, and can **respond to voice commands** (like "shut up bro" to exit). It is designed to be **noise robust, user-friendly**, and saves corrected transcriptions to your `Documents` folder.

---

##  Features

*  **Microphone-based speech recognition**
*  **Noise robustness** via ambient noise adjustment
*  **Grammar correction** using a pre-trained `T5` Transformer model
*  **Auto-saving** corrected text files with timestamps
*  **Automatic re-listening** every 10 seconds
*  **Voice command "shut up bro"** to exit the program
*  Runs entirely in Python using `speech_recognition`, `transformers`, and `torch`

---

##  Technologies Used

* [ Hugging Face Transformers](https://huggingface.co/vennify/t5-base-grammar-correction) – T5 model for grammar correction
*  [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – For microphone input and transcription
*  [PyTorch](https://pytorch.org/) – For running the Transformer model
*  Pure Python with no GUI (Terminal-based interaction)

---

##  Installation

Install the required packages:

```bash
pip install speechrecognition torch transformers
```

You may also need to install `pyaudio`:

* On Windows: `pip install pyaudio`
* On Linux:

  ```bash
  sudo apt install portaudio19-dev python3-pyaudio
  pip install pyaudio
  ```

---

##  How to Run

```bash
python speech_transcriber.py
```

> The script will start listening through your microphone, transcribe your speech, correct grammar, and save the output in the `Documents` folder.

Say **"shut up bro"** to stop the process at any time.

---

##  Output

Corrected transcripts are saved to your `Documents` folder as:

```
corrected_transcription_YYYYMMDD_HHMMSS.txt
```

---

##  Sample Output

```text
 Speak now...
 Transcribing...
 Raw Transcript: i has a dog and it eated my sandwich
 Corrected Transcript: I have a dog and it ate my sandwich
 Saved corrected text to: /home/username/Documents/corrected_transcription_20250508_130421.txt
```

---

## About Me

Name: R.hariharan
Project Title: Integrate language modling for improved accuracy in transcript.

GitHub: https://github.com/hari_w8)
Email: hari172003c@gmail.com


> This project is part of my final year research work focused on robust and intelligent voice transcription systems.

---
