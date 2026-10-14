import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Load data
df = pd.read_csv("clean_tickets.csv")

X = df['text']
y = df['category']

# 2. Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# 3. Train
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. Save with JOBLIB (pickle nako)
joblib.dump(model, "ticket_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved with joblib - Error fixed forever!")