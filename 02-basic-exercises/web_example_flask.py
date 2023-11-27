# pip install flask
import flask

app = flask.Flask("my app")


@app.route("/")  # Main site page
async def main_page():
    return "Hello World"


if __name__ == "__main__":
    app.run()
