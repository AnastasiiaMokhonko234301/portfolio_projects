import re
import pandas as pd
import assemblyai as aai
import spacy
import torch
from transformers import MarianMTModel, MarianTokenizer
from tqdm import tqdm

# Load SpaCy French model
nlp = spacy.load("fr_core_news_sm")

# =======================
# AssemblyAI Transcription
# =======================
import time

def extract_audio_transcription(audio_file_path: str, language_code: str = "fr", api_key: str = None) -> pd.DataFrame:
    import re
    import assemblyai as aai

    if api_key is None:
        raise ValueError("API key must be provided.")

    aai.settings.api_key = api_key

    # Initialize transcriber
    config = aai.TranscriptionConfig(language_code=language_code)
    transcriber = aai.Transcriber()

    print("[*] Transcribing audio with AssemblyAI...")

    # Submit job
    transcript_id = transcriber.transcribe(audio_file_path, config=config)

    print("[*] Waiting for transcription to complete...")

    # Wait for completion
    transcript = transcriber.wait_for_completion(transcript_id)

    # Check for failure
    if transcript.status == aai.TranscriptStatus.error:
        raise RuntimeError(f"[✗] Transcription failed: {transcript.error}")

    # Extract sentences
    sentences = [{"Sentence": s.strip()} for s in re.split(r'(?<=[.!?]) +', transcript.text) if s.strip()]
    df = pd.DataFrame(sentences)

    print("[✓] Transcription completed.")
    return df

# =======================
# Tokenization & WER
# =======================
def tokenize_french(text: str) -> list:
    doc = nlp(text.lower())
    return [token.text for token in doc if not token.is_punct and not token.is_space]

def calculate_wer(df: pd.DataFrame, token_column: str = "tokens", s_col: str = 'S', i_col: str = 'I', d_col: str = 'D') -> float:
    if s_col in df.columns and i_col in df.columns and d_col in df.columns:
        S = df[s_col].sum()
        I = df[i_col].sum()
        D = df[d_col].sum()
        N = df[token_column].explode().count()
        return (S + I + D) / N if N > 0 else 0
    else:
        raise ValueError("Missing S, I, or D columns in the DataFrame.")

def process_transcript_tokens_and_wer(file_path: str, header_row: int = 0) -> tuple:
    df = pd.read_excel(file_path, header=header_row)
    transcription_col = next((col for col in df.columns if "sentence" in col.lower() or "transcription" in col.lower()), None)
    if transcription_col is None:
        raise ValueError(f"No transcription column found in {file_path}.")

    df['tokens'] = df[transcription_col].astype(str).apply(tokenize_french)
    total_tokens = df['tokens'].explode().count()
    wer_score = calculate_wer(df, 'tokens')
    return df, total_tokens, wer_score

# =======================
# Translation (FR → EN)
# =======================
def translate_french_to_english(df: pd.DataFrame, sentence_col: str = "Sentence", batch_size: int = 8) -> pd.DataFrame:
    """
    Translate a DataFrame of French sentences to English.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[*] Using device: {device}")

    model_name = "Helsinki-NLP/opus-mt-fr-en"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name).to(device)

    # Dummy input to warm up GPU
    _ = torch.tensor([[0]]).to(device)

    sentences = df[sentence_col].astype(str).tolist()
    translated = []

    for i in tqdm(range(0, len(sentences), batch_size), desc="Translating", unit="batch"):
        batch = sentences[i:i + batch_size]
        inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True).to(device)
        with torch.no_grad():
            outputs = model.generate(**inputs)
        translated_batch = [tokenizer.decode(t, skip_special_tokens=True) for t in outputs]
        translated.extend(translated_batch)

    df['Translation'] = translated
    return df
