import pandas as pd
import spacy
import re

# Load SpaCy French language model
nlp = spacy.load("fr_core_news_sm")

# File paths
file_paths = {
    "assemblyAI": r"C:\Users\Mohon\OneDrive\Документы\GitHub\2024-25c-fai2-adsai-group-group10_french_y2c\Week_1\transcribed_data_assemblyAI_asta.xlsx",
    "whisper": r"C:\Users\Mohon\OneDrive\Документы\GitHub\2024-25c-fai2-adsai-group-group10_french_y2c\Week_1\transcribed_data_whisper_asta.xlsx"
}

# Function to tokenize text using SpaCy
def tokenize_french(text):
    doc = nlp(text.lower())  # Process text and lowercase
    tokens = [token.text for token in doc if not token.is_punct]  # Remove punctuation
    return tokens

# Function to count tokens for a transcript file
def count_tokens_spacy(file_path, header_row=0):
    # Load the transcript data
    df = pd.read_excel(file_path, header=header_row)
    
    # Identify the transcription column
    transcription_col = None
    for col in df.columns:
        if "sentence" in col.lower() or "transcription" in col.lower():  # Match case-insensitively
            transcription_col = col
            break

    if transcription_col is None:
        raise ValueError(f"No transcription column found in {file_path}.")
    
    # Tokenize and count tokens
    df['tokens'] = df[transcription_col].astype(str).apply(tokenize_french)
    
    # Print the first 5 sentences and their tokens for AssemblyAI
    if "assemblyAI" in file_path:
        print(f"First 5 sentences and their tokens for AssemblyAI ({file_path}):")
        for i, row in df.head(5).iterrows():
            print(f"Sentence: {row[transcription_col]}")
            print(f"Tokens: {row['tokens']}")
            print()
    
    # Print the first 5 sentences and their tokens for Whisper
    elif "whisper" in file_path:
        print(f"First 5 sentences and their tokens for Whisper ({file_path}):")
        for i, row in df.head(5).iterrows():
            print(f"Sentence: {row[transcription_col]}")
            print(f"Tokens: {row['tokens']}")
            print()
    
    return df

# Process both transcripts using the improved method
dfs = {name: count_tokens_spacy(path, header_row=0) for name, path in file_paths.items()}

# Display results
for model, df in dfs.items():
    print(f"Total tokens in {model} transcript: {df['tokens'].apply(len).sum()}")
