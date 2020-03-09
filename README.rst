.. image:: https://travis-ci.com/shlomikushchi/Simple-Pastebin-Parser.svg?branch=master
    :target: https://travis-ci.com/shlomikushchi/Simple-Pastebin-Parser

**********************
Simple-Pastebin-Parser
**********************

this is a simpler parser for the pastebin.com website.

it will iterate posts and parse their elements using lxml

installation:
#############


pip install simple-pastebin-parser


example usage
#############
.. code-block:: python

    import simple_pastebin_parser

    for paste in simple_pastebin_parser.get_pastes():
        print("Title: ", paste.Title)
        print("Author: ", paste.Author)
        print("date: ", paste.Date)
        print("Content: ")
        print(paste.Content)
        print("*" * 20)

Release notes:
################


v0.1.0 - P.O.C
*********************
initial proof of concept. nothing special, just doing the dirty work of parsing the posts.

how to execute:
1. create a virtual env of python 3.6
2. install requirements
3. run python poc.py


v0.2.5 (2020-03-07)
*********************

* integration with travis.ci


v0.2.6 (2020-03-07)
*********************

* changing the POC code to work with installed pypi package

v0.3.0 (2020-03-07)
*********************

* created the Paste() object for pastebin posts
* ability to stream data

v0.3.3 (2020-03-07)
*********************

* small fixes

v0.3.5 (2020-03-07)
*********************

* update README

v0.4.0 (2020-03-08)
*********************

* added documentation
* cleaned most pep8 issues
* some tests

v0.5.0 (2020-03-08)
*********************

* parse date in UTC
* add some logs
* add id to Paste()
