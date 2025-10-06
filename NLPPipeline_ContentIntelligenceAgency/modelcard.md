# Camembert 6 Model Card

## 1. Model Overview
Camembert 6 is a pretrained Hugging Face transformer model, based on the CamemBERT architecture, a RoBERTa-based transformer language model with 110 million trainable parameters. The model was trained for recognising and classifying 6 core emotions + neutral (happiness, sadness, fear, disgust, anger, and surprise), specifically developed for the French language. 

- Input: Short text string, such as a question, a prompt, a transcript, etc. whose emotion is to be classified.
- Output: A probability distribution over the 6 core emotions + neutral.

### Technicalities:
- Base Model: CamemBERT
- Pretrained weights: camembert-base
- Classifier Head: A linear layer on top of the pooled [CLS] output for 7-class classification.
- Hidden Size: 768
- Number of Layers: 12 Transformer blocks
- Attention Heads per Layer: 12
- Max Sequence Length: 128 tokens
- Dropout: 0.1 in embeddings and attention layers
- Activation Function: GELU

### Development Context
Due to time contraints, the data used was translated from English to French, which might fail to properly capture the essence of the language. This has been appropriately addressed in the Error Analysis part of the pipeline.[https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%208/Task_8.md]
The model leverages the pretrained weights of camembert-base, a robust French language model, providing a strong foundation for understanding French text. The classifier head was specifically designed for a 7-class emotion classification task (6 core emotions + neutral).

The training resources available included standard computational infrastructure suitable for fine-tuning transformer models of this size. The development conditions involved a standard machine learning workflow, including data preprocessing, model fine-tuning, and evaluation.

A key assumption during development was that translated data, despite potential limitations, would still provide sufficient signal for the model to learn to classify basic emotions in French. However, the "Language diversity and multilingual challenges" section of the model card acknowledges the potential impact of this assumption on the model's ability to handle subtle emotional expressions and culturally specific language.

## 2. Intended Use
The  model is intended to be used in film, series, TV-shows, and video analysis by classifying transcripted sentences into the aforementioned emotions. Its primary function is to support the Content Intelligence Agency in analyzing audiovisual media.
### Primary applications:
- Emotion tagging of video transcripts: Automatically label each line of dialogue in a video with its corresponding emotion
- Enhancing content insights: Help media makers understand emotional trends across characters, scenes, or full productions.
- Supporting editorial decisions: Enable editors, producers, and content creators to tailor content based on emotional pacing or intensity, while keeping their intended audience and desired emotional outcome in mind.

### Pipeline context:
- Speech-to-text transcription: Transcribes audio input from any type of media.
- Machine translation: French to English.

## 3. Dataset Details
### Training and Validation:
The training corpus is comprised of 3 datasets that have been preprocessed and concataned as following:
1. Emotion Detection dataset (12,606 instances), which contains phrases from the American TV show 'Friends'. The phrases were translated from English to French, with the emotion labels (Neutral, Joyful, Peaceful, Powerful, Scared,Mad, and Sad) being renamed to fit into our classes. The only columns kept were 'Sentence' and 'Emotion'. [https://github.com/emorynlp/emotion-detection].
2. Synthetic dataset generated with ChatGPT(GPT-4o) (3000 instances) containing only phrases labeled as 'sadness', 'disgust', and 'surprise' to help balance the classes.
3. Google AI GoEmotions dataset (46000 instances). The data was incorporated already preprocessed (NaN or missing values were deleted, duplicates were deleted). The GoEmotions dataset consists of comments from Reddit users with labels of their emotions. The data was translated from English to French. [https://www.kaggle.com/datasets/shivamb/go-emotions-google-emotions-dataset].

After concatanating the datasets, the data was augmented again using Text Attack, generating instances for the classes with less than 9000 instances. The file is named 'balanced_classes_dataset.csv'. The labels were encoded and the sentences were tokenized appropriately. 

The **validation dataset** is comprised of 20% of the training data (train_test_split).

### Testing:
The test set was sepparately curated. It is comprised of transcribed data from two different French TV reality shows ('La Ville' and 'Les Marseillais en Australie'), containing the Sentence and Emotion features.

### Language diversity and multilingual challenges
Much of the dataset has been translated from English to French due to time constraints. This implies loss of nuance in context, where emotions like sarcasm or culturally specific expressions may be lost. Additionally, original emotion labels from external datsets may not propelry mach the tone found in the pipeline output dataset.
Another challenge is the domain and dialect variation, as France varies by region and formality. This diversity helps generalizability but also increases risk of domain mismatch during inference.

## 4. Performance Metrics and Evaluation
Camembert 6 exhibits a tendency to confuse the 'neutral' and 'happiness' emotion categories, as well as 'disgust' and 'anger'. Despite 'neutral' being the most frequent class in the test data, the model struggles to accurately classify it, often mispredicting it as other emotions. Conversely, 'happiness' tends to be over-predicted. The model shows the highest misclassification rate for 'anger'. Analysis using LIME suggests the model has strongly learned to differentiate 'disgust' from other emotions, sometimes prioritizing this distinction over the actual expressed emotion. Furthermore, the model appears to rely heavily on individual keywords and surface-level cues like question marks and exclamation points, and it struggles with understanding the emotional context conveyed through phrases and idioms. Sentence length also impacts performance, with misclassification rates increasing with longer sentences. The frequent occurrence of common, non-emotion-specific words in misclassified examples indicates a potential over-reliance on structural elements rather than nuanced emotional vocabulary.
A more comprehensive error analysis can be found here [https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%208/Task_8.md]. 

## 5. Explainability and Transparency
To enhance transparency in our CamemBERT-based emotion classifier, we applied multiple Explainable AI (XAI) techniques to interpret how the model makes decisions and to ensure it relies on emotionally meaningful cues. A more in-depth analysis can be found here [https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/task%209/Task_9_Explainable_AI_(XAI)_for_Transformers.pdf].

### Part 1: Basic Explanation with Gradient × Input
This method revealed initial insights by highlighting tokens that contributed most to the model’s output through the product of gradients and inputs. Although informative, the results were occasionally noisy, attributing relevance to non-emotive or structurally irrelevant tokens. For instance, punctuation or auxiliary verbs sometimes received high 
relevance, raising concerns about interpretability.

![Gradiend and Input Relevance](./image_1.png)

*This plot is showing token relevance for the sentence “Comment quelqu’un peut-il supporter ça ?”*
### Part 2: Improved Explanation with Conservative Propagation(Layer-wise Relevance Propagation)
To improve interpretability, we implemented Conservative Propagation as proposed by Ali A. et al. (2022). This method propagates relevance scores through the attention mechanism more faithfully, highlighting a more human-aligned distribution of importance. 
- Emotionally charged tokens like 'supporter', 'drôle', and 'arriver' were consistently identified. 
- Attention heatmaps revealed that the model focused on syntactically and semantically connected terms.

![LRP Surprise](./image_2.png)
*(a) Conservative LRP bar plot*

![Attention scores heatmap](./image_3.png)
*(b) attention heatmap*

Side-by-side view of: (a) Conservative LRP bar plot and (b) attention heatmap for “Je ne peux pas croire que cela vient d’arriver!”

### Part 3: Model Robustness with Input Perturbation
We assessed how the model’s confidence changed when the least relevant tokens were removed:
- **Disgust** sentences showed a sharp drop in confidence after removing a few key tokens → strong token dependence.
- **Happiness** and **Surprise** examples were more robust, indicating distributed reliance across multiple words.

![Confidence drop Disgust](./image_4.png)
![Confidence drop Happiness](./image_5.png)
![Confidence drop Surprise](./image_6.png)
Line plots showing prediction confidence drop across token removals.

## 6. Recommendations for Use
The model has been fine-tuned to classify emotions in short, sentence-level French text. Therefore, the quality of the input text significantly affects output reliability. Preprocessing steps such as correcting transcription errors, cleaning filler words, and properly punctuating sentences are essential to maintain consistency with the kind of data the model was trained on.

Because Camembert 6 is trained specifically for the French language, it is not designed to process other languages natively. If working with multilingual content, users should ensure that any non-French text is accurately translated into French before passing it to the model for emotion classification. Furthermore, the model works best when applied to short, coherent segments of dialogue — such as single sentences or utterances — rather than long, unsegmented passages. In a media analysis pipeline, this aligns naturally with the structure of subtitles or transcription data from scene-level dialogue.

While the model performs reliably within its domain, there are several operational risks that users should be aware of. Domain shifts, such as data from dialects underrepresented in training (e.g., Canadian or African French), highly stylized speech (e.g., poetic forms or fantasy genres), or low-quality automatic transcripts, may cause the model’s performance to degrade. Additionally, as some of the training data was translated from English, the model may occasionally misinterpret emotional nuance when the input is generated through automated translation.

Given its training sources, which include translated TV scripts and Reddit comments, the model may show bias toward conversational tone and may underperform when analyzing more formal, literary, or culturally nuanced content.

Media companies and content stakeholders can derive significant value from Camembert 6 by applying it to scene-level emotion mapping, enabling teams to track the evolution of emotional tone across episodes or full productions. It is also particularly effective for character-level emotion profiling, helping content creators identify emotional consistency or development across a narrative. Editors and producers can leverage these insights to guide creative decisions, such as tailoring emotional pacing or adjusting key scenes to better align with intended audience responses.

Looking forward, it is recommended that the model be further developed with native French training data to reduce translation-related distortions. Fine-tuning on spoken French corpora from interviews, podcasts, or unscripted shows would also help improve its generalizability to real-world media. Additionally, expanding its capability to analyze multi-turn dialogue or emotion transitions over time could enhance its utility for deeper narrative understanding.

## 7. Safety and Reliability
### Safety
Camembert 6 is not designed for safety-critical applications and should not be used to make decisions that affect individuals' mental health, legal standing, or wellbeing. Although the emotion categories are non-sensitive, misclassification may occur, particularly in emotionally ambiguous or sarcastic inputs.

The model is vulnerable to adversarial examples, such as misleading punctuation or idiomatic expressions that shift emotional tone. It is also sensitive to sentence structure and context; isolated utterances may be misinterpreted without full conversational background.

To reduce potential harm:

Outputs should be interpreted as probabilistic suggestions, not definitive judgments.

The model should be used in supportive or exploratory roles (e.g., content analysis), not as a standalone diagnostic tool.

### Reliability
The model performs reliably on short, clean, conversational French text similar to its training data. However, it may degrade under the following conditions:

- Noisy input: Poor transcription, slang, or mixed-language sentences

- Out-of-domain content: Literary, poetic, highly stylized dialogue, or non-colocvial langauge

- Dialectal variation: Unseen regional uses of French (e.g., Canadian, African variants)

Robustness testing with token perturbation showed that emotions like disgust are heavily reliant on specific keywords, while others (e.g., surprise) are more robust to noise. See [*Explainability section*] for detailed examples.

Future improvements could include:

- Fine-tuning on spoken French data

- Testing on dialect-diverse corpora

- Incorporating uncertainty estimation (e.g., confidence thresholds for deployment)