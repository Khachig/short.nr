from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/handle_url', methods=['POST'])
def handle_url():
    input_url = request.form['url_input']
    print(input_url)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
