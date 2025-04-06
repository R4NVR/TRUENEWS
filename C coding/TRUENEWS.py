import pandas as pd

# Load the TSV (tab-separated values) file
train_df = pd.read_csv("liar_dataset/train.tsv", sep='\t', header=None)

# Assign column names (as per documentation)
train_df.columns = [
    "label", "statement", "subject", "speaker", "speaker_job", "state", "party",
    "barely_true_counts", "false_counts", "half_true_counts", "mostly_true_counts",
    "pants_on_fire_counts", "context"
]
print(train_df.head())       # First few rows
print(train_df['label'].value_counts())  # Label distribution
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

train_df['clean_statement'] = train_df['statement'].apply(clean_text)
def label_group(l):
    return 'fake' if l in ['false', 'pants-fire', 'barely-true'] else 'real'

train_df['binary_label'] = train_df['label'].apply(label_group)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(train_df['clean_statement'])
y = train_df['binary_label']  # or use 'label' for multi-class

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))
