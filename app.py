from flask import Flask, request

app = Flask(__name__)

@app.route('/calc')
def calc():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return str(a + b)

app.run(debug=True)
