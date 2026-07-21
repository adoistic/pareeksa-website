from html.parser import HTMLParser

class MenuParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_mega = False
        self.in_col = False
        self.in_title = False
        self.in_a = False
        self.current_title = ""
        self.current_href = ""
        self.current_text = ""
        self.menu_data = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        if 'nav-mega-menu' in classes:
            self.in_mega = True
        elif self.in_mega and 'nav-mega-column' in classes:
            self.in_col = True
        elif self.in_col and 'nav-mega-title' in classes:
            self.in_title = True
            self.current_title = ""
        elif self.in_col and tag == 'a':
            self.in_a = True
            self.current_href = attrs_dict.get('href', '')
            self.current_text = ""

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_col and not self.in_title:
            pass
        elif self.in_title and tag == 'h4':
            self.in_title = False
        elif self.in_a and tag == 'a':
            self.in_a = False
            self.menu_data.append((self.current_title, self.current_text.strip(), self.current_href.strip()))

    def handle_data(self, data):
        if self.in_title:
            self.current_title += data
        elif self.in_a:
            self.current_text += data

parser = MenuParser()
parser.feed(open('index.html', encoding='utf-8').read())
current_cat = None
for cat, text, href in parser.menu_data:
    if cat != current_cat:
        print(f"\n--- {cat} ---")
        current_cat = cat
    print(f"  - '{text}' -> {href}")
