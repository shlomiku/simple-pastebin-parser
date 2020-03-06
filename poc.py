from pprint import pprint

from lxml import html
import requests
import dateutil.parser

KNOWN_HREFS = ['/favicon.ico', '/i/pastebin.min.v9.css?1575389335', '/pro', '/api', '/faq', '/login', '/signup',
               '/archive', '/tools#chrome', '/languages', '/archive', '/faq', '/night_mode', '/dmca', '/contact']

KNOWN_PREFIXES = ['http://', 'https://', '/tools', '/doc_', '/archive/']

if __name__ == '__main__':
    page = requests.get('https://pastebin.com/archive')
    tree = html.fromstring(page.content)
    unfiltered_hrefs = [ref for ref in tree.xpath("//@href") if ref not in KNOWN_HREFS]
    hrefs = []
    for href in unfiltered_hrefs:
        is_pastebin_href = True
        for prefix in KNOWN_PREFIXES:
            if str(href).startswith(prefix):
                is_pastebin_href = False
                break
        if is_pastebin_href:
            hrefs.append(href)

    hrefs = [href for href in hrefs if len(href) > 5]

    for href in hrefs[:10]:
        page = requests.get('https://pastebin.com{}'.format(href))
        tree = html.fromstring(page.content)
        # title = tree.xpath("//h1")[0].text
        # title = tree.xpath("//div[@class='paste_box_line1']/h1")[0].text
        title = tree.xpath("//div[contains(@class, 'paste_box_line1')]")[0].getchildren()[0].text
        try:
            author = tree.xpath("//div[contains(@class, 'paste_box_line2')]/a")[0].text
        except:
            author = "Guest"
        date = dateutil.parser.parse(tree.xpath("//div[contains(@class, 'paste_box_line2')]/span")[0].text)
        code = tree.xpath("//textarea[contains(@id, 'paste_code')]")[0].text
        print("href: ", href)
        print("Title: ", title)
        print("Author: ", author)
        print("date: ", date)
        print(code)
        print("*"*20)
        print("*"*20)
