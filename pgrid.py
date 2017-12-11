from flask import Flask, request
import json

app = Flask(__name__)

# curl -Haccept:application/json http://localhost:5000
# curl http://localhost:5000

@app.route("/")
def json_or_text():
    res_type = request.headers.get('accept')
    if res_type == 'application/json':
        return '{"message": "Good morning"}'
    else:
        return "<p>Hello, World</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug = True)

