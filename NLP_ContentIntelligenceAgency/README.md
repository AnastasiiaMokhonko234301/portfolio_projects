# French Emotion Detection NLP Pipeline

**Client:** Content Intelligence Agency  
**Project:** Automated Emotion Analysis for French Media Content  
**Tech Stack:** Python, PyTorch, Transformers (CamemBERT, BERT), AssemblyAI  
**Domain:** Natural Language Processing, Emotion AI, Media Analytics

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-red.svg)
![Transformers](https://img.shields.io/badge/Transformers-4.36-yellow.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-63.09%25-success.svg)

## 📋 Project Overview

An end-to-end NLP pipeline that automatically analyzes emotions in French video content (reality TV, shows, transcripts) by combining speech-to-text, machine translation, and transformer-based emotion classification.

### Problem Statement

Media content producers need to understand the emotional landscape of their content for:
- Audience engagement analysis
- Content categorization
- Highlight reel generation
- Marketing insights

Manual emotion tagging is time-consuming and subjective.

### Solution

A production-ready pipeline that:
- ✅ Transcribes French video audio with 95% accuracy
- ✅ Classifies emotions into 7 categories with 63% overall accuracy
- ✅ Achieves 80% accuracy for high-risk emotion detection
- ✅ Provides explainable predictions using LIME and attention visualization
- ✅ Translates between French and English
- ✅ Processes hours of content in minutes

## 🎯 Emotion Categories

The model classifies text into 7 emotions:
1. **Happiness** (87.5% recall - excellent performance ✅)
2. **Neutral** (77.7% precision)
3. **Surprise** (68% balanced performance)
4. **Sadness**
5. **Anger**
6. **Disgust**
7. **Fear**

## 🗂️ Repository Structure

```
NLP_ContentIntelligenceAgency/
│
├── README.md                           # This file
│
├── nlp_pipeline/                       # Main pipeline implementation
│   ├── NLP_emotion_detection_pipeline.ipynb  # Complete pipeline
│   ├── run_pipeline.py                # Production script
│   └── requirements.txt               # Dependencies
│
├── data_preprocessing/                 # Data cleaning & preparation
│   ├── emotion_detection_dataset_processing.ipynb
│   ├── go_emotions_dataset_processing.ipynb
│   ├── feature_selection_finalized.ipynb
│   ├── solving_class_imbalance.ipynb
│   ├── transformers_dataset.ipynb
│   ├── zipping_dataset.ipynb
│   └── nb_confusion_matrix.ipynb
│
├── datasets/                           # Training & test data
│   ├── balanced_classes_dataset       # Class-balanced training data
│   ├── final_dataset                  # Production dataset
│   ├── go_emotions_dataset            # Google's emotion dataset
│   ├── synthetic_emotion_dataset      # Augmented data
│   ├── emory_nlp_ds                   # Friends TV show dataset
│   ├── df_gotranslated                # Translated datasets
│   └── custom_embeddings              # Fine-tuned embeddings
│
├── models/                             # Trained models
│   ├── best_lstm_model.h5             # LSTM baseline
│   ├── best_rnn_model.h5              # RNN baseline
│   ├── LR_NB                          # Logistic Regression + Naive Bayes
│   ├── LSTM                           # LSTM architecture
│   ├── RNN                            # RNN architecture
│   ├── Transformers                   # CamemBERT final model
│   └── Y2C_model_iteration_log        # Training logs
│
├── error_analysis/                     # Model diagnostics
│   ├── Error_analysis.ipynb           # Comprehensive error analysis
│   ├── error_analysis_Camembert.md                      # Error analysis report
│   ├── Confusion_matrix.png
│   ├── attention_map_*.png            # Attention visualizations
│   ├── lime_*.png                     # LIME explanations
│   └── performance_metrics/
│
├── machine_translation/                # Translation components
│   ├── machine_translation.ipynb      # FR↔EN translation
│   ├── machine_translation_iterations.ipynb
│   ├── transcribed_data_assemblyAI.csv
│   ├── translated_data_assemblyAI.xlsx
│   └── translations_scored.xlsx
│
├── transcript-data/                    # Video transcriptions
│   ├── transcribed_data_assemblyAI    # AssemblyAI output
│   ├── transcribed_data_whisper       # Whisper output
│   ├── speech_to_text_assemblyAI.ipynb
│   ├── speech_to_text_whisper.ipynb
│   └── la_villa_s5e68                 # Sample transcripts
│
├── WER-calc/                           # Transcription quality metrics
│   ├── STT_Assembly.xlsx              # AssemblyAI WER: 5.07%
│   ├── STT_Whisper.xlsx               # Whisper WER: 7.04%
│   └── Tokens_and_WER_calc.ipynb
│
├── xai_transformers/                   # Explainable AI
│   ├── XAI_for_Transformers.pdf       # Theory & implementation
│   ├── Part_1_Gradient_x_Input.ipynb
│   ├── Part_2_Conservative_Propagation.ipynb
│   ├── Part_3_Input_Perturbation.ipynb
│   └── selected_sentences_for_xai     # Test cases
│
├── prompt_engineering/                 # LLM experiments
│   ├── prompt_engineering.ipynb
│   ├── prompt_engineering_it1.ipynb
│   ├── prompt_engineering_tutorial.ipynb
│   └── simple_test_dataset
│
├── model_card/                         # Model documentation
│   ├── modelcard.md                   # Complete model card
│   └── performance_visualizations/
│
└── presentation/                       # Project deliverables
    └── Final_Presentation.pdf         # Client presentation
```

## 🚀 Pipeline Workflow

### Complete Process Flow

```
┌─────────────┐
│  Video      │
│  Input      │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ Audio Extraction    │
│ (MP3/WAV)           │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Speech-to-Text      │
│ (AssemblyAI)        │
│ French Transcript   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Text Preprocessing  │
│ (Tokenization)      │
└──────┬──────────────┘
       │
       ├──────────────────┐
       │                  │
       ▼                  ▼
┌─────────────┐   ┌─────────────────┐
│ Translation │   │ Emotion         │
│ (FR→EN)     │   │ Classification  │
│ OPUS-MT     │   │ (CamemBERT)     │
└─────────────┘   └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Emotion Output  │
                  │ + Confidence    │
                  │ + Explanations  │
                  └─────────────────┘
```

## 📊 Key Results

### Model Performance

| Metric | Score |
|--------|-------|
| **Overall Accuracy** | 63.09% |
| **High-Risk Detection** | **80.00%** |
| **Precision (weighted)** | 63.53% |
| **Recall (weighted)** | 63.09% |
| **F1-Score (weighted)** | 62.64% |

### Per-Class Performance

| Emotion | Precision | Recall | F1-Score |
|---------|-----------|--------|----------|
| **Happiness** | 0.73 | **0.88** | 0.73 |
| **Neutral** | **0.78** | 0.63 | 0.70 |
| **Surprise** | 0.68 | 0.70 | 0.69 |
| Anger | 0.55 | 0.41 | 0.45 |
| Sadness | 0.60 | 0.47 | 0.52 |
| Disgust | 0.57 | 0.51 | 0.49 |
| Fear | 0.54 | 0.55 | 0.54 |

### Transcription Quality

| Service | Word Error Rate (WER) | Status |
|---------|----------------------|---------|
| **AssemblyAI** | **5.07%** | ✅ Selected |
| Whisper | 7.04% | Tested |

## 🧠 Model Architecture

### CamemBERT 6 (Final Model)

**Base Model:** CamemBERT (French RoBERTa)  
**Fine-tuning:** 7-class emotion classification  
**Parameters:** ~110M  

**Training Configuration:**
- Optimizer: AdamW (lr=2e-5, weight_decay=0.01)
- Batch size: 16
- Max sequence length: 128 tokens
- Early stopping: patience=3
- Gradient clipping: max_norm=1.0
- Learning rate: Linear warmup scheduler

**Why CamemBERT?**
- Pre-trained on 138GB of French text
- Understands French linguistic nuances
- Better than multilingual models for French
- Contextual embeddings for subtle emotion detection

## 📚 Dataset Construction

### Data Sources (5 combined datasets)

1. **Friends TV Show Emotions** (emotion-detection-1.0)
   - Original: 7 emotions → Mapped to project labels
   - Translated: English → French (OPUS-MT)

2. **GoEmotions Dataset** (Google)
   - Original: 28 emotions → Consolidated to 7
   - Translated: English → French
   - 50,000+ sentences

3. **Synthetic French Dataset**
   - AI-generated French reality TV dialogues
   - Contextually augmented using CamemBERT

4. **Pipeline Output Dataset**
   - Real French TV transcripts
   - Manual emotion labeling
   - La Villa, reality shows

5. **Custom Augmented Data**
   - EasyDataAugmenter (TextAttack)
   - Contextual word substitution
   - Target: 5,000 samples per class

### Data Augmentation Strategy

```python
# CamemBERT-based contextual augmentation
aug = naw.ContextualWordEmbsAug(
    model_path='camembert-base',
    action="substitute",
    device='cuda'
)

# Balance classes to 5,000 samples each
TARGET_SIZE = 5000
```

**Final Training Set:** 35,000 sentences (5,000 per emotion)  
**Test Set:** 3,918 sentences (stratified)

## 🔍 Explainable AI (XAI)

### LIME Analysis

**Local Interpretable Model-Agnostic Explanations** reveal:

1. **Model Bias:** Strongly learned "disgust vs NOT disgust"
2. **Punctuation Over-reliance:** 
   - Question marks (?) → assumes "surprise"
   - Exclamation marks (!) → assumes "happiness" or "anger"
3. **Idiom Weakness:** Breaks French idioms into individual words
   - "hors de moi" (beside myself) → misses anger cue
   - "Tu vas voir!" (You'll see!) → doesn't recognize as threat

### Attention Visualizations

**Attention maps** show the model focuses on:
- ❌ Common grammatical words (je, tu, est, ce, que)
- ❌ Punctuation marks excessively
- ✅ Some intensity words (beaucoup, très)
- ⚠️ Fails to focus on key emotion keywords

### Key Findings

**Most Common Misclassifications:**
1. Neutral ↔ Happiness
2. Anger ↔ Surprise (due to question marks)
3. Disgust ↔ Anger

**Performance by Sentence Length:**
- Short (1-3 words): Good performance
- Medium (4-9 words): Moderate performance
- **Long (10+ words): 60% error rate** ⚠️

## 🛠️ Technical Implementation

### Core Technologies

**NLP & Deep Learning:**
- transformers (Hugging Face)
- PyTorch
- CamemBERT (camembert-base)
- MarianMT (Helsinki-NLP/opus-mt)

**Speech Processing:**
- AssemblyAI API
- Whisper (OpenAI)
- spaCy (French NLP)

**Data Processing:**
- pandas, NumPy
- scikit-learn
- NLTK, TextBlob-FR

**Explainability:**
- LIME
- Attention visualization
- Gradient-based methods

**Augmentation:**
- nlpaug (contextual augmentation)
- TextAttack (EasyDataAugmenter)
- Google Translate API

### Model Iterations Tested

| Model | Architecture | Accuracy | Notes |
|-------|-------------|----------|-------|
| Logistic Regression + Naive Bayes | Classical ML | ~45% | Baseline |
| RNN | Recurrent NN | ~52% | Better context |
| LSTM | Long Short-Term Memory | ~58% | Improved memory |
| **CamemBERT** | **Transformer** | **63.09%** | **Selected** ✅ |

## 📂 Folder Descriptions

### `/nlp_pipeline`
**Main implementation notebooks and scripts**
- `NLP_emotion_detection_pipeline.ipynb` - Complete end-to-end pipeline
- `run_pipeline.py` - Production script
- `requirements.txt` - Python dependencies

### `/data_preprocessing`
**Data cleaning and preparation workflows**
- Dataset-specific preprocessing notebooks
- Feature selection and engineering
- Class balancing techniques
- Confusion matrix analysis for data quality

**Key Files:**
- `emotion_detection_dataset_processing.ipynb` - Friends dataset
- `go_emotions_dataset_processing.ipynb` - GoEmotions processing
- `solving_class_imbalance.ipynb` - Augmentation strategies
- `feature_selection_finalized.ipynb` - Feature engineering

### `/datasets`
**Training and test datasets**
- `balanced_classes_dataset` - 5K samples per class
- `final_dataset` - Production training set (35K sentences)
- `go_emotions_dataset` - Google's 28-emotion dataset
- `synthetic_emotion_dataset` - AI-generated French sentences
- `emory_nlp_ds` - Friends TV show emotions
- `df_gotranslated` - Translated versions
- `custom_embeddings` - Fine-tuned word vectors

### `/models`
**Trained model files and architectures**
- `best_lstm_model.h5` - LSTM baseline
- `best_rnn_model.h5` - RNN baseline
- `LR_NB` - Classical ML models
- `Transformers` - CamemBERT final model
- `Y2C_model_iteration_log` - Training history

**Model Files:**
- Saved model weights (.h5, .pt)
- Tokenizer configurations
- Label encoders

### `/error_analysis`
**Comprehensive model diagnostics**

Contains detailed analysis with 19 artifacts:
- `Error_analysis.ipynb` - Complete error analysis notebook
- `error_analysis_Camembert.md` - Written error analysis report
- Confusion matrices
- LIME explanation visualizations (5 examples)
- Attention map heatmaps (5 examples)
- Performance metrics by class
- Misclassification rate analysis
- Sentence length distribution impact

**Key Insights:**
- 60% error rate for 10-word sentences
- Neutral/Happiness most confused
- Anger hardest to detect (60% misclassification)

### `/machine_translation`
**French ↔ English translation**
- `machine_translation.ipynb` - Translation implementation
- Uses Helsinki-NLP OPUS-MT models
- GPU-accelerated batch translation
- Translation quality scoring

**Models Used:**
- `opus-mt-en-fr` (English → French)
- `opus-mt-fr-en` (French → English)

### `/transcript-data`
**Video transcription outputs**
- `transcribed_data_assemblyAI` - AssemblyAI transcripts (5.07% WER)
- `transcribed_data_whisper` - Whisper transcripts (7.04% WER)
- `speech_to_text_*.ipynb` - Transcription notebooks
- `la_villa_s5e68` - Sample French reality TV data

**Contains:**
- Raw transcriptions
- Timestamped sentences
- Speaker identification (where available)

### `/WER-calc`
**Word Error Rate calculations**
- `STT_Assembly.xlsx` - AssemblyAI evaluation
- `STT_Whisper.xlsx` - Whisper evaluation
- `Tokens_and_WER_calc.ipynb` - WER computation

**Methodology:**
- SpaCy French tokenization
- Levenshtein distance
- Manual ground truth comparison

### `/xai_transformers`
**Explainable AI implementations**
- `XAI_for_Transformers.pdf` - Theory documentation
- `Part_1_Gradient_x_Input.ipynb` - Gradient-based attribution
- `Part_2_Conservative_Propagation.ipynb` - Layer-wise relevance
- `Part_3_Input_Perturbation.ipynb` - LIME implementation
- Attention mechanism analysis
- Test sentences for XAI evaluation

### `/model_card`
**Model documentation and metadata**
- `modelcard.md` - Complete model card (dataset, training, eval)
- Performance visualizations
- Training curves
- Confusion matrices
- Class distribution charts

### `/prompt_engineering`
**LLM-based experiments**
- `prompt_engineering.ipynb` - GPT/Claude emotion detection
- Iteration notebooks
- Prompt optimization strategies
- Comparison with fine-tuned models

### `/presentation`
**Client deliverables**
- `Final_Presentation.pdf` - Project showcase for Content Intelligence Agency

## 🎥 How to Use the Pipeline

### Quick Start

```bash
# 1. Install dependencies
pip install -r nlp_pipeline/requirements.txt

# 2. Set up API keys
export ASSEMBLYAI_API_KEY="your_key_here"

# 3. Run the pipeline
python nlp_pipeline/run_pipeline.py --input video.mp4
```

### Step-by-Step Usage

**1. Transcribe Video**
```python
import assemblyai as aai

aai.settings.api_key = "your_key"
config = aai.TranscriptionConfig(language_code="fr")
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("video.mp4", config=config)
sentences = extract_sentences(transcript.text)
```

**2. Classify Emotions**
```python
from transformers import CamembertForSequenceClassification, CamembertTokenizer

model = CamembertForSequenceClassification.from_pretrained('./models/Transformers')
tokenizer = CamembertTokenizer.from_pretrained('camembert-base')

inputs = tokenizer(sentence, return_tensors="pt")
outputs = model(**inputs)
emotion = label_encoder.inverse_transform([outputs.logits.argmax()])
```

**3. Get Explanations (Optional)**
```python
from lime.lime_text import LimeTextExplainer

explainer = LimeTextExplainer(class_names=emotion_labels)
explanation = explainer.explain_instance(sentence, predict_fn)
explanation.show_in_notebook()
```

## 📈 Model Training Process

### Data Preparation

1. **Collection:** Combined 5 diverse datasets
2. **Translation:** English → French using OPUS-MT
3. **Cleaning:** Removed duplicates, handled missing values
4. **Balancing:** Augmented to 5,000 samples per class
5. **Splitting:** 80/20 train/validation split

### Training Pipeline

```python
# Fine-tune CamemBERT
model = CamembertForSequenceClassification.from_pretrained(
    'camembert-base', 
    num_labels=7
)

optimizer = AdamW(model.parameters(), lr=2e-5, weight_decay=0.01)

# Train with early stopping
for epoch in range(15):
    train_loss = train_epoch(model, train_loader)
    val_loss = validate(model, val_loader)
    
    if early_stopping_triggered:
        break

model.save_pretrained('./models/camembert_model_6')
```

### Evaluation Metrics

- Accuracy, Precision, Recall, F1-Score
- Confusion matrix analysis
- Per-class performance breakdown
- Error rate by sentence length

## 🔬 Error Analysis Insights

### What the Model Does Well ✅

1. **Happiness Detection:** 87.5% recall - excellent
2. **Neutral Precision:** 77.7% - when it says neutral, it's usually right
3. **Positive Emotions:** Generally strong performance
4. **Short Sentences:** Good accuracy on 1-5 word sentences

### What Needs Improvement ⚠️

1. **Negative Emotions:** Struggles with anger (41% recall), sadness (47%)
2. **Idioms:** Doesn't understand French expressions as phrases
3. **Punctuation Bias:** Over-relies on ! and ?
4. **Long Sentences:** 60% error rate for 10+ word sentences
5. **Subtle Emotions:** Misses implicit emotional cues

### Common Errors

**Confusion Pairs:**
- Neutral → Happiness (over-predicts happiness)
- Anger → Surprise (due to question marks)
- Disgust → Anger (similar negative valence)

## 🚀 Production Deployment

### Requirements

```txt
# Core Dependencies
torch==2.0.1
transformers==4.36.0
assemblyai==0.17.0
pandas==1.5.3
numpy==1.24.3
scikit-learn==1.3.0

# NLP Tools
spacy==3.5.3
fr-core-news-sm==3.5.0
textblob==0.17.1
textblob-fr==0.2.0
nltk==3.8.1

# Explainability
lime==0.2.0.1

# Augmentation
nlpaug==1.1.11
textattack==0.3.8

# Translation
googletrans==4.0.0rc1

# Visualization
matplotlib==3.7.1
seaborn==0.12.2

# GPU Support
cudatoolkit==11.8
```

## 📊 Business Impact

### For Content Intelligence Agency

**Value Delivered:**
- **Time Savings:** Hours of manual tagging → Minutes of automated analysis
- **Scalability:** Process entire seasons of TV shows automatically
- **Insights:** Emotional arc tracking, audience engagement prediction
- **Monetization:** Content categorization, highlight generation

### Use Cases

1. **Content Categorization:** Auto-tag emotional tone
2. **Highlight Reels:** Find peak emotional moments
3. **Audience Analytics:** Predict viewer engagement
4. **Marketing:** Create emotion-targeted promotions
5. **A/B Testing:** Compare emotional impact of different edits

## 🔮 Future Enhancements

### Short-term (1-3 months)
- [ ] Improve idiom detection with phrase-level embeddings
- [ ] Reduce punctuation bias through data augmentation
- [ ] Fine-tune on native French reality TV data
- [ ] Add emotion intensity scoring

### Medium-term (3-6 months)
- [ ] Multi-modal analysis (audio tone + text)
- [ ] Real-time streaming video analysis
- [ ] Speaker-specific emotion profiling
- [ ] API deployment for client integration

### Long-term (6-12 months)
- [ ] Expand to other languages (Spanish, Italian)
- [ ] Emotional arc visualization over episodes
- [ ] Integration with video editing software
- [ ] Predictive analytics for audience reaction

## 👤 Author

**Anastasiia Mokhonko**

- GitHub: [@AnastasiiaMokhonko234301](https://github.com/AnastasiiaMokhonko234301)
- LinkedIn: [Anastasiia Mokhonko](https://www.linkedin.com/in/anastasiia-mohonko/)
- Email: Mohonko.anastasia@gmail.com

**Academic Affiliation:**  
Data Science & Artificial Intelligence  
Breda University of Applied Sciences

## 📧 Contact

For questions, collaboration, or API access:
- Email: Mohonko.anastasia@gmail.com
- LinkedIn: [Connect with me](https://www.linkedin.com/in/anastasiia-mohonko/)

## 🙏 Acknowledgments

- **Content Intelligence Agency** for project opportunity
- **Hugging Face** for transformer models and tools
- **AssemblyAI** for speech-to-text API
- **Google** for GoEmotions dataset
- **Emory NLP** for Friends emotion dataset

---

**Project Status:** ✅ Complete  
**Model Version:** CamemBERT 6  
**Last Updated:** October 2024  

*Transforming hours of video into actionable emotional insights through state-of-the-art NLP.*