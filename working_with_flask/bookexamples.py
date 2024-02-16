from flask import Flask, url_for, request, make_response, redirect, abort
from flask import render_template

# from flask.ext.script import Manager
# manager = Manager(app)

app = Flask(__name__, template_folder='templates')


@app.route('/')
def main():
    return '<h1>bububu</h1>'
    # return redirect('http://www.example.com')


@app.route('/user/<name>')
def greet(name):
    return render_template('user.html', name=name)


if __name__ == "__main__":
    print(app.url_map)
    # manager.run()
    app.run(debug=True)