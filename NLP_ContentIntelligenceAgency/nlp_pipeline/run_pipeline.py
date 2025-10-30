from helpers import (
    extract_audio_transcription,
    process_transcript_tokens_and_wer,
    translate_french_to_english
)
import pandas as pd

if __name__ == "__main__":
    # === Step 1: Transcription ===
    AUDIO_FILE = "../Task 2/la_villa_s5e68.mp3"
    API_KEY = "b5e1d69d7be14bb291bff901bf4dc1c8"
    LANGUAGE = "fr"
    TRANSCRIPT_EXCEL = "assembly_transcript.xlsx"
    TRANSCRIPT_CSV = "assembly_transcript.csv"

    print("[*] Transcribing audio with AssemblyAI...")
    transcript_df = extract_audio_transcription(AUDIO_FILE, language_code=LANGUAGE, api_key=API_KEY)
    transcript_df.to_excel(TRANSCRIPT_EXCEL, index=False, engine="openpyxl")
    transcript_df.to_csv(TRANSCRIPT_CSV, sep="\t", index=False)
    print(f"[✓] Transcription saved to {TRANSCRIPT_EXCEL}")

    # === Step 2: Tokens & WER ===
    print("[*] Tokenizing and computing WER...")
    df_tokens, total_tokens, wer_score = process_transcript_tokens_and_wer(TRANSCRIPT_EXCEL)
    print(f"[✓] Total tokens: {total_tokens}")
    print(f"[✓] WER score: {wer_score:.4f}")

    # === Step 3: Translation ===
    print("[*] Translating French to English...")
    df_translated = translate_french_to_english(transcript_df)
    print(df_translated.head())

    TRANSLATED_CSV = "translated_data_assemblyAI.csv"
    TRANSLATED_EXCEL = "translated_data_assemblyAI.xlsx"
    df_translated.to_csv(TRANSLATED_CSV, sep="|", index=False)
    df_translated.to_excel(TRANSLATED_EXCEL, index=False)
    print(f"[✓] Translated data saved to {TRANSLATED_EXCEL}")