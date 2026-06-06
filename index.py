from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        i = int(request.args.get('i'))
        j = int(request.args.get('j'))

        result = i + j

        return jsonify({
            "i": i,
            "j": j,
            "sum": result
        })

    except (TypeError, ValueError):
        return jsonify({
            "error": "Please provide valid integers for i and j"
        }), 400

if __name__ == '__main__':
    app.run(debug=True)