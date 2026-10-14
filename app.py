from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Demo model - No training needed
def get_prediction(text):
    text = text.lower()
    if "pay" in text or "bill" in text or "refund" in text or "debit" in text:
        return "Billing", "Hi there, we understand your billing concern. Our finance team is checking your transaction. The amount will be refunded in 24-48 hrs if debited. Sorry for inconvenience."
    elif "login" in text or "account" in text or "password" in text:
        return "Account", "Hello, we are looking into your account issue. Please try resetting your password or share your registered email. We will resolve this quickly."
    elif "error" in text or "not working" in text or "bug" in text or "crash" in text:
        return "Technical", "Thanks for reporting! Our technical team has noted this issue. We are fixing it on priority and will update you soon."
    else:
        return "Feature Request", "Thank you for your valuable suggestion! We have forwarded your feature request to our product team."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text','')
    cat, reply = get_prediction(text)
    return jsonify({"category": cat, "reply": reply})

if __name__ == '__main__':
    app.run(debug=True)