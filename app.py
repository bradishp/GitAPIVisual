from flask import Flask, render_template
from gitRetrieval import generate_info
app = Flask(__name__)

@app.route("/generate/info")
def get_info():
    json_projects = generate_info("XanthusXX")
    return json_projects

@app.route("/")
def display_info():
    return render_template('visual.html', name=None)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
