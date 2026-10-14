<div align="center">

# 🎫 TicketMind
### AI-Powered Customer Support Ticket Classification & Reply Assistant

**Turn incoming support messages into organized tickets and helpful draft replies.**

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/NLP-TF--IDF%20%7C%20Scikit--learn-8A2BE2?style=for-the-badge" alt="NLP and machine learning">
  <img src="https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge" alt="Prototype">
</p>

</div>

---

## 📌 Overview

**TicketMind** is a customer-support automation prototype designed to help teams categorize incoming support requests and prepare consistent, professional responses. A user enters a ticket in the web interface and receives a predicted category and a suggested reply.

The repository includes a Flask web interface, sample ticket data, and scripts for preparing data and training a text-classification model.

> **Implementation note:** The current Flask `/predict` endpoint uses keyword-based rules in `app.py`. The TF-IDF and scikit-learn model training scripts are separate and are not currently connected to that endpoint. The project should therefore be treated as a prototype, not a production-ready AI service.

## ✨ Key Features

- **Ticket categorization** — assigns incoming messages to a support category.
- **Suggested replies** — returns a reusable response template for the detected category.
- **Simple web interface** — enter a support message and view the result in the browser.
- **Flask JSON endpoint** — provides a `/predict` route for the web UI.
- **Model-training workflow** — includes scripts using TF-IDF and scikit-learn to experiment with text classification.
- **CSV-based data workflow** — works with ticket datasets for preparation and training.

## 🗂️ Supported Categories

| Category | Example request |
|---|---|
| Billing | “I was charged twice for my order.” |
| Account | “I cannot log in to my account.” |
| Technical | “The application crashes when I open it.” |
| Feature Request | “Please add a dark mode option.” |

*The live Flask demo currently uses keyword matching, so wording that does not match its rules may be classified as a feature request.*

## 🧰 Technology Stack

| Area | Tools |
|---|---|
| Backend | Python, Flask |
| Machine learning experiments | scikit-learn, TF-IDF, Multinomial Naive Bayes, Logistic Regression |
| Data processing | pandas, NumPy |
| Model persistence | joblib |
| Frontend | HTML, CSS, JavaScript |
| Dataset | CSV |

## 🏗️ Project Structure

```text
Apptware-project/
├── app.py                    # Flask application and /predict endpoint
├── clean.py                  # Ticket data cleaning script
├── data_maker.py             # Ticket data generation script
├── model.py                  # TF-IDF + Multinomial Naive Bayes training
├── train.py                  # TF-IDF + Logistic Regression training
├── tickets.csv               # Ticket dataset
├── clean_tickets.csv         # Prepared dataset used by training scripts
├── ticket_model.pkl          # Saved model artifact (if generated)
├── vectorizer.pkl            # Saved TF-IDF vectorizer (if generated)
├── templates/
│   └── index.html            # Browser interface
└── ticket-data-project/
    ├── data_maker.py
    ├── requirements.txt
    └── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rohanthosar213-source/TicketMind-AI-Support.git
cd TicketMind-AI-Support
```

If you downloaded this project as a ZIP, extract it and open a terminal in the project folder instead.

### 2. Create and activate a virtual environment (recommended)

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

The repository does not currently include a root-level `requirements.txt`. Install the dependencies used by the application and training scripts:

```bash
python -m pip install Flask pandas numpy scikit-learn joblib
```

### 4. Run the web application

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser, enter a support ticket, and select **Classify Ticket**.

To stop the development server, press `Ctrl + C` in the terminal.

## 🧪 Train the Machine Learning Model (Optional)

The repository contains two alternative training scripts. Run them from the project root after confirming that `clean_tickets.csv` contains the columns `text` and `category`.

```bash
python model.py
```

Or:

```bash
python train.py
```

The scripts save `ticket_model.pkl` and `vectorizer.pkl`. They use different classifiers, so running one after the other overwrites those output files. **Training these files does not change the current web predictions**, because `app.py` currently uses its own keyword-based `get_prediction()` function.

## 🔌 API Reference

### `POST /predict`

Request body:

```json
{
  "text": "I was charged twice for my subscription."
}
```

Example response:

```json
{
  "category": "Billing",
  "reply": "Hi there, we understand your billing concern..."
}
```

The reply text is generated by the current rule-based demo. Exact response wording depends on the detected category.

## 🔐 Responsible Use & Limitations

- This is a learning/prototype project; review generated replies before sending them to customers.
- Do not submit passwords, payment details, or other sensitive customer information.
- The current classifier is keyword-based and may misclassify ambiguous or unfamiliar messages.
- The Flask app currently runs with `debug=True`; disable debug mode and add production-grade configuration before deployment.
- Add input validation, automated tests, logging, security controls, and monitoring before any real-world use.
- Model performance should be measured on a held-out dataset before reporting an accuracy score.

## 🛣️ Roadmap

- [ ] Connect the trained model and vectorizer to the Flask prediction endpoint.
- [ ] Add a maintained root-level `requirements.txt`.
- [ ] Add automated tests for category predictions and API responses.
- [ ] Improve validation and error handling for empty or malformed requests.
- [ ] Add confidence scores and a human-review fallback for uncertain predictions.
- [ ] Prepare a production deployment configuration.

## 👨‍💻 Author

**Rohan Thosar**

- GitHub: [@rohanthosar213-source](https://github.com/rohanthosar213-source)
- Project: [TicketMind AI Support](https://github.com/rohanthosar213-source/TicketMind-AI-Support)

---

<div align="center">

**Built to explore practical applications of Python, NLP, and machine learning in customer support.**

</div>
