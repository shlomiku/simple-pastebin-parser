
import requests
from lxml import html

PASTEBIN_URL_PREFIX = "https://pastebin.com/"


class InvalidPastebinUrl(Exception):
    pass


class Url:
    def __init__(self, url: str, ):
        if not url.startswith(PASTEBIN_URL_PREFIX):
            raise InvalidPastebinUrl("not a valid pastebin url")
        self.url = url

    def __repr__(self):
        return self.url


def parse_html(url: Url):
    page = requests.get(str(url))
    return html.fromstring(page.content)


if __name__ == '__main__':
    try:
        print("{}".format(Url("shlomi")))
    except InvalidPastebinUrl:
        pass

    print("{}".format(Url("https://pastebin.com/j59FEXhf")))
