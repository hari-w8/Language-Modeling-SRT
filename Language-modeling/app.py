import os
from datetime import datetime
import speech_recognition as sr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import time  # Make sure this is imported at the top
import sys  # For exiting the program

# 🧠 Load grammar correction model (once)
tokenizer = AutoTokenizer.from_pretrained("vennify/t5-base-grammar-correction")
model = AutoModelForSeq2SeqLM.from_pretrained("vennify/t5-base-grammar-correction", use_safetensors=False)

def correct_grammar(text):
    input_text = f"grammar: {text}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_length=64,
            num_beams=5,
            no_repeat_ngram_size=2,
            early_stopping=True
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def save_to_documents(text):
    filename = f"corrected_transcription_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    path = os.path.join(os.path.expanduser("~/Documents"), filename)
    with open(path, "w") as f:
        f.write(text)
    print(f"✅ Saved corrected text to: {path}")


def listen_and_transcribe():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:  # Keep listening continuously until 'shut up bro' is said
        with mic as source:
            print("🎤 Speak now...")  # This message will now show clearly before countdown

            recognizer.adjust_for_ambient_noise(source, duration=0.3)

            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)
                print("🔍 Transcribing...")

                raw_text = recognizer.recognize_google(audio)
                print("🔤 Raw Transcript:", raw_text)

                corrected_text = correct_grammar(raw_text)
                print("✅ Corrected Transcript:", corrected_text)

                save_to_documents(corrected_text)

                # Start 10-second countdown after each transcription
                print("\n⏳ Starting 10-second countdown...")
                for i in range(10, 0, -1):
                    print(f"⏳ Listening will restart in {i} seconds", end='\r')
                    time.sleep(1)

                print("\n")  # Newline to separate messages

                # Check if the command 'shut up bro' is detected
                if "shut up bro" in raw_text.lower():
                    print("❌ 'Shut up bro' detected. Stopping the process.")
                    sys.exit()  # Exit the program if 'shut up bro' is detected

            except sr.WaitTimeoutError:
                print("\n⏰ No speech detected for 10 seconds. Listening timed out.")
            except sr.UnknownValueError:
                print("❌ Could not understand the audio.")
            except sr.RequestError as e:
                print(f"❌ Recognition error: {e}")


if __name__ == "__main__":
    listen_and_transcribe()
