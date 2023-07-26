from flask import Flask

app = Flask(__name__, template_folder="static", static_folder="static")


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def index_file(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    print(app.url_map)
    app.run()
