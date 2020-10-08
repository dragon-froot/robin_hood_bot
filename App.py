from flask import Flask
from flask import jsonify, render_template
from flask_cors import CORS
# import robin_stocks as r
# from Stock import Stock
# from Option import Option


app = Flask(__name__)
app.config.from_object(__name__)

#enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=["GET"])
def home():
    return "Hello thtere"

if __name__ == "__main__":
    app.run(debug=True)
    




