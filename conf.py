alphabets = {
	"en": "abcdefghijklmnopqrstuvwxyz",
	"es": "aábcdeéfghiíjklmnñoópqrstuúüvwxyz"
}

block_size = 7
characters_per_line = 40
cipher_delim = "-"
count = 7
default_has_hint = True
default_is_patristocrat = False
default_language = "en"
has_hint = [False] # TODO revert this to []
hint_pat = ", pat"
hint_text = "[%s%s] Hint: %s"

html_extension = ".html"
html_footer = "</body></html>"
html_header = "<!DOCTYPE html><html>%s<body>"
html_line_break = "<br />"
html_style = "<style>body { font-family: Fira Code; }</style>"
html_header %= html_style

is_patristocrat = [True]
languages = ["es"]
lookgoodq = "Does this quote look good [y/N]? "
no_hint = "|> NO HINT! ( sorry :( ) <|"

quote_minlen = 50
quote_maxlen = 250

quotes_json = "quotes.json"

spaces_character = "&nbsp;"
tab_size = 2

txt_key = "key.txt"
txt_ciphers = "cipher.txt"

vertical_lines = False
cipher_delim = cipher_delim * ((characters_per_line * 4 - 1) if vertical_lines else \
	(characters_per_line * 3)) + "\n"

wikiquote_page = "https://%s.wikiquote.org/wiki/%s"
