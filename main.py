from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def generate_url(seed):
    new_url = seed[:5]
    return new_url


@app.route('/')
def home():
    return render_template('index.html', shortened=request.args.get('short'))


@app.route('/handle_url', methods=['POST'])
def handle_url():
    input_url = request.form['url_input']
    shortened = generate_url(input_url)
    return redirect(url_for('home', short=shortened))


if __name__ == '__main__':
    app.run(debug=True)
