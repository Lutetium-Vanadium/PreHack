from flask import Flask, render_template
import os

app = Flask("__main__", template_folder=os.path.abspath("./static"))

@app.route("/")
def frontend():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()