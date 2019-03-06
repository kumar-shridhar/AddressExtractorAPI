from flask import Flask
from flask import jsonify
from postal.parser import parse_address

app = Flask(__name__)


@app.route('/')
def hello():
    return "Address Extractor. Please put a query in the link "

@app.route('/<user_input>')
def address_parser(user_input):
	
    
    return jsonify(parse_address(user_input))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8081)