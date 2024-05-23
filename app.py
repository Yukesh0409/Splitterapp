import os
import Split
from flask import Flask, render_template, request

app = Flask("__splitterapp__")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home2():
    return render_template('home.html')

@app.route('/instruction')
def instruction():
    return render_template('instruction.html')

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == "POST":
        print("file received")
        print(request.files['directory'])
        print(request.form['groupName'])
        print(request.form['receiversName'])
        file = request.files['directory']
        if file:
            print("folder found")
            folder_path = os.path.abspath(os.path.dirname(file.filename))
            print(folder_path)
            print("Sending for spliting")
            Split.start_split(folder_path)
        else:
            return render_template('send.html')
        return render_template('send.html')
    else:
        return render_template('send.html')

@app.route('/receive')
def receive():
    return render_template('receive.html')

if __name__ == '__main__':
    app.run(debug=True)