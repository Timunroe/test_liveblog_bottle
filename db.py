from operator import itemgetter

db = {
    "authors": [
        {"name": "Steve Milton", "lname": "Milton", "twitter": "miltonatthespec", "email": "smilton@thespec.com", "img": "https://dynamicmedia.zuza.com/zz/m/cropped_140x210/6/9/693a770a-7a2e-43eb-92ba-8b51acdafc50/smilton-authorbio.jpg"},
        {"name": "Matthew Van dongen", "lname": "Van Dongen", "twitter": "mattatthespec", "email": "mvandongen@thespec.com", "img": "https://dynamicmedia.zuza.com/zz/m/cropped_140x210/6/7/67596cc1-f2d3-41ea-9a16-eae81fc682b3/mvandongen-authorbio.jpg"},
        {"name": "Nicole O'Reilly", "lname": "O'Reilly", "twitter": "nicoleatthespec", "email": "noreilly@thespec.com", "img": "https://dynamicmedia.zuza.com/zz/m/cropped_140x210/a/0/a070cded-9302-4649-95df-1e5ddf819f3e/noreilly-authorbio.jpg"},
        {"name": "Natalie Paddon", "lname": "Paddon", "twitter": "natatthespec", "email": "npaddon@thespec.com", "img": "https://dynamicmedia.zuza.com/zz/m/cropped_140x210/b/c/bc25c4b8-1ca6-4098-87bd-c0b59e504738/natalie.jpg"},
    ],
    "pages": [
        {
            "title": "weather nov 9", "page_id": "1", "slug": "weather-nov-9", "timestamp": "11-09-2018", "DNN_asset": "", "posts": [
                {"headline": "Warning ended", "status": "live", "post_id": "1", "timestamp": "11-09-2018", "author": "Natalie Paddon", "content": "<p>Chambray <b>hoodie</b> cornhole, <em>neutra DIY</em> narwhal kombucha. &#8220;Bob&#8221;, he said. &#8220;Don&#8217;t go.&#8221; Yuccie squid literally drinking vinegar aesthetic typewriter. Normcore poke microdosing chillwave VHS godard. Aesthetic artisan chartreuse affogato plaid squid bespoke DIY.</p>"},
                {"headline": "", "status": "draft", "post_id": "2", "timestamp": "11-09-2018", "author": "Natalie Paddon", "content": "<p>Man braid next level coloring book tumblr waistcoat air plant. Twee XOXO intelligentsia lyft, butcher air plant taiyaki kitsch echo park trust fund. Brooklyn hell of keytar cred gastropub raclette. Hell of pug beard, copper mug fam disrupt kickstarter four dollar toast. Four dollar toast lo-fi single-origin coffee plaid af selfies messenger bag cardigan typewriter authentic.</p>"},
                {"headline": "Heavy rain warning", "status": "live", "post_id": "3", "timestamp": "11-09-2018", "author": "Nicole O'Reilly", "content": "<p>Air plant celiac snackwave lumbersexual jianbing. Pour-over letterpress taxidermy pickled prism tilde. Franzen meh VHS enamel pin pork belly. Yr tumeric snackwave, squid vinyl hammock prism cray swag truffaut scenester food truck vexillologist.</p>"},
            ]
        },
        {
            "title": "council nov 4", "page_id": "2", "slug": "council-nov-4", "timestamp": "11-04-2018", "DNN_asset": "", "posts": [
                {"headline": "Council votes 15-1", "status": "live", "post_id": "1", "timestamp": "11-09-2018", "author": "Matthew Van Dongen", "content": "<p>Esse amet minim dolor aliquip. Adipisicing incididunt ex officia labore. Nulla consectetur non Lorem magna in nulla. Quis velit sint incididunt id elit cupidatat exercitation eu est. Ea sint veniam eiusmod quis veniam consequat.</p>"},
                {"headline": "", "status": "live", "post_id": "2", "timestamp": "11-09-2018", "author": "Matthew Van Dongen", "content": "<p>Reprehenderit eiusmod id dolor qui amet tempor enim ullamco ea. Dolor tempor adipisicing deserunt cupidatat. Amet qui laboris cillum et nisi eiusmod deserunt voluptate adipisicing. Et labore veniam cillum non id cupidatat exercitation consequat deserunt laborum. Minim eiusmod quis consectetur magna occaecat voluptate veniam laborum sunt tempor amet. Excepteur incididunt laboris minim labore nulla culpa nulla.</p>"},
                {"headline": "Report recommends demolition", "status": "live", "post_id": "3", "timestamp": "11-09-2018", "author": "Matthew Van Dongen", "content": "<p>Ullamco do minim cupidatat id id esse nulla ullamco enim excepteur est nulla. Non est occaecat tempor nulla laborum ad nisi labore excepteur id cupidatat cupidatat amet enim. Proident enim mollit irure officia sit. Qui amet commodo eu non non Lorem occaecat et. Ea enim sit nostrud dolore. Esse velit dolor elit enim ipsum ut ea fugiat.</p>"},
            ]
        },
        {
            "title": "Breaking news nov 6", "page_id": "3", "slug": "breaking-news-nov-6", "timestamp": "11-06-2018", "DNN_asset": "", "posts": [
                {"headline": "Council votes 15-1", "status": "live", "post_id": "1", "timestamp": "11-09-2018", "author": "Steve Milton", "content": "Id veniam ipsum aliquip excepteur sunt est. Pariatur ad nostrud et reprehenderit fugiat aliqua Lorem ad et. Eiusmod laboris est aliqua aliquip qui aute. Elit deserunt mollit officia veniam sint culpa cupidatat."},
                {"headline": "", "status": "live", "post_id": "2", "timestamp": "11-09-2018", "author": "Nicole O'Reilly", "content": "Elit aliquip ullamco deserunt ut qui deserunt ad occaecat sunt elit. Culpa elit fugiat consectetur est. Magna magna adipisicing et ut aliqua laboris ea duis eiusmod."},
                {"headline": "Report recommends demolition", "status": "live", "post_id": "3", "timestamp": "11-09-2018", "author": "Natalie Paddon", "content": "In aliquip excepteur est nisi duis ea. Exercitation ad pariatur cillum minim non qui in velit aliquip. Ad minim nisi dolor irure. Ad ex exercitation magna ut laboris ullamco qui est in fugiat non cillum dolore pariatur. Ad reprehenderit duis aute ipsum labore tempor aliquip incididunt aliquip aute cupidatat."},
            ]
        },
    ]
}


def get_pages():
    pages_list = [(item["title"], item["page_id"]) for item in db["pages"]]
    return pages_list


def get_posts(page_id, post_id=None):
    page = next((item for item in db["pages"] if item["page_id"] == page_id))
    # print(page)
    if post_id:
        post = next((item for item in page['posts'] if item["post_id"] == post_id))
        return post
    else:
        # print(posts_list)
        return page


def get_author(name):
    author = next((item for item in db["authors"] if item["name"].lowercase() == name.lowercase()))
    return author


def get_authors():
    authors = sorted(db['authors'], key=itemgetter('lname'))
    return authors
