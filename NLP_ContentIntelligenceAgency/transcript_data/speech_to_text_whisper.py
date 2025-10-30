import whisper
import pandas as pd

def transcribe_with_whisper(audio_file, model_size="small"):
    """Loads Whisper model and transcribes the given audio file."""
    model = whisper.load_model(model_size)  # Load Whisper model (faster but less accurate)
    result = model.transcribe(audio_file)   # Transcribe audio
    return result["text"]

def save_transcription_to_file(text, output_file):
    """Splits transcription into sentences and saves as Excel file."""
    sentences = text.split(". ")  # Basic sentence segmentation
    df = pd.DataFrame({"Sentence": sentences})
    df.to_excel(output_file, index=False)

# File name
audio_file = "la_villa_s5e68.mp3"

# Transcribe
transcribed_text = transcribe_with_whisper(audio_file)

# Save to Excel file
output_file = "transcribed_data_whisper.xlsx"
save_transcription_to_file(transcribed_text, output_file)

print(f"Transcription complete. Saved as {output_file}")