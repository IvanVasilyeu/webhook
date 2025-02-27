from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge', ''), 200
    elif request.method == 'POST':
        print(request.json)
        return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use PORT env variable or default to 8080
    app.run(host='0.0.0.0', port=port)