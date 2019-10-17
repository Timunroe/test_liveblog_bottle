from tinydb import TinyDB, Query

sites = ['spectator', 'record', 'niagara', 'examiner']

for site in sites:
    db = TinyDB(f'''blogs/{site}.json''')
    db.table('pages')
    db.table('posts')
    db.close()

db = TinyDB('blogs/spectator.json')
pages = db.table('pages')
pages.insert({'title': 'Council June 24', 'date_created': '2019-06-24', 'status': 'live', 'DNN_asset': '9875678', 'script': 'council_june_24.js'})
pages.insert({'title': 'Weather June 9', 'date_created': '2019-06-09', 'status': 'live', 'DNN_asset': '9873451', 'script': 'weather_june_9.js'})
pages.insert({'title': 'Council July 7', 'date_created': '2019-07-07', 'status': 'live', 'DNN_asset': '9875984', 'script': 'council_july_7.js'})
posts = db.table('posts')
posts.insert({'headline': 'Wind wreaks havoc', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': 'live', 'rank': 'chrono', 'created': '2019-06-09', 'page_id': '1'})
posts.insert({'headline': 'Wind wreaks havoc 2', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': 'live', 'rank': 'chrono', 'created': '2019-06-09', 'page_id': '2'})
posts.insert({'headline': 'Wind wreaks havoc 3', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': 'live', 'rank': 'chrono', 'created': '2019-06-09', 'page_id': '3'})
posts.insert({'headline': 'Wind wreaks havoc 4', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': 'live', 'rank': 'chrono', 'created': '2019-06-09', 'page_id': '1'})

db.close()

db = TinyDB('blogs/examiner.json')
pages = db.table('pages')
pages.insert({'title': 'Council June 24', 'date_created': '2019-06-24', 'status': 'live', 'DNN_asset': '9875678', 'script': 'council_june_24.js'})
pages.insert({'title': 'Weather June 9', 'date_created': '2019-06-09', 'status': 'live', 'DNN_asset': '9873451', 'script': 'weather_june_9.js'})
pages.insert({'title': 'Council July 7', 'date_created': '2019-07-07', 'status': 'live', 'DNN_asset': '9875984', 'script': 'council_july_7.js'})
posts = db.table('posts')
posts.insert({'headline': 'Taxes going up 1', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': 'live', 'rank': '1', 'created': '2019-06-24', 'page_id': '1'})
posts.insert({'headline': 'Taxes going up 2', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': 'live', 'rank': '1', 'created': '2019-06-24', 'page_id': '2'})
posts.insert({'headline': 'Taxes going up 3', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': 'live', 'rank': '1', 'created': '2019-06-24', 'page_id': '3'})
posts.insert({'headline': 'Taxes going up 4', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': 'live', 'rank': '1', 'created': '2019-06-24', 'page_id': '2'})
db.close()

db = TinyDB('blogs/niagara.json')
pages = db.table('pages')
pages.insert({'title': 'Council June 24', 'date_created': '2019-06-24', 'status': 'live', 'DNN_asset': '9875678', 'script': 'council_june_24.js'})
pages.insert({'title': 'Weather June 9', 'date_created': '2019-06-09', 'status': 'live', 'DNN_asset': '9873451', 'script': 'weather_june_9.js'})
pages.insert({'title': 'Council July 7', 'date_created': '2019-07-07', 'status': 'live', 'DNN_asset': '9875984', 'script': 'council_july_7.js'})
posts = db.table('posts')
posts.insert({'headline': '1', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': '0', 'rank': 'chrono', 'created': '2019-07-07', 'page_id': '1'})
posts.insert({'headline': '2', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': '0', 'rank': 'chrono', 'created': '2019-07-07', 'page_id': '2'})
posts.insert({'headline': '3', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': '0', 'rank': 'chrono', 'created': '2019-07-07', 'page_id': '3'})
posts.insert({'headline': '4', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': '0', 'rank': 'chrono', 'created': '2019-07-07', 'page_id': '1'})
posts.insert({'headline': '5', 'raw': '<p>Hello</p><p>World</p>', 'processed': '<p>Hello</p><p>World</p>', 'status': '0', 'rank': 'chrono', 'created': '2019-07-07', 'page_id': '2'})
db.close()
