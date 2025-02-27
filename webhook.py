from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge', ''), 200
    elif request.method == 'POST':
        print(request.json)
        return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run(port=8080)