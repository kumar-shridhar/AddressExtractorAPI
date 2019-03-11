from flask import Flask
from flask import jsonify
from postal.parser import parse_address
import spacy

app = Flask(__name__)


@app.route('/')
def hello():
    return "Address Extractor. Please put a query in the link "

@app.route('/<user_input>')
def address_parser(user_input):
	nlp = spacy.load('nl_core_news_sm')
	doc = nlp(user_input)
	sample_list = []
	for entity in doc.ents:
		sample_list.append(entity.text)

	text_lib = ' '.join(sample_list)

	return jsonify(parse_address(text_lib))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8081)