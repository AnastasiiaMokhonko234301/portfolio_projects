import pandas as pd
import spacy

# Load SpaCy French language model
nlp = spacy.load("fr_core_news_sm")

# File paths
file_paths = {
    "assemblyAI": r"Week_1/STT_Assembly.xlsx",
    "whisper": r"Week_1/STT_Whisper.xlsx"
}

# Function to tokenize text using SpaCy
def tokenize_french(text):
    doc = nlp(text.lower())  # Process text and lowercase
    tokens = [token.text for token in doc if not token.is_punct and not token.is_space]  # Remove punctuation & spaces
    return tokens

# Function to calculate Word Error Rate (WER)
def calculate_wer(df, token_column, s_col='S', i_col='I', d_col='D'):
    if s_col in df.columns and i_col in df.columns and d_col in df.columns:
        S = df[s_col].sum()
        I = df[i_col].sum()
        D = df[d_col].sum()
        N = df[token_column].explode().count()  # Total token count
        WER = (S + I + D) / N if N > 0 else 0
        return WER
    else:
        raise ValueError("Missing S, I, or D columns in the file.")

# Function to count tokens and compute WER
def process_transcript(file_path, header_row=0):
    df = pd.read_excel(file_path, header=header_row)
    
    # Identify the transcription column
    transcription_col = next((col for col in df.columns if "sentence" in col.lower() or "transcription" in col.lower()), None)

    if transcription_col is None:
        raise ValueError(f"No transcription column found in {file_path}.")
    
    # Tokenize and count tokens
    df['tokens'] = df[transcription_col].astype(str).apply(tokenize_french)
    total_tokens = df['tokens'].explode().count()
    
    # Calculate WER
    wer_score = calculate_wer(df, 'tokens')
    
    return df, total_tokens, wer_score

# Process both transcripts and compute WER
dfs = {}
wer_scores = {}

for model, path in file_paths.items():
    df, total_tokens, wer = process_transcript(path, header_row=0)
    dfs[model] = df
    wer_scores[model] = wer
    print(f"Total tokens in {model} transcript: {total_tokens}")
    print(f"WER for {model} transcript: {wer:.4f}")

## OUTPUT
# Total tokens in assemblyAI transcript: 1263
# WER for assemblyAI transcript: 0.0507
# Total tokens in whisper transcript: 1434
# WER for whisper transcript: 0.0704