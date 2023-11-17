from flask import Flask, jsonify

# Create a Flask web application
app = Flask(__name__)


# Define a route that returns JSON data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, World!',
        'number': 42
    }
    return jsonify(data)

@app.route('/', methods=['GET'])
def get_root():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()
