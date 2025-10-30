import requests
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
import requests
import json

API_BASE = "http://194.171.191.227:30080/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNmNDkxYWRiLThlZTgtNDExMi05OWU1LTBjODM5MDA2ZDgxOSJ9.1emxciT5A9Vc0J_ljlDflOGMlICVrLNS5fR5K_SD0VM"
# List models
header = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
response = requests.get(f"{API_BASE}/api/models", headers=header)
print(json.dumps(response.json(), indent=2))

def classify_emotions(token, sentence, prompt):
    url = 'http://194.171.191.227:30080/api/chat/completions'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "llama3.2:3b",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": sentence}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    
    try:
        result = response.json()
        return result['choices'][0]['message']['content'].strip().lower()
    except Exception as e:
        print(f"Error processing: {sentence} - {e}")
        return "error"

def evaluate_prompts(token, dataset_path):
    df = pd.read_csv(dataset_path)
    prompts = {
        "baseline": "Analyze the following sentence and classify it as one of the six core emotions (happiness, sadness, anger, surprise, fear, disgust) or neutral:",
        "few_shot": "Classify the emotion based on examples:\nExample: 'I am thrilled!' → happiness\nExample: 'I feel terrible.' → sadness\nSentence:",
        "structured": "Please classify the given sentence into one of the categories: happiness, sadness, anger, surprise, fear, disgust, or neutral. Provide only the category name."
    }
    results = {}
    
    for prompt_name, prompt_text in prompts.items():
        df[f'predicted_{prompt_name}'] = df['Translation'].apply(lambda x: classify_emotions(token, x, prompt_text))
        accuracy = accuracy_score(df['label'], df[f'predicted_{prompt_name}'])
        cm = confusion_matrix(df['Emotion'], df[f'predicted_{prompt_name}'], labels=["happiness", "sadness", "anger", "surprise", "fear", "disgust", "neutral"])
        results[prompt_name] = {"accuracy": accuracy, "confusion_matrix": cm}
    
    print("Evaluation complete. Results:")
    for prompt, metrics in results.items():
        print(f"{prompt}: Accuracy = {metrics['accuracy']}")
    
    return results

if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNmNDkxYWRiLThlZTgtNDExMi05OWU1LTBjODM5MDA2ZDgxOSJ9.1emxciT5A9Vc0J_ljlDflOGMlICVrLNS5fR5K_SD0VM"  # Replace with your actual token
    dataset_path = r"C:\Users\luisf\Documents\GitHub\2024-25c-fai2-adsai-group-group10_french_y2c\Task 7\simple_test_dataset.csv"
    evaluate_prompts(token, dataset_path)