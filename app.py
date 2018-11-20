from bottle import Bottle, run, template, request, static_file
import db

app = Bottle()


@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


@app.route('/')
def index():
    # get list of pages
    return template('pages.html', data=db.get_pages())


@app.route('/page/<page_id>')
def posts(page_id):
    # if id is 'new', then create page
    if page_id == 'new':
        return None
    # else get list of posts for this page
    else:
        return template('page.html', data=db.get_posts(page_id))


@app.route('/edit/page/<page_id>')
@app.route('/edit/page/<page_id>/post/<post_id>')
def edit(page_id, post_id=None):
    # dealing with editing a new page or existing page
    if post_id is None:
        return template('page_edit.html', data=db.get_posts(page_id, post_id))
    else:
        # dealing with editing or creating a new post belonging to a page
        return template('post_edit.html', data=db.get_posts(page_id, post_id), authors=db.get_authors())

@app.route('/save/page/<page_id>', method='POST')
@app.route('/save/page/<page_id>/post/<post_id>', method='POST')
def save(page_id, post_id=None):
    # get list of posts for this page
    if post_id:
        print("Page id: ", page_id)
        print("Post id: ", post_id)
        content = request.forms.get('content')
        print("Content: ", content.replace('\r\n', ''))
    else:
        print("Page id: ", page_id)
        title = request.forms.get('title')
        print("Title: ", title)


run(app, host='localhost', port=8080, debug=True, reloader=True)
