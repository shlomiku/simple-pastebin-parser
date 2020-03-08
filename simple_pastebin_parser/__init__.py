"""Top-level package for simple pastebin parser."""

__author__ = """Shlomi Kushchi"""
__email__ = 'shlomik@example.com'

from time import sleep

from simple_pastebin_parser.paste import Paste
from simple_pastebin_parser.utils import parse_html, Url

KNOWN_HREFS = ['/favicon.ico', '/i/pastebin.min.v9.css?1575389335', '/pro', '/api', '/faq', '/login', '/signup',
               '/archive', '/tools#chrome', '/languages', '/archive', '/faq', '/night_mode', '/dmca', '/contact']

KNOWN_PREFIXES = ['http://', 'https://', '/tools', '/doc_', '/archive/']
PASTEBIN_ARCHIVE_URL = 'https://pastebin.com/archive'


def trim_pastes_cache(hrefs):
    """
    make sure we don't cache too much data.
    if we have more than 1000 drop the first 100 ( threshold is arbitrary )
    :param hrefs:
    :return:
    """
    if len(hrefs) > 1000:
        hrefs = hrefs[100:]


def get_pastes(should_stream: bool=False, sampling_frequency=60 * 2):
    """
    get the current pastes on pastebin.com.
    if should_stream is False we get a snapshot of current pastes
    if should_stream is True we will sample the site every sampling_frequency for new pastes
    and yield them as they come

    :return: yields pastes
    """
    hrefs = []
    while 1:
        tree = parse_html(Url(PASTEBIN_ARCHIVE_URL))
        new_hrefs = get_current_pastes_ids(tree)

        for href in new_hrefs:
            if href not in hrefs:
                yield Paste(href)
                hrefs.append(href)
        trim_pastes_cache(hrefs)
        sleep(sampling_frequency)
        if not should_stream:
            break


def get_current_pastes_ids(tree):
    """

    :param tree:
    :return:
    """
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
    return hrefs

