import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook_verification():
    VERIFY_TOKEN = '101185'

    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode and token == VERIFY_TOKEN:
        print("WEBHOOK VERIFIED")
        return challenge, 200
    else:
        return '', 403


# Step 2: Handle Events
@app.route('/webhook', methods=['POST'])
def handle_events():
    body = request.json
    print("Received Webhook:", json.dumps(body, indent=2))

    # Handle different event types here

    return json.dumps(body, indent=2), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use PORT env variable or default to 8080
    app.run(host='0.0.0.0', port=port)