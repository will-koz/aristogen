alphabets = {
	"en": "abcdefghijklmnopqrstuvwxyz",
	"es": "aábcdeéfghiíjklmnñoópqrstuúüvwxyz"
}

characters_per_line = 40
cipher_delim = "-" * characters_per_line * 3 + "\n"
count = 7
default_language = "en"
hint_text = "[%s] Hint: %s"

html_extension = ".html"
html_footer = "</body></html>"
html_header = "<!DOCTYPE html><html>%s<body>"
html_line_break = "<br />"
html_style = "<style>body { font-family: Fira Code; }</style>"
html_header %= html_style

languages = ["es"]
lookgoodq = "Does this data look good [y/N]? "

quote_minlen = 50
quote_maxlen = 250

quotes_json = "quotes.json"

txt_key = "key.txt"
txt_ciphers = "ciphers.txt"

wikiquote_page = "https://%s.wikiquote.org/wiki/%s"
