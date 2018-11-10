from flask import Flask
app = Flask(__name__)
info_to_display = ""

def set_display_info(string):
    global info_to_display 
    info_to_display = string


@app.route("/")
def display_info():
    global  info_to_display
    return info_to_display
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
