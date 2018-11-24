from flask import Flask, render_template
from gitRetrieval import generate_info

app = Flask(__name__)

@app.route("/generate/info")
def get_info():
    languages_json = generate_info("adamlkl")
    return languages_json

@app.route("/")
def display_info():
    return render_template('visual.html', name=None)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
