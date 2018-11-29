import sys
from flask import Flask, render_template
from gitRetrieval import generate_info, get_minor_languages

username = ""

app = Flask(__name__)

@app.route("/generate/info")
def get_info():
    global username
    languages_json = generate_info(username)
    return languages_json

@app.route("/")
def display_info():
    return render_template('visual.html', name=None)
    

if __name__ == "__main__":
    global username
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else: 
        username = "mbostock"  # Default value
    app.run(host='0.0.0.0',port=5000,debug=True)