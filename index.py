from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    # Support both GET (query params) and POST (JSON body)
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        i = data.get('i')
        j = data.get('j')
    else:
        i = request.args.get('i')
        j = request.args.get('j')

    try:
        i = int(i)
        j = int(j)
    except (TypeError, ValueError):
        return jsonify({
            "error": "Please provide valid integers for i and j"
        }), 400

    result = i + j

    return jsonify({
        "i": i,
        "j": j,
        "sum": result
    })


if __name__ == '__main__':
    app.run(debug=True)