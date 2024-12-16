import nltk
import spacy
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")

nltk.download("stopwords")

def preprocess_hybrid(text):
    #print("Original input: ", text)    debug line
    text = text.lower()
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_punct]
   # print("After tokenization: ", tokens)  debug line

    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words or word in ["how", "are", "you"]]

    #print("After stopword removal: ", filtered_tokens) debug line
    return filtered_tokens