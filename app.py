from bottle import Bottle, run, template, request, static_file
import db

app = Bottle()


@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


@app.route('/')
def index():
    # get list of pages
    return template('index.html', data=db.get_pages())


@app.route('/page/<page_id>')
def posts(page_id):
    # get list of posts for this page
    return template('page.html', data=db.get_posts(page_id))


@app.route('/edit/<page_id>/<post_id>')
def edit(page_id, post_id):
    # get post specified
    # post = db.get_posts(page_id, post_id)
    # author = db.get_author(post['author'])
    return template('edit.html', data=db.get_posts(page_id, post_id), authors=db.get_authors(), ref_page=page_id)


@app.route('/save/<page_id>/<post_id>', method='POST')
def save(page_id, post_id):
    # get list of posts for this page
    print("Page id: ", page_id)
    print("Post id: ", post_id)
    content = request.forms.get('content')
    print("Content: ", content.replace('\r\n', ''))


run(app, host='localhost', port=8080, debug=True)
