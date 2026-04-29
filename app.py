from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)

    if data.get("action") == "buy":
        print("BUY EXECUTED")

    if data.get("action") == "sell":
        print("SELL EXECUTED")

    return "ok"

app.run(host='0.0.0.0', port=10000)
