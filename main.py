from flask import Flask, render_template

app = Flask(__name__)
app.secret_key='112'


@app.route('/')
def index():
    return render_template('Homepage.html') 

if __name__=='__main__':
    app.run(debug=True)