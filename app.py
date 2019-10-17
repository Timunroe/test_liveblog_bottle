from bottle import Bottle, run, template, request, static_file
from tinydb import TinyDB, Query
import micawber
import db

providers = micawber.bootstrap_basic()

HOST = '0.0.0.0'
PORT = 5002

app = Bottle()

'''
Need app to allow user to create a stream of a blog page
-- a stream of micro-posts,
either text/HTML, or Twitter/Instagram/Youtube embed ---
and publish as a .json file to S3,
so a javascript script linked to a DNN article will pull it in,
parse and add the HTML to certain divs.
+++
NEED TABLE FOR EACH 'blog/page'.
'''


def munge_text(data):
    # fixes for text imported from form
    # Need to wrap youtube link with responsive div,
    # Need to wrap img tag with responsive figure wrapper
    # before calling micawber
    print("Raw data: ", data)
    temp = ''
    for line in data.splitlines():
        if 'youtube.com' in line:
            temp += f'''<div class="embed-container">{line.replace('<p>', '').replace('</p>', '')}</div>'''
        elif 'IMG:' in line:
            img_url = line.replace('<p>IMG:', '').replace('</p>', '').strip()
        elif 'CAP:' in line:
            line = line.replace('<p>CAP:', '').replace('</p>', '').strip()
            temp += f'''<figure style="margin: 0;"><img style="width: 100%;" src="{img_url}" alt="{line}"><figcaption style="font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-weight: bold;">{line}</figcaption></figure>'''
        elif '<blockquote' in line:
            temp += f'''{line}<span style="color: grey; float: left; font-size: 52px; line-height: 1; font-weight: bold; margin-right: 9px;">“</span><div style="margin-left: 35px;">'''
        elif '/blockquote' in line:
            temp += f'''</div>{line}'''
        else:
            temp += line
    '''
    <div class='embed-container'><iframe src='https://www.youtube.com/embed/QILiHiTD3uc' frameborder='0' allowfullscreen></iframe></div>
    ---
    <figure style="margin: 0;">
    <img style="width: 100%;" src="xxxxxxxx" alt=".">
    <figcaption style="font-family: Arial, Helvetica, sans-serif; font-size: 12px; font-weight: bold;">XXXXXXXX</figcaption></figure>

    '''
    # need to modify iframes with youtube
    return providers.parse_html(temp)


non_url_safe = ['"', '#', '$', '%', '&', '+',
                ',', '/', ':', ';', '=', '?',
                '@', '[', '\\', ']', '^', '`',
                '{', '|', '}', '~', "'"]
translate_table = {ord(char): u'' for char in non_url_safe}


def slugify(text):
    text = text.translate(translate_table)
    text = u'_'.join(text.split())
    return text


sites = ['spectator', 'record', 'niagara', 'examiner']
default = 'spectator'
for site in sites:
    TinyDB(f'''./blogs/{site}.json''')

# db = TinyDB(f'''./blogs/{default}.json''')


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
        return template('page_edit.html', data=None)
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
        content = munge_text(request.forms.get('content'))
        print("\nCONTENT: \n", content)
    else:
        # it's a new blog page
        # create new entry in site db file's 'pages' table
        # create a new table in site db file
        print("Page id: ", page_id)
        title = request.forms.get('title')
        page_name = slugify(title)
        print("Title: ", slugify(page_name))
        # db.table('table_name')


run(app, host=HOST, port=PORT, debug=True, reloader=True)
