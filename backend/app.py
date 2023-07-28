from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def index_file(path):
    return app.send_static_file(path)

@app.route("/headers", methods=["GET"])
def headers():
    headers = request.headers
    return jsonify(dict(headers))

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
