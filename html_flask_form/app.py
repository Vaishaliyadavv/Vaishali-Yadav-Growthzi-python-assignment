from flask import Flask, render_template, redirect, request

app = Flask(__name__)  # object -> WSGI application


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/home')
def red_home():
    return redirect('/')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        information = request.form.to_dict()  # Convert ImmutableMultiDict to dictionary

    return render_template("submit.html", data=information)


# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         information = request.form

#     return render_template("submit.html", data=information)

if __name__ == '__main__':
    app.run(debug=True)
