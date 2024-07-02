from flask import Flask, render_template
''' A basic Flask app that Create a single / route and an index.html '''


app = Flask(__name__)


@app.route('/')
def index():
    ''' renders index.html template '''
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
