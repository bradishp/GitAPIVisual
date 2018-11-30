import sys
from flask import Flask, render_template
from gitRetrieval import GitLanguagesRetrieval


app = Flask(__name__)

@app.route("/username")
def get_username():
    global users_language_info
    return users_language_info.get_username()

@app.route("/collaborators/generate/info")
def get_average_collaborators():
    global users_language_info
    return users_language_info.get_average_collaborators()

@app.route("/collaborators")
def display_average_collaborators():
    return render_template('visualCollaborators.html', name=None)

@app.route("/additional/generate/info")
def get_number_of_appearences():
    global users_language_info
    return users_language_info.get_languages_appearences()

@app.route("/additional")
def display_number_of_appearences():
    return render_template('visualNumberOfRepos.html', name=None)

@app.route("/other/generate/info")
def get_minor_language_info():
    global users_language_info
    return users_language_info.get_minor_languages()

@app.route("/other")
def display_minor_language_info():
    return render_template('visualOtherLanguages.html', name=None)

@app.route("/generate/info")
def get_info():
    global users_language_info
    return users_language_info.get_main_languages()

@app.route("/")
def display_info():
    return render_template('visualMain.html', name=None)
    

if __name__ == "__main__":
    username = "mbostock"   # Default values
    tokken = ""
    if len(sys.argv) > 1:   # Can specify from the command line
        username = sys.argv[1]
    if len(sys.argv) > 2:
        tokken = sys.argv[2]  
    users_language_info = GitLanguagesRetrieval(username, tokken)   # All data is retrieved and processed before the server is run
    app.run(host='0.0.0.0',port=5000,debug=True)