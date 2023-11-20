from flask import Flask, jsonify

# Create a Flask web application
app = Flask(__name__)


# Define a route that returns JSON data
@app.route('/current_design', methods=['GET'])
def get_daily():
    data = {
        'design': 'running_text',
        'settings': {
            'led-rows': 64,
            'led-cols': 64,
            'led-slowdown-gpio': 4,
            'led-brightness': 20,
        }
    }
    return jsonify(data)


@app.route('/design/<design>', methods=['GET'])
def get_design(design):
    # get design file from designs/design_name
    # return design file
    try:
        file = open("api/designs/" + design + ".py", "r")
        return file.read()
    except FileNotFoundError:
        return "Design not found"


@app.route('/', methods=['GET'])
def get_root():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()
