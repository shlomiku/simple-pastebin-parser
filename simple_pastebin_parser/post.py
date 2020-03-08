import dateutil.parser

from simple_pastebin_parser.utils import parse_html, Url


def pastebin_post_url(href):
    """
    the post url in pastebin.com
    :param href: a string that is structured like so: /<uniqe_id>. e.g /j59FEXhf
    :return: legit pastebin url
    """
    return 'https://pastebin.com{}'.format(href)


class Post(object):
    def __init__(self, href: str) -> None:
        self.tree = parse_html(Url(pastebin_post_url(href)))
        self.author = self.parse_author()
        self.title = self.parse_title()
        self.date = self.parse_date()
        self.code = self.parse_code()

    def parse_author(self):
        """
        under paste_box_line2 we have the user, date, etc.
        when we do have a valid user (not guest) we have <a></a> elements under it
        the first one, is the user. so these are equivalent:
        "//div[contains(@class, 'paste_box_line2')]/a" => <div class="paste_box_line2"><a> User</a> ... </div>
        when there's no logged in user, there's no <a> elements under, paste_box_line2. so this will raise
        that way w][][]e know it's a guest
        :return:
        """
        try:
            author = self.tree.xpath("//div[contains(@class, 'paste_box_line2')]/a")[0].text
        except IndexError:
            author = "Guest"
        return author

    def parse_title(self):
        """
        the title is located in a h1 tag under the paste_box_line1 element.
        it is also the only h1 element in the entire document.
        we could by searching all h1 and get the only one:
            self.title = self.tree.xpath("//h1")[0].text
        we could get the children of paste_box_line1, it will be the first child:
            self.title = self.tree.xpath("//div[contains(@class, 'paste_box_line1')]")[0].getchildren()[0].text
        but we will get the h1 under paste_box_line1 to make it more readable like so:
            self.title = self.tree.xpath("//div[@class='paste_box_line1']/h1")[0].text
        :return:
        """
        return self.tree.xpath("//div[@class='paste_box_line1']/h1")[0].text

    def parse_date(self):
        """
        the date is in the first span under paste_box_line1
        :return:
        """
        return dateutil.parser.parse(self.tree.xpath("//div[contains(@class, 'paste_box_line2')]/span")[0].text)

    def parse_code(self):
        """
        code has an id 'paste_code'. we could just search for that id directly
        :return:
        """
        return self.tree.xpath("//textarea[contains(@id, 'paste_code')]")[0].text

