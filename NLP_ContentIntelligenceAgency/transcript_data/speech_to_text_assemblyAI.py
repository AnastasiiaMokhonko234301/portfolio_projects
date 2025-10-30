import assemblyai as aai
import pandas as pd
import re

aai.settings.api_key = "b5e1d69d7be14bb291bff901bf4dc1c8"

audio_file = "/Users/daria/Desktop/2024-25c-fai2-adsai-anastasiiamokhonko234301/Week_1/extracted mp3s/Le Schtroumpf Navigateur • Les Schtroumpfs.mp3"

# Initialize transcriber with French language config
config = aai.TranscriptionConfig(language_code="fr")
transcriber = aai.Transcriber()

# Start transcription
transcript_id = transcriber.transcribe(audio_file, config=config)

# Wait for completion
transcript = transcriber.wait_for_completion(transcript_id)

if transcript.status == aai.TranscriptStatus.error:
    print(f"Transcription failed: {transcript.error}")
    exit(1)
#print(transcript.text)
# Extract sentences (assuming you want individual sentences in rows)
sentences = [{"Sentence": s.strip()} for s in re.split(r'(?<=[.!?]) +', transcript.text) if s.strip()]

# Convert to a DataFrame
df = pd.DataFrame(sentences)

# Specify output Excel file name
excel_filename = "Le_Schtroumpf_Navigateur_Les_Schtroumpfs.xlsx"

# Save to an Excel file
df.to_excel(excel_filename, index=False, engine="openpyxl")

print(f"Transcription saved as {excel_filename}")