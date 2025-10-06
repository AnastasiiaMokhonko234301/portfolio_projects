# Error analysis for Camembert 6
## All tables, figures, and results can be found in this [notebook](https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%208/Error%20analysis.ipynb)
This file is meant to share and discuss the results following the error analysis of the final model (Camembert 6). More information about the model can be found in [its model card ](https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%2010/modelcard.md).

The dataset used for this analysis is the final test dataset, comprised of 3918 entries, differing per class:

| Emotion |  | 
| -------- | -------- | 
| neutral   | 981   | 
| happiness   | 754   |
| surprise   | 585   |
| anger   | 445   |
| sadness   | 419   |
| disgust   | 380   |
| fear   | 354   |

More information about how this dataset was compiled can be found in the [model card](https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%2010/modelcard.md).

---
Following the output of the analysis, the following conclusions have been drawn.

### Overall insights
Camembert 6 is predominently confusing the classes 'neutral' and 'happiness', as well as 'disgust' and 'anger' (as per *[Error Analysis notebook, section b, subsection 'Common misclassifications](https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%208/Error%20analysis.ipynb)*). This can also be derived from *figure 0* *figure 1*, where we can see that the number of predicted labels for the 'happiness' class was 1046, even though the class has a total of 754 instances. Even tough the 'neutral' class has the most instances out of all the other classes (*figure 1*), the model still has trouble classifying it.

![Confusion matrix](./Confusion_matrix.png)
*figure 0*

![Distribution of predicted and true labels](./Distribution_of_predicted_and_true_labels.png)
*figure 1*

- the model misclassifies anger the most, with a rate of almost 0.6. Sadness is second.

Even so, Camembert 6 still misclassifies 'anger' the most, with a misclassification rate of 0.6 (*figure 2*)
Relative_missclassification_rate_per_emotion_class
![Relative missclassification rate per emotion class](./Relative_missclassification_rate_per_emotion_class.png)
*figure 2*


### LIME Explanations
After performing LIME(Local Interpretable Model-Agnostic Explanations) analysis on 10 randomly selected misclassified sentences, a very interesting outcome was found. The model has most litely learned to strongly differentiate between 'disgust' and 'NOT disgust'. This was derived from the fact that all 10 examples were shwoing the weights for words associated with either one of the two situations. This has been exemplified using *figures 3, 4, and 5*.
This could mean that the model's internal weights and representations have been optimized to identify patterns that separate "disgust" from everything else. These patterns (specific words, phrases, or even stylistic elements) become the most influential features in its decision-making process, regardless of the actual emotion being expressed.

On the other hand, in cases where the emotional meaning is conveyed through a phrase or idiom (e.g., "hors de moi" (*figure 3*), "Tu vas voir ce que tu vas voir!" (*figure 6*)), LIME tends to highlight individual words within the phrase. This indicates a potential weakness in understanding multi-word expressions and their holistic emotional content.

Exclamations and words indicating intensity (e.g.,"beaucoup" (*figure 7*)) seem to point he model to sometimes associate this intensity with emotions like fear or happiness, even when the underlying emotion is different (e.g., sadness or anger). This suggests a possible confusion between the strength of an emotion and its specific type. 

Common words like pronouns ("Je," "Tu," "me"), articles ("la," "le," "un"), and auxiliary verbs ("suis," "vas") sometimes appear in the LIME explanations with significant weights. Additionally, the high frequency of words like "je," "est," "ça," "suis," "ce," "que," "c'," "tu," "de," "on," "j'," "fait," "qui," "me," "ai," "le," "ne" strongly suggests that these words, while essential for sentence structure, often lack strong inherent emotional meaning on their own. (*[Error Analysis notebook, section e](https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%208/Error%20analysis.ipynb)*). Their frequent appearance in misclassified examples suggests the model might be relying on their co-occurrence patterns with other words, potentially leading to incorrect classifications when those patterns are ambiguous or context-dependent.

In *figure 4*, we can derive observe that the negation "ne...plus" is highlighted with a negative weight towards disgust (the true label). This suggests the model correctly identifies the role of negation in altering the sentiment, but in this case, not strongly enough to overcome other cues leading to "sadness.". This is also reinforced by the presence of "quoi" and "pas" in the top words (*[Error Analysis notebook, section e](https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%208/Error%20analysis.ipynb)*). This indicates the model's sensitivity to negation and interrogative structures, which, as seen in the attention maps (attention to "?"), can sometimes lead to misclassifications (e.g., confusing anger with surprise).

Coincidently, even when the predicted label is the same across different examples (e.g., fear, happiness - depicted in the *[Error Analysis notebook, section d, subsection LIME analysis](https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%208/Error%20analysis.ipynb)*), the specific words highlighted by LIME vary. This suggests that the model might be arriving at the same incorrect prediction through different reasoning pathways based on the surface-level features of each sentence.

Overall, the types of errors observed (e.g., confusing anger with surprise based on question marks, or misinterpreting idioms) might reflect biases or limitations in the training data. Certain emotional expressions or linguistic structures might be underrepresented or ambiguously labeled.

![Lime classif ex 1](./lime_1.png)
*figure 3*

*Translation: I am beside myself!*

![Lime classif ex 2](./lime_2.png)
*figure 4*

*Translation: I'm disgusted, I don't want to hear about you anymore.*

![Lime classif ex 3](./lime_3.png)
*figure 5*

*Translation: What's going on, damn it?*

![Lime classif ex 4](./lime_4.png)
*figure 6*

*Translation: You'll see what you're going to see!*

![Lime classif ex 4](./lime_5.png)
*figure 7*

*Translation: I feel so alone here.*

### Attention maps
Attention maps for the first attention head in the last layer of the CamemBERT model selected only for the misclassifications of 'anger' were also used in this analysis. The sentences used for this were randomly selected. They can be found in the *[Error Analysis notebook, section d, subsection 'Attention maps'](https://github.com/BredaUniversityADSAI/2024-25c-fai2-adsai-group-group10_french_y2c/blob/main/Task%208/Error%20analysis.ipynb)*. This has helped gain shed light on the reasoning of the model. 
The overall conclusion of the maps and a possible explanation for the misclassifications is a lack of strong attention to obvious 'anger' keywords. Across several examples, there isn't consistently strong attention focused on words that humans might immediately associate with anger (though French-specific nuances need consideration). For instance, in *figure 8*, the attention seems distributed rather than heavily focused on "stupide" as a potential indicator of frustration or anger.
Examples ending in question marks (*figure 8, figure 9*) often show strong attention towards the question mark itself and the words immediately preceding it. This might be a reason for misclassification as "surprise," as questioning can be associated with that emotion. Similarly, the exclamation mark in *figure 11* and *figure 12* attracts significant attention, but doesn't consistently lead to the correct "anger" classification. Exclamations can also be associated with other emotions.
Therefore, the model might be over-relying on surface-level cues like question marks and exclamation points, which can be associated with multiple emotions, leading to confusion with "surprise" or other categories.

Additionally, we can see in *figure 12* that the sentence is quite ambiguous without more context. The model's prediction of "happiness" might be based on a superficial interpretation of "beaucoup avec Julie" without understanding the underlying frustration or annoyance implied (which leads to the "anger" label). The attention map doesn't reveal a clear focus on any specific "anger" cues, possibly because they are more implicit.

![Attention map ex 1](./attention_map_1.png)
*figure 8*

*Translation: Do you think I'm stupid or what?*

![Attention map ex 2](./attention_map_2.png)

*figure 9*

*Translation: Are you serious right now?!*

![Attention map ex 3](./attention_map_3.png)
*figure 10*

*Translation: This is the last straw!*

![Attention map ex 4](./attention_map_4.png)

*figure 11*

*Translation: You lied to me from the start!*

![Attention map ex 5](./attention_map_5.png)

*figure 12*

*Translation: The guy is overdoing it with Julie.*

### Frequent words in misclassified sentences

| Top 30 words in misclassified examples: |  | 
| -------- | -------- | 
| je   | 549   | 
| est   | 347   |
| ça   | 270   |
| suis  | 251   |
| ce   | 240   |
| que   | 225   |
| c    | 223   |
| tu   | 218   |
| de   | 200   |
| on   | 179   |
| j    | 172   |
| fait | 168   |
| qui  | 163   |
| me   | 162   |
| ai   | 160   |
| le   | 160   |
| pas  | 156   |
| tout | 152   |
| ne   | 133   |
| quoi | 107   |
| un   | 102   |
| à    | 99   |
| la   | 99   |
| bien | 97   |
| et   | 94   |
| se   | 90   |
| vera | 85   |
| passe | 78   |
| ni   | 76   |
| t    | 75   |

The absence of strong, unambiguous emotion-specific keywords (like insults, words expressing intense feelings of anger, sadness, joy, etc.) in the top misclassified words is striking. This further supports the idea that the model might be struggling when the emotion is conveyed through more subtle language, idioms, or context rather than explicit emotional vocabulary. Words like "ça," "que," and "et" being frequent might indicate that the model pays attention to sentence beginnings and connectors, potentially trying to infer the overall sentiment or flow of the discourse, but sometimes misinterpreting it. 
Additionally, the presence of "ni" (neither/nor) and the contracted pronoun "t'" (you) are more grammatical. Their frequency further emphasizes the model's attention to structural elements.
The presence of "bien" (well/good) and "verra" (will see) is interesting. "Bien" can be used in sarcastic or dismissive tones, which might be relevant to anger, but it also has positive connotations. "Verra" (will see) appeared in the "Tu vas voir ce que tu vas voir !" example (*figure 6*), a threat indicative of anger. Their frequency suggests the model might be picking up on these words but failing to consistently interpret their emotional valence in different contexts.


### Misclasification rate
- the missclassification rate peaked at 0.6 for sentences with a length of ten words, starting to rise at sentence length 4.  

*Figure 13* and *figure 14* strongly suggest that the model's performance is negatively impacted by increasing sentence complexity and the potential for more intricate contextual relationships. Even relatively short sentences beyond a few words seem to introduce challenges, implying that the model's understanding of emotion is not robust to even moderate linguistic complexity. This could be because the model relies more on local word-level features rather than effectively capturing the interplay of words and phrases that contribute to the overall emotional meaning as sentences become longer.

![Attention map ex 5](./Missclassification_rate_by_Sentence_length.png)

*figure 13*

![Attention map ex 5](./Sentence_Length_Distribution.png)

*figure 14*

### 'Neutral' and 'happiness' classes being confused for each other
Although neutral had the most instances in the test data (981), it was still heavily misclassified, whereas 'happiness' (754 instances and second overall by count), was mostly correclty classified.

The contrasting performance between the "neutral" and "happiness" categories, despite their instance counts, highlights the model's sensitivity to the nature of the emotional expression. The high misclassification rate for "neutral," the most frequent class, likely stems from its role as a catch-all for subtle or weakly expressed emotions, as well as sentences lacking strong positive or negative valence. This suggests that the model struggles with the absence of clear emotional signals and might have difficulty distinguishing genuinely neutral sentences from those with faint or ambiguous emotional undertones.


### Overall performance
The overall performance metrics for the emotion classification model reveal a test loss of 1.8041 and a test accuracy of 63.09%, suggesting a moderate level of predictive capability with room for improvement in reducing prediction error and increasing overall correctness. The precision of 0.6353 indicates that when the model predicts an emotion, it is correct roughly 63.53% of the time, while a recall of 0.6309 shows that the model correctly identifies about 63.09% of all the true instances of each emotion. The balanced F1-score of 0.6264 further reflects this moderate performance.

Examining the performance across individual emotion categories highlights significant variations. The "happiness" category stands out with a high recall of 0.8753 and a strong F1-score of 0.7333, confirming that the model is adept at identifying this emotion, likely due to clearer linguistic cues. In contrast, "neutral" achieves the highest precision at 0.7772, indicating high confidence in its "neutral" predictions, but its lower recall of 0.6330 underscores the earlier observation of heavy misclassification, as the model misses a substantial portion of actual neutral instances. "Surprise" shows balanced and reasonable performance. However, the model struggles with negative emotions such as "anger," "disgust," and "sadness," all exhibiting lower recall rates (0.4090, 0.5053, and 0.4726, respectively) and F1-scores (0.4472, 0.4942, and 0.5176, respectively). Notably, "anger" has the weakest performance, with the model failing to identify a large fraction of true instances. These metrics collectively suggest that while the model has learned to recognize certain emotions like "happiness" reasonably well and is cautious when predicting "neutral," it faces considerable challenges in accurately identifying and distinguishing between other emotions, particularly the negative ones.

### Model Advantages and Disadvantages in Relation to Project Objectives

CamemBERT 6 was chosen due to its strong alignment with the project’s linguistic scope: it is a French-language RoBERTa-based transformer model, pretrained on large-scale French corpora. This makes it particularly suitable for handling the informal, conversational tone found in TV transcripts and reality show dialogue — the core domain of this project.

An advantage of this architecture is its ability to capture nuanced sentence-level meaning through contextual embeddings, which supports accurate emotion classification, especially for positive or explicit emotional statements (e.g., happiness or surprise). Its performance on short inputs is also well-suited to media subtitle analysis.

However, the model exhibits limitations when handling subtle, idiomatic, or culturally specific expressions. The error analysis reveals systematic misclassifications due to reliance on surface-level features like punctuation and intensity words, instead of deeper semantic understanding. This poses challenges in correctly labeling neutral or negative emotions, which are often implicit. The model’s struggles with 'anger' and 'disgust', and the impact of sentence length on accuracy, highlight weaknesses in robustness and generalization — important factors for real-world editorial workflows.

Overall, while CamemBERT 6 aligns well with the project's goal of providing automated emotional insights for media content, it would benefit from further domain-specific fine-tuning on native, non-translated French data and strategies to improve the handling of nuanced or ambiguous expressions.

### Bias Considerations

Several types of bias were identified during the development and evaluation of Camembert 6. First, the reliance on translated and synthetic datasets introduces **data source bias**, as translated phrases may lack natural French phrasing or cultural nuance. This can result in incorrect emotional interpretations, especially for sarcasm or idioms.

Second, despite class balancing techniques, the model still exhibits **class imbalance bias** — frequently overpredicting dominant categories such as ‘happiness’ and ‘neutral’ while underperforming on emotions like ‘anger’ and ‘disgust’.

Third, both LIME and attention map analyses revealed **lexical and syntactic bias**. The model places high weight on punctuation (e.g., exclamation and question marks) and common function words (e.g., “je,” “tu,” “ne”) that do not carry intrinsic emotional meaning. This suggests the model may rely on surface-level patterns rather than deeper semantic features, leading to misleading predictions in subtle or context-rich sentences.

These biases must be considered when interpreting outputs, especially in professional media applications where emotional mislabeling could distort narrative insights or audience profiling.


### On a positive note
Despite the challenges in specific categories, Camembert 6 demonstrates a moderately good overall accuracy of 63.09% on a multi-class emotion classification task. This indicates that it has learned to correctly identify the emotion in a significant portion of the test data, performing considerably better than random chance would.

The model shows strong performance in identifying "happiness," achieving a high recall of 0.8753 and a robust F1-score of 0.7333. This suggests that the model has effectively learned the linguistic patterns and features associated with positive sentiment and is very good at recognizing instances of happiness.

The model exhibits high precision for the "neutral" category (0.7772). This indicates that when the model predicts a sentence as "neutral," it is very likely to be correct. While it might miss some true neutral instances (lower recall), its predictions for this common category are highly reliable.

The model also demonstrates reasonable and balanced performance for "surprise," with both precision and recall around 0.68-0.70, leading to a decent F1-score. This suggests it has learned to identify and predict "surprise" with a fair degree of accuracy and consistency.