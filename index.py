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
        return make_json_response(success=False, error="Please provide valid integers for i and j", status=400)

    result = i + j

    return make_json_response(success=True, data={"i": i, "j": j, "sum": result})


def make_json_response(success: bool, data: dict = None, error: str = None, status: int = 200):
    payload = {"success": bool(success)}
    if success:
        payload["data"] = data or {}
    else:
        payload["error"] = error or ""

    return jsonify(payload), status


if __name__ == '__main__':
    app.run(debug=True)