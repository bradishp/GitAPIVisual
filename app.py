import sys
from flask import Flask, render_template
from gitRetrieval import GitLanguagesRetrieval


app = Flask(__name__)

@app.route("/username")
def get_username():
    global users_language_info
    return users_language_info.get_username()

@app.route("/appearences")
def get_number_of_appearences():
    global users_language_info
    return users_language_info.get_languages_appearences()

@app.route("/other/generate/info")
def get_minor_language_info():
    global users_language_info
    return users_language_info.get_minor_languages()

@app.route("/other")
def display_minor_language_info():
    return render_template('visualOther.html', name=None)

@app.route("/generate/info")
def get_info():
    global users_language_info
    return users_language_info.get_main_languages()

@app.route("/")
def display_info():
    return render_template('visual.html', name=None)
    

if __name__ == "__main__":
    username = ""
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else: 
        username = "mbostock"  # Default value
    users_language_info = GitLanguagesRetrieval(username)   #All computations done at the start
    app.run(host='0.0.0.0',port=5000,debug=True)