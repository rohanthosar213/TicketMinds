import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

print("=== MODEL TRAINING START ===")

# 1. Load
df = pd.read_csv('clean_tickets.csv')
print(f"Total tickets: {len(df)}")
print(df['category'].value_counts())

# 2. Numpy check - data numpy madhe convert hotay ka?
texts = df['text'].values # Numpy array
labels = df['category'].values
print(f"\nTexts type: {type(texts)} - Numpy array")
print(f"Example: {texts[0][:50]}...")

# 3. TF-IDF - Text -> Number (Numpy Matrix)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text']) # Sparse matrix (Numpy cha prakar)
y = df['category']

print(f"\nTF-IDF Matrix Shape: {X.shape}")
print(f"Means: {len(df)} tickets x {X.shape[1]} words")

# 4. Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTrain: {X_train.shape[0]}, Test: {X_test.shape[0]}")

# 5. Train Model
model = MultinomialNB()
model.fit(X_train, y_train)
print("\nModel trained!")

# 6. Test & Accuracy - Numpy round vapraycha
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)
print(f"\nAccuracy: {np.round(acc*100, 2)}%")

print("\nReport:")
print(classification_report(y_test, preds))

# 7. Save - He pudhchya step sathi lagel
joblib.dump(model, 'ticket_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("\nSaved: ticket_model.pkl + vectorizer.pkl")

# 8. Live Test - 3 tickets var
print("\n=== LIVE TEST ===")
test_tickets = np.array([
    "refund my double payment",
    "app is crashing after update",
    "please add dark mode feature"
])

test_vec = vectorizer.transform(test_tickets)
test_preds = model.predict(test_vec)

for t, p in zip(test_tickets, test_preds):
    print(f"Ticket: '{t}' -> Predicted: {p}")

print("\n=== TRAINING DONE ===")