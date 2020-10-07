from flask import Flask
from flask import jsonify, render_template
from flask_cors import CORS
import robin_stocks as r
from Stock import Stock
from Option import Option


app = Flask(__name__)
app.config.from_object(__name__)

#enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=["GET"])
def home_route():
    positions = Stock().get_current_positions()
    
    return jsonify(positions)

@app.route('/options', methods=["GET"])
def options_route():
    options = Option().get_current_options()

    return jsonify(options) 


if __name__ == "__main__":
    r.login()
    app.run(debug=True)
    




