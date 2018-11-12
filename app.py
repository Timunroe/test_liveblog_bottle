from bottle import Bottle, run, template
import db

app = Bottle()


@app.route('/')
def index():
    # get list of pages
    return template('index.html', data=db.get_pages())


@app.route('/page/<page>')
def posts(page):
    # get list of posts for this page
    return template('page.html', data=db.get_posts(page))


run(app, host='localhost', port=8080, debug=True)
