#!/usr/bin/python3

import conf
import utils

page_titles = []
raw_quotes = []

utils.setup_lang()

utils.choose_quotes(page_titles, raw_quotes)

utils.save_quotes_as_json(page_titles, raw_quotes)
