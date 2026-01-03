import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_txt(text):
    #Lower case the text
    text = text.lower()

    text = re.sub(r'\n', ' ', text) # Remove new line characters
    text = re.sub(r'\s+', ' ', text) # Remove extra whitespace
    text = re.sub(r'\d+', '', text) # Remove numbers
    text = re.sub(r'[^a-zA-Z ]', '', text) # Remove special characters
    text = text.strip() # Remove leading/trailing whitespace

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word not in stop_words)

    return   