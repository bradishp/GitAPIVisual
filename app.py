import sys
from flask import Flask, render_template
from gitRetrieval import generate_info, get_minor_languages, get_languages_appearences
import json

major_languages = None
minor_languages = None

app = Flask(__name__)

@app.route("/username")
def get_username():
    global username
    return json.dumps(username)

@app.route("/appearences")
def get_number_of_appearences():
    number_of_appearences = get_languages_appearences()
    return number_of_appearences

@app.route("/other/generate/info")
def get_minor_language_info():
    global minor_languages
    if minor_languages:
        return minor_languages
    minor_languages = get_minor_languages()
    return minor_languages

@app.route("/other")
def display_minor_language_info():
    return render_template('visualOther.html', name=None)

@app.route("/generate/info")
def get_info():
    global username
    global major_languages
    if major_languages:
        return major_languages
    major_languages = generate_info(username)
    return major_languages

@app.route("/")
def display_info():
    return render_template('visual.html', name=None)
    

if __name__ == "__main__":
    username = ""
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else: 
        username = "mbostock"  # Default value
    app.run(host='0.0.0.0',port=5000,debug=True)