import dateutil.parser

from simple_pastebin_parser.utils import parse_html, Url

PASTEBIN_POST_URL = lambda href: 'https://pastebin.com{}'.format(href)


class Post(object):
    def __init__(self, href: str) -> None:
        self.tree = parse_html(Url(PASTEBIN_POST_URL(href)))
        self.parse_author()
        self.parse_title()
        self.parse_date()
        self.parse_code()

    def parse_author(self):
        try:
            self.author = self.tree.xpath("//div[contains(@class, 'paste_box_line2')]/a")[0].text
        except:
            self.author = "Guest"

    def parse_title(self):
        # self.title = self.tree.xpath("//h1")[0].text
        # self.title = self.tree.xpath("//div[@class='paste_box_line1']/h1")[0].text
        self.title = self.tree.xpath("//div[contains(@class, 'paste_box_line1')]")[0].getchildren()[0].text

    def parse_date(self):
        self.date = dateutil.parser.parse(self.tree.xpath("//div[contains(@class, 'paste_box_line2')]/span")[0].text)

    def parse_code(self):
        self.code = self.tree.xpath("//textarea[contains(@id, 'paste_code')]")[0].text


if __name__ == '__main__':
    p = Post("/j59FEXhf")
    print("author: {}".format(p.author))
    print("title: {}".format(p.title))
    print("date: {}".format(p.date))
    print("code: {}".format(p.code))
