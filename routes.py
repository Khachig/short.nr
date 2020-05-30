import random
import string
import time

from flask import render_template, request, redirect, url_for
from app import app, db, URL

# URL prefix is localhost so redirects go through during development
PREFIX = '127.0.0.1:5000/'


# App logic
def in_db(shortened):
    all_urls = URL.query.all()
    for url in all_urls:
        if url.short == shortened:
            return True
    return False


def get_long_url(short_url):
    url_item = URL.query.get(short_url)
    return url_item.long


def db_cleanup():
    all_urls = URL.query.all()
    for url in all_urls:
        # If url hasn't been used for 3+ months
        if time.time() - url.timestamp > 8035200:
            db.session.delete(url)
    db.session.commit()


def db_update(short_url):
    url_item = URL.query.get(short_url)
    url_item.timestamp = time.time()
    db.session.commit()


@app.route('/')
def home():
    db_cleanup()
    return render_template('index.html', shortened=request.args.get('short'))


@app.route('/shortened', methods=['POST'])
def handle_url():
    input_url = request.form['url_input']
    random.seed(input_url)
    shortened = ''.join(
        [random.choice(string.ascii_letters) for i in range(15)]
    )

    if not in_db(shortened):
        item = URL(
            short=shortened,
            long=input_url,
            timestamp=time.time()
        )
        db.session.add(item)
        db.session.commit()

    return redirect(url_for('home', short=PREFIX+shortened))


@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    if not in_db(short_url):
        return render_template('error.html')
    db_update(short_url)
    return redirect(get_long_url(short_url))


if __name__ == '__main__':
    app.run(debug=True)
