data = {
    "pages": [
        {
            "title": "weather nov 9", "slug": "weather-nov-9", "timestamp": "11-09-2018", "posts": [
                {"headline": "Warning ended", "slug": "random5", "timestamp": "11-09-2018", "author": "Dave Phillips", "content": "Dolor id amet duis labore duis laboris fugiat veniam. Duis cillum est ad deserunt excepteur minim non sint eu nisi exercitation duis ex. Anim culpa elit excepteur Lorem aliqua voluptate consequat est. Laborum laborum elit est duis nisi quis laborum sunt ad sint ea eiusmod dolor reprehenderit. Labore reprehenderit veniam deserunt pariatur dolore Lorem voluptate exercitation do tempor."},
                {"headline": "", "slug": "random8", "timestamp": "11-09-2018", "author": "Jim Brown", "content": "Do eu dolor excepteur officia aliqua consectetur excepteur. Velit duis enim veniam laborum quis. Aliqua consequat fugiat aute aliquip ad adipisicing culpa occaecat do quis ex. Ex consequat excepteur laborum dolor dolor reprehenderit adipisicing velit consectetur eiusmod. Veniam culpa mollit aliquip laboris reprehenderit. Id consequat ad amet ad irure officia aute veniam sit veniam aute mollit."},
                {"headline": "Heavy rain warning", "slug": "heavy-rain-warning", "timestamp": "11-09-2018", "author": "Dave Phillips", "content": "Id consectetur proident fugiat consequat sint enim exercitation dolore. Nulla voluptate reprehenderit aute ea minim adipisicing. Fugiat nulla cupidatat incididunt laborum tempor ipsum. Non magna veniam eu nulla ipsum quis ea quis occaecat laborum cillum. Nisi qui nisi aute ea amet ullamco esse aliqua. Eu officia anim minim dolore incididunt cillum enim. Amet anim tempor aliqua esse elit tempor nostrud."},
            ]
        },
        {
            "title": "council nov 4", "slug": "council-nov-4", "timestamp": "11-04-2018", "posts": [
                {"headline": "Council votes 15-1", "slug": "random3", "timestamp": "11-09-2018", "author": "Sydney Green", "content": "Esse amet minim dolor aliquip. Adipisicing incididunt ex officia labore. Nulla consectetur non Lorem magna in nulla. Quis velit sint incididunt id elit cupidatat exercitation eu est. Ea sint veniam eiusmod quis veniam consequat."},
                {"headline": "", "slug": "random1", "timestamp": "11-09-2018", "author": "Sydney Green", "content": "Reprehenderit eiusmod id dolor qui amet tempor enim ullamco ea. Dolor tempor adipisicing deserunt cupidatat. Amet qui laboris cillum et nisi eiusmod deserunt voluptate adipisicing. Et labore veniam cillum non id cupidatat exercitation consequat deserunt laborum. Minim eiusmod quis consectetur magna occaecat voluptate veniam laborum sunt tempor amet. Excepteur incididunt laboris minim labore nulla culpa nulla."},
                {"headline": "Report recommends demolition", "slug": "report-recommends-demolition", "timestamp": "11-09-2018", "author": "Sydney Green", "content": "Ullamco do minim cupidatat id id esse nulla ullamco enim excepteur est nulla. Non est occaecat tempor nulla laborum ad nisi labore excepteur id cupidatat cupidatat amet enim. Proident enim mollit irure officia sit. Qui amet commodo eu non non Lorem occaecat et. Ea enim sit nostrud dolore. Esse velit dolor elit enim ipsum ut ea fugiat."},
            ]
        },
        {
            "title": "Breaking news nov 6", "slug": "breaking-news-nov-6", "timestamp": "11-06-2018", "posts": [
                {"headline": "Council votes 15-1", "slug": "council-votes-15-1", "timestamp": "11-09-2018", "author": "Sydney Green", "content": "Id veniam ipsum aliquip excepteur sunt est. Pariatur ad nostrud et reprehenderit fugiat aliqua Lorem ad et. Eiusmod laboris est aliqua aliquip qui aute. Elit deserunt mollit officia veniam sint culpa cupidatat."},
                {"headline": "", "slug": "random2", "timestamp": "11-09-2018", "author": "Sydney Green", "content": "Elit aliquip ullamco deserunt ut qui deserunt ad occaecat sunt elit. Culpa elit fugiat consectetur est. Magna magna adipisicing et ut aliqua laboris ea duis eiusmod."},
                {"headline": "Report recommends demolition", "slug": "report-recommends-demolition", "timestamp": "11-09-2018", "author": "Sydney Green", "content": "In aliquip excepteur est nisi duis ea. Exercitation ad pariatur cillum minim non qui in velit aliquip. Ad minim nisi dolor irure. Ad ex exercitation magna ut laboris ullamco qui est in fugiat non cillum dolore pariatur. Ad reprehenderit duis aute ipsum labore tempor aliquip incididunt aliquip aute cupidatat."},
            ]
        },
    ]
}


def get_pages():
    pages_list = [(item["title"], item["slug"]) for item in data["pages"]]
    return pages_list


def get_posts(page):
    posts_list = next((item for item in data["pages"] if item["slug"] == page))
    print(posts_list)
    return posts_list
